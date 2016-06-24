import os
import requests


def avatar(user):
    response = requests.get(
        "https://api.github.com/users/{}".format(user), auth=(user, os.environ.get("PASS")))
    return response.json()['avatar_url']

if __name__ == "__main__":
    response = avatar("riquellopes")
    print(response)
