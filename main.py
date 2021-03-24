import requests
import os
import json
import argparse

from datetime import date, timedelta

token = os.environ['AUTH_TOKEN']
token = f'Bearer {token}'



def get_user_id(username):
  url = f'https://gitlab.scicrop.com/api/v4/users'
  headers = {
      "Authorization": token,
  }
  r = requests.get(url, headers=headers)

  res = json.loads(r.text)

  for item in res:
    if item['username'] == username:
      return item['id']
    
  raise Exception('Username not found')



def time_spent_today(user_id):
  sec_spent=0
  page = 1
  loop = True
  count_issues = 0

  while loop:
    url = f'https://gitlab.scicrop.com/api/v4/projects/4/issues?page={str(page)}&per_page=50'
    headers = {
      "Authorization": token,
    }
    r = requests.get(url, headers=headers)

    res = json.loads(r.text)
    total_pages = int(r.headers['X-Total-Pages'])

    for item in res:
      for assignee in item['assignees']:
          if assignee['id'] == user_id:
            if item['due_date']:
              due = date.fromisoformat(item['due_date'])
              if due.weekday() < date.today().weekday():
                loop = False
                break
              if date.today() - due == timedelta(days=0) and 'Entregue' in item['labels']:
                sec_spent += item['time_stats']['total_time_spent']
                count_issues += 1
    
    if page < total_pages:
      page+=1
    else:
      break
    
  min_spent = sec_spent/60
  hour_spent = min_spent/60
    
  return hour_spent



def time_spent_this_week(user_id):
  sec_spent=0
  page = 1
  loop = True
  count_issues = 0

  today = date.today()
  days_behind = today.weekday()

  while loop:
    url = f'https://gitlab.scicrop.com/api/v4/projects/4/issues?page={str(page)}&per_page=50'
    headers = {"Authorization": token}
    r = requests.get(url, headers=headers)

    res = json.loads(r.text)
    total_pages = int(r.headers['X-Total-Pages'])
    
    for item in res:
      for assignee in item['assignees']:
          if assignee['id'] == user_id:
            if item['due_date'] and 'Entregue' in item['labels']:
              due = date.fromisoformat(item['due_date'])
              if date.today() - due <= timedelta(days=days_behind):
                sec_spent += item['time_stats']['total_time_spent']
                count_issues+=1
              else:
                loop = False
                break

    if page < total_pages:
      page+=1
    else:
      break
  
  min_spent = sec_spent/60
  hour_spent = min_spent/60

  return hour_spent




if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument('username')
  parser.add_argument('--today', action='store_true')
  parser.add_argument('--week', action='store_true')

  args = parser.parse_args()

  username = args.username
  today = args.today
  week = args.week

  user_id = get_user_id(username)

  if today:
    print(time_spent_today(user_id))

  elif week:
    print(time_spent_this_week(user_id))

