import requests
import os
from dotenv import load_dotenv

BASE_URL = "https://api.github.com"

def no_auth_api():
    response = requests.get("{}".format(BASE_URL))
    if response.ok:
        print(response.status_code)
        print(response.json().get("current_user_url"))
    else:
        print(response.status_code)
        print("Oh no!")

def auth_api():
    headers = {
        "Authorization": "token {}".format(os.getenv("ACCESS_TOKEN"))
    }

    response = requests.get("{}/user".format(BASE_URL), headers=headers)
    if response.ok:
        print(response.status_code)
        print(response.json().get("login"))
    else:
        print(response.status_code)
        print("Oh no!")

if __name__=="__main__":
    # Load environment variables from .env
    load_dotenv()
    no_auth_api()
    auth_api()