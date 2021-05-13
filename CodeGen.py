from termcolor import colored
import os, random, time, keyboard
from math import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def generator():
    cls()
    code = ""
    chars = "ABCDEFGHIJKLNMOPQRSTUVWXYZ1234567890"
    nums = "1234567890"

    part1 = ""
    part2 = ""
    part3 = ""
    part4 = ""
    part5 = ""
    part6 = ""
    part7 = ""
    part8 = ""


    count = 0
    print(colored(" / $$      /$$ /$$      /$$ /$$   /$$       /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$", "cyan"))
    print(colored(" | $$$    /$$$| $$$    /$$$| $$  / $$      | $$_____/| $$$ | $$ /$$__  $$|_  $$_/| $$$ | $$| $$_____/", "cyan"))
    print(colored(" | $$$$  /$$$$| $$$$  /$$$$|  $$/ $$/      | $$      | $$$$| $$| $$  \__/  | $$  | $$$$| $$| $$", "cyan"))      
    print(colored(" | $$ $$/$$ $$| $$ $$/$$ $$ \  $$$$/       | $$$$$   | $$ $$ $$| $$ /$$$$  | $$  | $$ $$ $$| $$$$$", "cyan"))   
    print(colored(" | $$  $$$| $$| $$  $$$| $$  >$$  $$       | $$__/   | $$  $$$$| $$|_  $$  | $$  | $$  $$$$| $$__/", "cyan"))   
    print(colored(" | $$\  $ | $$| $$\  $ | $$ /$$/\  $$      | $$      | $$\  $$$| $$  \ $$  | $$  | $$\  $$$| $$", "cyan"))      
    print(colored(" | $$ \/  | $$| $$ \/  | $$| $$  \ $$      | $$$$$$$$| $$ \  $$|  $$$$$$/ /$$$$$$| $$ \  $$| $$$$$$$$", "cyan"))
    print(colored(" |__/     |__/|__/     |__/|__/  |__/      |________/|__/  \__/ \______/ |______/|__/  \__/|________/", "cyan"))
    print("\n")
    print(colored(" [*] ", "green") + "WHAT KIND OF CODES DO YOU WANT TO GENERATE?")
    print(colored(" [*] ", "green") + "PRESS 'N' TO STOP THE GENERATION PROCESS!")
    print("\n")
    print(colored(" [1] ", "green") + " PSN BALANCE")
    print(colored(" [2] ", "green") + " PS PLUS")
    print(colored(" [3] ", "green") + " XBOX LIFE")
    print(colored(" [4] ", "green") + " XBOX BALANCE")
    print(colored(" [5] ", "green") + " NINTENDO ESHOP")
    print(colored(" [6] ", "green") + " NINTENDO ONLINE")
    print(colored(" [7] ", "green") + " ITUNES BALANCE")
    print(colored(" [8] ", "green") + " GOOGLE PLAY")
    print(colored(" [9] ", "green") + " AMAZON BALANCE")
    print(colored(" [10]", "green") + " NEFLIX GIFT")
    print(colored(" [11]", "green") + " STEAM GAMES")
    print(colored(" [12]", "green") + " STEAM WALLET CODES")
    print(colored(" [13]", "green") + " WINDOWS PRO KEYS")
    print(colored(" [14]", "green") + " ROBLOX GIFT CARDS")
    print(colored(" [15]", "green") + " PAYSAFECARD")
    print(colored(" [16] RESTART", "green"))
    print(colored(" [17] EXIT", "red"))
    print("\n")

    greendot = colored("[*]", "green")
    selection = int(input(" " + greendot + "  SELECTION: "))


    match selection:
        case 1: # PSN
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
        case 2: # PSN
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
        case 3: # XBOX
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(5):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}-{part4}-{part5}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
                part5 = ""
        case 4: # XBOX
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(5):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}-{part4}-{part5}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
                part5 = ""
        case 5: # NINTENDO
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                print(colored(f'{part1} {part2} {part3} {part4}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
        case 6: # NINTENDO
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            nin = "ACDEFGHJKLNMPQRSTUVWXY1234567890"
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(nin)
                    part2 = part2 + random.choice(nin)
                    part3 = part3 + random.choice(nin)
                    part4 = part4 + random.choice(nin)
                print(colored(f'{part1} {part2} {part3} {part4}, "green'))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
        case 7: # APPLE
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                part1 = "X"
                for i in range(4):
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                for i in range(3):
                    part1 = part1 + random.choice(chars)
                print(colored(f'{part1}{part2}{part3}{part4}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
        case 8: # GOOGLE PLAY
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1} {part2} {part3} {part4} {part5}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
                part5 = ""
        case 9: # AMAZON
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(chars)
                for i in range(6):
                    part2 = part2 + random.choice(chars)
                for i in range(5):
                    part3 = part3 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
        case 10: # Neflix
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(11):
                    part1 = part1 + random.choice(chars)
                print(colored(f'{part1}', "green"))
                count = count + 1
                part1 = ""
        case 11: # Steam
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(5):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}-{part4}-{part5}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
                part5 = ""
        case 12: # Steam
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(5):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
        case 13: # WINDOWS
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(5):
                    part1 = part1 + random.choice(chars)
                    part2 = part2 + random.choice(chars)
                    part3 = part3 + random.choice(chars)
                    part4 = part4 + random.choice(chars)
                    part5 = part5 + random.choice(chars)
                print(colored(f'{part1}-{part2}-{part3}-{part4}-{part5}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
                part5 = ""
        case 14: # ROBLOX
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(3):
                    part1 = part1 + random.choice(nums)
                    part2 = part2 + random.choice(nums)
                for i in range(4):
                    part3 = part3 + random.choice(nums)
                print(colored(f'{part1} {part2} {part3}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
        case 15: # PSC
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(4):
                    part1 = part1 + random.choice(nums)
                    part2 = part2 + random.choice(nums)
                    part3 = part3 + random.choice(nums)
                    part4 = part4 + random.choice(nums)
                print(colored(f'{part1} {part2} {part3} {part4}', "green"))
                count = count + 1
                part1 = ""
                part2 = ""
                part3 = ""
                part4 = ""
        case 16:
            generator()
        case 16:
            exit()
    selexit = input('\n' + colored(" [Y/N]", "green") + " DO YOU WANT TO GENERATE MORE?: ")
    match selexit:
        case "Y":
            cls()
            generator()
        case "y":
            cls()
            generator()
        case "n":
            exit()
        case "N":
            exit()
generator()
