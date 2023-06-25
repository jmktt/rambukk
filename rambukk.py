from pystyle import *
import argparse

class bcolors:
    YELLOW = '\033[1;33m'
    RESET = '\033[0;0m'
tname = Colorate.Horizontal(Colors.yellow_to_red, "BRUTE FORCE TOOL",1)
cname = Colorate.Horizontal(Colors.red_to_blue, "JMKTT",2)
version= Colorate.Horizontal(Colors.red_to_blue, "1.0",2)
banner = """

\t ██▀███   ▄▄▄       ███▄ ▄███▓ ▄▄▄▄    █    ██  ██ ▄█▀ ██ ▄█▀
\t▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒▓█████▄  ██  ▓██▒ ██▄█▒  ██▄█▒ 
\t▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░▒██▒ ▄██▓██  ▒██░▓███▄░ ▓███▄░ 
\t▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ ▒██░█▀  ▓▓█  ░██░▓██ █▄ ▓██ █▄ 
\t░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒░▓█  ▀█▓▒▒█████▓ ▒██▒ █▄▒██▒ █▄
\t░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒▒ ▒▒ ▓▒
\t  ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░▒░▒   ░ ░░▒░ ░ ░ ░ ░▒ ▒░░ ░▒ ▒░
\t  ░░   ░   ░   ▒   ░      ░    ░    ░  ░░░ ░ ░ ░ ░░ ░ ░ ░░ ░ 
\t   ░           ░  ░       ░    ░         ░     ░  ░   ░  ░   
\t                                    ░                             
"""
print(banner)
print("\t\t\033[1;34m[---]    RAMBUKK ({}\033[1;34m).      [---]".format(tname)+bcolors.RESET)
print("\t\t\033[1;34m[---]          Created by: {}\033[1;34m          [---]".format(cname)+bcolors.RESET)
print("\t\t\033[1;34m[---]            Version: \033[1;31m {} \033[0;0m \033[1;34m          [---] \n".format(version))
print(Colors.green,"\t\t\t      Welcome to RAMBUKK.\n"+bcolors.RESET)
