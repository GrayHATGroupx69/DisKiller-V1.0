import time
import requests
from data.common import *

def getAllAdminServers(token):
    set_console_title("DisKiller  | Get Servers of Administrator")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    admin_guilds = []
    r_guilds = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=headers)
    guilds = r_guilds.json()
    for guild in guilds:
        if guild['owner']:  # Check if user is the owner of the guild
            print(f"{rr}[ {w}G {rr}]{w} {guild['name']} (Owner)")
        elif (guild_id := guild['id']) in admin_guilds:  # Check if user is an admin of the guild
            print(f"{rr}[ {w}G {rr}]{w} {guild['name']} (Administrator)")
        # else:
            # print(f"{rr}[ {w}G {rr}]{w} {guild['name']} (Member)")
    input("Press any key to continue...")