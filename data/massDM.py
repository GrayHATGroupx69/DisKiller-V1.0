import requests
from data.common import *

def massDM(token, content):
    set_console_title("DisKiller | Mass DM")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{content}"})
            print(f"{rr}[ {w}+ {rr}]{w} ID:{rr} "+channel['id'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
