import os
import sys
import time
import ctypes
import random
import configparser
import requests
import subprocess
from time import sleep
from colorama import Fore, Style
rr = Fore.RED
c = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
w = Fore.WHITE
r = Style.RESET_ALL
# Define necessary WinAPI constants and functions
SetWindowLong = ctypes.windll.user32.SetWindowLongW
GetWindowLong = ctypes.windll.user32.GetWindowLongW
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
LWA_ALPHA = 0x2
conf = configparser.ConfigParser()
# ====================================================================================================================== #
def restart():
    os.execv(sys.argv[0], sys.argv)
def restartTokens():
    conf.read('config.ini')
def config2():
    subprocess.run(["notepad", "config.ini"], check=True)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def clear_banner():
    banner = f"""{rr}
                        ██████╗ ██╗███████╗██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
                        ██╔══██╗██║██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
                        ██║  ██║██║███████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
                        ██║  ██║██║╚════██║██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
                        ██████╔╝██║███████║██║  ██╗██║███████╗███████╗███████╗██║  ██║
                        ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
    """
    # faded_banner = fade.fire(banner)
    faded_banner = banner

    if os.name == "nt":
        os.system("cls")
        print(faded_banner)
        info = f"""\t\t\t\t\t  {rr}[+] {w}THIS TOOL BY GRAYHAT GROUP  {rr}[+]"""
        for x in info:
            time.sleep(0.0001)
            sys.stdout.write(x)
            sys.stdout.flush()
        print()
    else:
        os.system("clear")
        print(faded_banner)
        info = f"""\t\t\t\t\t  {rr}[+] {w}THIS TOOL BY GRAYHAT GROUP {rr}[+]"""
        for x in info:
            time.sleep(0.0001)
            sys.stdout.write(x)
            sys.stdout.flush()
        print()

# ====================================================================================================================== #

def set_window_transparency(hwnd, transparency):
    # Get current window style
    ex_style = GetWindowLong(hwnd, GWL_EXSTYLE)
    
    # Set window style to include WS_EX_LAYERED
    SetWindowLong(hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)
    
    # Set transparency level (0=transparent, 255=opaque)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, transparency, LWA_ALPHA)
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
set_window_transparency(hwnd, 200)
def increase_transparency_over_time(hwnd, max_transparency=255, min_transparency=180, step=10, interval=0.1):
    transparency = 180
    direction = 1  # 1 for increasing, -1 for decreasing

    while True:
        set_window_transparency(hwnd, transparency)

        transparency += direction * step
        if transparency >= max_transparency:
            transparency = max_transparency
            direction = -1  # Start decreasing transparency
        elif transparency <= min_transparency:
            transparency = min_transparency
            direction = 1  # Start increasing transparency

        time.sleep(interval)
def validateToken():
    while True:
        configur = configparser.ConfigParser()
        configur.read('config.ini')
        token = configur.get('SETTINGS', 'TOKEN', fallback=f"{Fore.RED}Err, No such Tokens.")
        sleep(1)
        base_url = "https://discord.com/api/v9/users/@me"
        message = "You need to verify your account in order to perform this action."
        r = requests.get(base_url, headers=getheaders(token))
        if r.status_code != 200:
            print(f'[ ! ] Invalid Token.')
            sleep(1)
            while True:
                choice = input(f"[ Enter A Vaild Token ] :> ")
                if len(choice) > 0 and choice != " ":
                    break
            configur.set('SETTINGS', 'TOKEN', choice)
            with open('config.ini', 'w') as config:
                configur.write(config)
            restartTokens()
            # config2()
            # validateToken(token)
            # __import__("spammer").main()
        j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(token)).json()
        try:
            if j["message"] == message:
                print(f"[ ! ] Phone Locked Token!")
                sleep(1)
        except:
            pass
            break
        

# ====================================================================================================================== #

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

# ====================================================================================================================== #

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

# ====================================================================================================================== #

def getDiscordCredits():
    s = requests.Session()
    
    url = "https://pastebin.com/raw/QTypeBEb"
    
    r = s.get(url)
    response = r.json()
    if r.ok:
        discordUser = (response['username'])
        return discordUser
    else:
        return "1161003805324886161"
# getDiscordCredits()

def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")
