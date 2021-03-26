# Track my issues on GitLab
Track time spent on your issues:

Check hours spent on issues due **today** or **this week**  

## Token
First, you need to create a personal access token on gitlab:
* Go to https://gitlab.scicrop.com/profile/personal_access_tokens
* Fill name
* Check scopes: **api** and **read_user**
* Create and copy! (you won't be able to access it again)
* Create a .env file inside this project and add the following:
```
AUTH_TOKEN = <YOUR_PERSONAL_TOKEN>
```


## Usage
Now you're good to go! 

Just run the following command inside this project to track your time spent:
```
  python main.py <username> [--today] [--week]
```

* username: your gitlab user
* --today (optional): track time spent today
* --week (optional): track time spent this week


