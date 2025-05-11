import requests
from data.common import *

def deleteWebhook(url):
    set_console_title("DisKiller  | Delete Webhook")
    requests.delete(url)
    print(f"{rr}[ {w}+{rr} ] {w}Deleted Webhook")
    sleep(1)