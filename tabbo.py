import requests
import os
import json
import time
import getpass
from colorama import Fore, init

init(autoreset=True)

AUTH_SERVER = "https://tabbo-auth.vercel.app/api/auth"
LOOKUP_API = "https://tabbo-proxy.vercel.app/api/search?mobile="

USERS_FILE = "users.json"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_users():
    try:
        with open(USERS_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_users(data):
    with open(USERS_FILE,"w") as f:
        json.dump(data,f,indent=2)


def banner(user,credits):

    clear()

    print(Fore.RED + """
╔══════════════════════════════════════════════════════╗
║                                                      ║
║        ████████╗ █████╗ ██████╗ ██████╗  ██████╗      ║
║        ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗     ║
║           ██║   ███████║██████╔╝██████╔╝██║   ██║     ║
║           ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║     ║
║           ██║   ██║  ██║██████╔╝██████╔╝╚██████╔╝     ║
║           ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝      ║
║                                                      ║
║              🔎 TABBO NUMBER INFO TOOL 🔎           ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")

    print(Fore.CYAN + "╔══════════════ USER INFO ══════════════╗")

    print(Fore.YELLOW + f"   👤 User Name : {user}")
    print(Fore.YELLOW + f"   💳 Credits   : {credits}")

    print(Fore.CYAN + "╚═══════════════════════════════════════╝\n")

    print(Fore.GREEN + "⭐ Credit By TABBO\n")


def login():

    clear()

    print(Fore.CYAN + """
╔════════════════════════════════════╗
            🔐 TOOL LOGIN
╚════════════════════════════════════╝

📩 Generate password contact admin
Telegram : @tabbo73
""")

    password = getpass.getpass("🔑 Enter Password : ")

    try:

        r = requests.get(AUTH_SERVER, params={"pass": password}).json()

        if r.get("status") != "ok":

            print("❌ Invalid password")
            exit()

    except:

        exit()


def show_results(data, number):

    print(Fore.MAGENTA + f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 RESULTS FOR : {number}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    if not isinstance(data, dict):
        return

    for i, key in enumerate(data,1):

        r = data[key]

        print(Fore.CYAN + "╔══════════════════════════════╗")
        print(Fore.CYAN + f"         RECORD {i}")
        print(Fore.CYAN + "╚══════════════════════════════╝")

        if r.get("name") or r.get("fname"):

            print(Fore.YELLOW + "\n👤 PERSONAL INFORMATION")

            if r.get("name"):
                print("   Name   :", r["name"])

            if r.get("fname"):
                print("   Father :", r["fname"])

        if r.get("address"):

            print(Fore.YELLOW + "\n🏠 ADDRESS DETAILS")
            print("   Location :", r["address"])

        if r.get("circle") or r.get("id"):

            print(Fore.YELLOW + "\n📡 NETWORK INFO")

            if r.get("circle"):
                print("   Circle :", r["circle"])

            if r.get("id"):
                print("   ID :", r["id"])

        print(Fore.RED + """
────────────────────────────────────
📩 Telegram : @tabbo73
🛑 Credit By TABBO
────────────────────────────────────
""")


def search(user,users):

    if users[user] <= 0:

        print("❌ No credits left")
        input()
        return

    number = input("📱 Enter Mobile Number : ")

    print("\n🔎 Searching...\n")

    time.sleep(1)

    try:

        r = requests.get(LOOKUP_API + number)

        data = r.json()

        show_results(data, number)

    except:
        pass

    users[user] -= 1
    save_users(users)

    input("Press Enter...")


def menu(user,users):

    while True:

        banner(user,users[user])

        print("""
1️⃣  Single Lookup
2️⃣  Exit
""")

        op = input("Select : ")

        if op == "1":
            search(user,users)

        elif op == "2":
            exit()


login()

users = load_users()

username = os.getlogin()

if username not in users:
    users[username] = 5

save_users(users)

menu(username,users)
