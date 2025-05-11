import requests
from data.common import *

def createServers(token, count, name):
    set_console_title("DisKiller  | Create Servers")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(int(count)):
        print(f"{rr}[ {w}{str(i+1)} {rr}] {w}Created Server")
        json = { 'name': name }
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=json, timeout=999)
    time.sleep(2)