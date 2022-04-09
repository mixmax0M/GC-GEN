from termcolor import colored
import os, random, time, keyboard, requests
import subprocess as sp
from bs4 import BeautifulSoup
from math import *

# https://discord.com/api/v9/entitlements/gift-codes/*code here*?with_application=true&with_subscription_plan=true
# 60s ip ban


f = open("codes.txt", "a")
f = open("proxies.txt", "a")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def getProxies(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='HTTP' or 'HTTPS':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies


def generator():
    cwd = os.getcwd()
    cls()
    code = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    hits = 0
    miss = 0
    error = 0
    timeout = 0
    checkyy = 0
    used = 0

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
    print(colored(" [*] ", "green") + "PRESS 'S' TO STOP THE CHECK PROCESS!")
    print(colored(" [*] ", "green") + "PRESS 'N' TO STOP THE CODE GENERATION!")
    print("\n")
    print(colored(" [1] ", "green") + " GENERATE GIFTS")
    print(colored(" [2] ", "green") + " CHECK GIFTS")
    print(colored(" [3] ", "green") + " EDIT PROXIES")
    print(colored(" [4] ", "green") + " DELET PREVIOUSLY GENERATED GIFTS")
    print(colored(" [5]  RESTART", "green"))
    print(colored(" [6]  EXIT", "red"))
    print("\n")

    greendot = colored("[*]", "green")
    selection = int(input(" " + greendot + "  SELECTION: "))

    match selection:
        case 1:
            ammount = int(input('\n ' + greendot + ' HOW MANY CODES DO YOU WANT TO GENERATE?: '))
            while count != ammount:
                try:
                    if keyboard.is_pressed('n'):
                        break
                except:
                    break
                for i in range(24):
                    f = open("codes.txt", "a")
                    code = code + random.choice(chars)
                print(colored(f'{code}', "green"))
                f = open("codes.txt", "a")
                f.write(f'{code}\n')
                f.close
                count = count + 1
                code = ""
        case 2:
            checkyy = 1
            cls()
            proxy = input(colored(" [Y/N]", "green") + " DO YOU WANT TO USE PROXIES?: ")
            match proxy:
                case "n":
                    f = open("codes.txt", "r")
                    lines = f.readlines()
                    count = 0
                    selection = 1

                    for line in lines:
                        try:
                            if keyboard.is_pressed('s'):
                                break
                        except:
                            break
                        count += 1
                        rqURL = f"https://discord.com/api/v9/entitlements/gift-codes/{line.strip()}"
                        r = requests.get(url=rqURL)
                        msg = r.json()
                        try:
                            if msg["code"] == 10038:
                                print(colored(line.strip(), "red"))
                                miss = miss + 1
                            elif msg["code"] == line.strip() and msg["redeemed"] == False:
                                print(colored(line.strip(), "green"))
                                f = open("hits.txt", "a")
                                f.write(f'https://discord.com/gifts/{line.strip()}\n')
                                f.close
                                hits = hits + 1
                            elif msg["code"] == line.strip() and msg["redeemed"] == True:
                                print(colored(line.strip(), "yellow"))
                                f.close
                                used = used + 1
                            else:
                                print(colored("UNKNOWN ERROR", "red"))
                                error = error + 1
                        except:
                            print("»" + colored("Timeout: ", "red") + str(msg["retry_after"]))
                            timeout = timeout + 1
                case "N":
                    f = open("codes.txt", "r")
                    lines = f.readlines()
                    count = 0
                    selection = 1
                    for line in lines:
                        try:
                            if keyboard.is_pressed('s'):
                                break
                        except:
                            break
                        count += 1
                        rqURL = f"https://discord.com/api/v9/entitlements/gift-codes/{line.strip()}"
                        r = requests.get(url=rqURL)
                        msg = r.json()
                        try:
                            if msg["code"] == 10038:
                                print(colored(line.strip(), "red"))
                                miss = miss + 1
                            elif msg["code"] == line.strip() and msg["redeemed"] == False:
                                print(colored(line.strip(), "green"))
                                f = open("hits.txt", "a")
                                f.write(f'https://discord.com/gifts/{line.strip()}\n')
                                f.close
                                hits = hits + 1
                            elif msg["code"] == line.strip() and msg["redeemed"] == True:
                                print(colored(line.strip(), "yellow"))
                                f.close
                                used = used + 1
                            else:
                                print(colored("UNKNOWN ERROR", "red"))
                                error = error + 1
                        except:
                            print("»" + colored("Timeout: ", "red") + str(msg["retry_after"]))
                            timeout = timeout + 1
                case "y":
                    while proxy == "y" or "Y":
                        
                        try:
                            if keyboard.is_pressed('s'):
                                break
                        except:
                            break
                        f = open("codes.txt", "r")
                        pr = open("proxies.txt", "r")
                        lines = f.readlines()
                        proxyfg = ""
                        print(colored(" [1] ", "green") + " API")
                        print(colored(" [2] ", "green") + " FILE")
                        print("\n")
                        prxsell = int(input(greendot + " SELECTION: "))
                        match prxsell:
                            case 1:
                                smol_list = ["https://free-proxy-list.net/", "https://www.netzwelt.de/proxy/index.html/"]
                                for ads in smol_list:
                                    dalist = getProxies(ads)
                                    for element in dalist:
                                        proxyfg = proxyfg + "\n" + element
                            case 2:
                                proxyfg = pr.readlines()
                        count = 0
                        selection = 1
                        tmot = int(input(" " + greendot + " TIMEOUT IN S: "))
                        print(" " + greendot + " STARTING IN 3 SEC")
                        cls()
                        time.sleep(3)
                        for lin in proxyfg:
                            for line in lines:
                                try:
                                    if keyboard.is_pressed('s'):
                                        break
                                except:
                                    break
                                try:
                                    count += 1
                                    rqURL = f"https://discord.com/api/v9/entitlements/gift-codes/{line.strip()}"
                                    r = requests.get(url=rqURL, proxies={'http': f"http://{lin}", 'https': f"http://{lin}"}, timeout=tmot)
                                    msg = r.json()
                                    try:
                                        if msg["code"] == 10038:
                                            print(colored(line.strip(), "red"))
                                            miss = miss + 1
                                        elif msg["code"] == line.strip() and msg["redeemed"] == False:
                                            print(colored(line.strip(), "green"))
                                            f = open("hits.txt", "a")
                                            f.write(f'https://discord.com/gifts/{line.strip()}\n')
                                            f.close
                                            hits = hits + 1
                                        elif msg["code"] == line.strip() and msg["redeemed"] == True:
                                            print(colored(line.strip(), "yellow"))
                                            f.close
                                            used = used + 1
                                        else:
                                            print(colored("UNKNOWN ERROR", "red"))
                                            error = error + 1
                                    except:
                                        print("»" + colored("Timeout: ", "red") + str(msg["retry_after"]))
                                        timeout = timeout + 1
                                except:
                                    pass
                case "Y":
                    while proxy == "y" or "Y":
                        
                        try:
                            if keyboard.is_pressed('s'):
                                break
                        except:
                            break
                        f = open("codes.txt", "r")
                        pr = open("proxies.txt", "r")
                        lines = f.readlines()
                        proxyfg = ""
                        print(colored(" [1] ", "green") + " API")
                        print(colored(" [2] ", "green") + " FILE")
                        print("\n")
                        prxsell = int(input(greendot + " SELECTION: "))
                        match prxsell:
                            case 1:
                                dalist = getProxies("https://free-proxy-list.net/")
                                for element in dalist:
                                    proxyfg = proxyfg + "\n" + element
                            case 2:
                                proxyfg = pr.readlines()
                        count = 0
                        selection = 1
                        tmot = int(input(" " + greendot + " TIMEOUT IN S: "))
                        print(" " + greendot + " STARTING IN 3 SEC")
                        cls()
                        time.sleep(3)
                        for lin in proxyfg:
                            for line in lines:
                                try:
                                    if keyboard.is_pressed('s'):
                                        break
                                except:
                                    break
                                try:
                                    count += 1
                                    rqURL = f"https://discord.com/api/v9/entitlements/gift-codes/{line.strip()}"
                                    r = requests.get(url=rqURL, proxies={'http': f"http://{lin}", 'https': f"http://{lin}"}, timeout=tmot)
                                    msg = r.json()
                                    try:
                                        if msg["code"] == 10038:
                                            print(colored(line.strip(), "red"))
                                            miss = miss + 1
                                        elif msg["code"] == line.strip() and msg["redeemed"] == False:
                                            print(colored(line.strip(), "green"))
                                            f = open("hits.txt", "a")
                                            f.write(f'https://discord.com/gifts/{line.strip()}\n')
                                            f.close
                                            hits = hits + 1
                                        elif msg["code"] == line.strip() and msg["redeemed"] == True:
                                            print(colored(line.strip(), "yellow"))
                                            f.close
                                            used = used + 1
                                        else:
                                            print(colored("UNKNOWN ERROR", "red"))
                                            error = error + 1
                                    except:
                                        print("»" + colored("Timeout: ", "red") + str(msg["retry_after"]))
                                        timeout = timeout + 1
                                except:
                                    pass
        case 3:
            open("proxies.txt", "a")
            programName = "notepad.exe"
            fileName = "proxies.txt"
            sp.Popen([programName, fileName])
            generator()
        case 4:
            open('codes.txt', 'w').close()
            generator()
        case 5:
            generator()
        case 6:
            exit()
    if checkyy == 1:
        print("\n")
        print("───────────────")
        print("│" + colored(" Hits:      ", "green") + str(hits) + "│")
        print("│" + colored(" Used:      ", "cyan") + str(used) + "│")
        print("│" + colored(" Fails:     ", "red") + str(miss) + "│")
        print("│" + colored(" Timeouts:  ", "yellow") + str(timeout) + "│")
        print("│" + colored(" Errors:    ", "magenta") + str(error) + "│")
        print("───────────────")
        print("\n")

    if selection == 1:
        selexit = input('\n' + colored(" [Y/N]", "green") + " RETURN TO MENU?: ")
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
