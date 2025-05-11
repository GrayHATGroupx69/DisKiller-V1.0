import requests
from data.common import *

def close_all_dms(token):
    set_console_title("DisKiller  | Close DMs")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        print(f"{rr}[ {w}+{rr} ] {w}ID:{rr} "+channel['id'] + Fore.RESET)
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,)