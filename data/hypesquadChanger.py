import time
import requests
from colorama import Fore



def hypeSquadChanger():
    hypetoken = input(f"Token: {Fore.RESET}")
    print(f"{rr}[{w}1{rr}]{w} Bravery\n{rr}[{w}2{rr}]{w} Briliance\n{rr}[{w}3{rr}]{w} Balance\n")
    hypesquad = input(f"{rr} Choice: {Fore.RESET}")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)