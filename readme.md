# Track my issues 
Track time spent on your issues:

Check hours spent on issues due **today** or **this week**  

## Usage
```
  python main.py <username> [--today] [--week]
```

* username: your gitlab user
* --today (optional): track time spent today
* --week (optional): track time spent this week


## Token
You need a personal access token:
* Create your personal access token on gitlab (https://gitlab.scicrop.com/profile/personal_access_tokens)
* Create a .env file inside this project and add the following:
```
AUTH_TOKEN = <YOUR_PERSONAL_TOKEN>
```