from colorama import init
from colorama import Fore, Back, Style
from os import system
from time import sleep
from random import randint
from rquests import post, get
init()

with open("1.txt", "r+") as f:
    art_1 = f.read()
    f.close()

for i in range(20):
    system("clear")
    print(Fore.GREEN + art_1)
    sleep(0.1)
    system("clear")
    print(Fore.WHITE + art_1)
    sleep(0.1)

noqte=""
website= input(Fore.RED+"website: ")
for i in range(100):
    system("clear")
    print(Fore.BLUE+art_1)
    noqte+="*"
    print(Fore.GREEN+ noqte)
    sleep(0.5)
