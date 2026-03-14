import requests
import os
import json
import time
import base64
import sys
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

AUTH_SERVER = base64.b64decode(
"aHR0cHM6Ly90YWJiby1hdXRoLnZlcmNlbC5hcHAvYXBpL2F1dGg="
).decode()

HISTORY_FILE = "history.json"
LIMIT_FILE = "limit.json"

DAILY_LIMIT = 15


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner(user, remaining):

    clear()

    print(Fore.RED + r"""

████████╗ █████╗ ██████╗ ██████╗  ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
   ██║   ███████║██████╔╝██████╔╝██║   ██║
   ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║
   ██║   ██║  ██║██████╔╝██████╔╝╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝

        🔎 TABBO NUMBER INFO TOOL 🔎

""")

    print(Fore.CYAN + "┌─────────────────────────────┐")
    print(Fore.CYAN + "          USER INFO")
    print(Fore.CYAN + "└─────────────────────────────┘")

    print(Fore.GREEN + f"👤 User Name : {user}")
    print(Fore.YELLOW + f"⭐ Credits   : {remaining}\n")

    print(Fore.GREEN + "⭐ Credit By TABBO\n")


def load_json(file, default):
    try:
        with open(file) as f:
            return json.load(f)
    except:
        return default


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


def check_limit(user):

    data = load_json(LIMIT_FILE, {})
    today = datetime.now().strftime("%Y-%m-%d")

    if user not in data:
        data[user] = {"count": 0, "date": today}

    if data[user]["date"] != today:
        data[user]["count"] = 0
        data[user]["date"] = today

    save_json(LIMIT_FILE, data)

    return data


def login():

    clear()

    print(Fore.CYAN + """
╔════════════════════════════════╗
            🔐 LOGIN
╚════════════════════════════════╝
Telegram : @tabbo73
""")

    password = input("Password : ")

    try:
        r = requests.get(AUTH_SERVER, params={"pass": password}).json()

        if r.get("status") != "ok":
            print(Fore.RED + "❌ Invalid Password")
            sys.exit()

    except:
        print(Fore.RED + "Server Error")
        sys.exit()


def show_results(data, number):

    print(Fore.MAGENTA + f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 RESULTS FOR : {number}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    if not isinstance(data, dict) or len(data) == 0:
        print(Fore.RED + "\n❌ DATA NOT FOUND\n")
        return

    for i, key in enumerate(data, 1):

        r = data[key]

        print(Fore.BLUE + "╔══════════════════════════════╗")
        print(Fore.BLUE + f"         RECORD {i}")
        print(Fore.BLUE + "╚══════════════════════════════╝")

        if r.get("name"):
            print(Fore.YELLOW + "👤 Name : " + Fore.CYAN + r["name"])

        if r.get("fname"):
            print(Fore.YELLOW + "👨 Father : " + Fore.CYAN + r["fname"])

        if r.get("address"):
            print(Fore.GREEN + "\n🏠 ADDRESS DETAILS")

            addr = r["address"].split("!")

            labels = [
                "Relation",
                "Village",
                "City",
                "District",
                "State",
                "Pincode"
            ]

            for i, part in enumerate(addr):

                part = part.strip()

                if part and i < len(labels):

                    print(
                        Fore.YELLOW + "   " + labels[i] +
                        Fore.MAGENTA + " : " +
                        Fore.CYAN + part
                    )

        if r.get("circle"):
            print(Fore.GREEN + "\n📡 Circle : " + Fore.CYAN + r["circle"])

        if r.get("alt"):
            print(Fore.YELLOW + "📞 Alternate : " + Fore.CYAN + r["alt"])

        if r.get("id"):
            print(Fore.MAGENTA + "🆔 ID : " + Fore.CYAN + r["id"])

        print(Fore.RED + """
────────────────────────────────────
📩 Telegram : @tabbo73
⭐ Credit By TABBO
────────────────────────────────────
""")


def search(user):

    data = check_limit(user)

    if data[user]["count"] >= DAILY_LIMIT:

        print(Fore.RED + "\n❌ Daily limit finished (15 searches)\n")
        input("Press Enter...")
        return

    number = input("📱 Enter Mobile Number : ")

    print("🔎 Searching...\n")
    time.sleep(1)

    try:

        day = datetime.now().day
        key = "tabbo786" + str(day)

        url = hidden_api() + number + "&k=" + key

        r = requests.get(url)
        result = r.json()

        show_results(result, number)

        history = load_json(HISTORY_FILE, [])
        history.append(number)
        save_json(HISTORY_FILE, history)

    except:
        pass

    data[user]["count"] += 1
    save_json(LIMIT_FILE, data)

    remaining = DAILY_LIMIT - data[user]["count"]

    print(Fore.YELLOW + f"\n🔎 Remaining Searches : {remaining}")

    input("Press Enter...")


def history():

    data = load_json(HISTORY_FILE, [])

    print(Fore.CYAN + "\n📜 SEARCH HISTORY\n")

    if len(data) == 0:
        print("No history")

    for i, n in enumerate(data, 1):
        print(Fore.YELLOW + f"{i}. {n}")

    input("\nPress Enter...")


def clear_history():

    save_json(HISTORY_FILE, [])
    print("History cleared")
    input()


def menu(user):

    while True:

        data = check_limit(user)
        remaining = DAILY_LIMIT - data[user]["count"]

        banner(user, remaining)

        print(Fore.GREEN + "1️⃣  Search Number")
        print(Fore.CYAN + "2️⃣  History")
        print(Fore.MAGENTA + "3️⃣  Clear History")
        print(Fore.RED + "4️⃣  Exit\n")

        op = input("Select Option : ")

        if op == "1":
            search(user)

        elif op == "2":
            history()

        elif op == "3":
            clear_history()

        elif op == "4":
            sys.exit()


# hidden proxy api

def hidden_api():

    p1="aHR0cHM6Ly90YW"
    p2="Jiby1wcm94eS52"
    p3="ZXJjZWwuYXBwL2"
    p4="FwaS9zZWFyY2g/"
    p5="bW9iaWxlPQ=="

    return base64.b64decode(p1+p2+p3+p4+p5).decode()


login()

username = os.getlogin()

menu(username)
