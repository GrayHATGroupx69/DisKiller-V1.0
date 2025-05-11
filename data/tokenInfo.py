import requests
from data.common import *

def tokenInfo(token):
    set_console_title("DisKiller | Token Info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f"""
{rr}[{w}User ID{rr}]         {w}{userID}
{rr}[{w}User Name{rr}]       {w}{userName}
{rr}[{w}2 Factor{rr}]        {w}{mfa}
{rr}[{w}Email{rr}]           {w}{email}
{rr}[{w}Phone number{rr}]    {w}{phone if phone else "None"}
{rr}[{w}Token{rr}]           {w}{token}
            """)
            input('Press any key to continue...')
