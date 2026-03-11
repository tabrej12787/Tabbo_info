import requests
import sys
import os
import json
import time
from colorama import Fore, Style, init

init(autoreset=True)

AUTH_SERVER = "https://tabbo-auth.vercel.app/api/auth"
LOOKUP_API = "https://tabbo-proxy.vercel.app/api/search?mobile="

USER_FILE = "users.json"
HISTORY_FILE = "history.json"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner(user="Guest", credits=0):

    clear()

    print(Fore.MAGENTA + """

████████╗ █████╗ ██████╗ ██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
   ██║   ███████║██████╔╝██████╔╝
   ██║   ██╔══██║██╔══██╗██╔══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝

""")

    print(Fore.CYAN + "╔══════════════════════════════╗")
    print(Fore.CYAN + "        ⚡ TABBO OSINT TOOL ⚡")
    print(Fore.CYAN + "╚══════════════════════════════╝\n")

    print(Fore.YELLOW + "📡 Mobile Intelligence Lookup Engine\n")

    print(Fore.GREEN + f"👤 User    : {user}")
    print(Fore.GREEN + f"💳 Credits : {credits}\n")


def verify_password():

    print(Fore.YELLOW + """
╔══════════════════════════════╗
🔒 ACCESS REQUIRED
Generate password contact admin
Telegram : @tabbo73
╚══════════════════════════════╝
""")

    password = input("🔑 Enter Tool Password : ")

    try:

        r = requests.get(
            AUTH_SERVER,
            params={"pass": password},
            timeout=10
        ).json()

        if r.get("status") != "ok":

            print(Fore.RED + "\n❌ Invalid password\n")

            sys.exit()

        print(Fore.GREEN + "\n✅ Access granted\n")

        time.sleep(1)

    except:

        print(Fore.RED + "\n❌ Server connection failed\n")

        sys.exit()


def load_users():

    try:

        with open(USER_FILE) as f:

            return json.load(f)

    except:

        return {}


def save_users(data):

    with open(USER_FILE, "w") as f:

        json.dump(data, f, indent=2)


def load_history():

    try:

        with open(HISTORY_FILE) as f:

            return json.load(f)

    except:

        return []


def save_history(data):

    with open(HISTORY_FILE, "w") as f:

        json.dump(data, f, indent=2)


def show_results(data, number):

    print(Fore.YELLOW + f"\n📊 RESULTS FOR : {number}\n")

    if not isinstance(data, dict):

        print(data)

        return

    print(Fore.GREEN + f"Found {len(data)} record(s)\n")

    for i, key in enumerate(data,1):

        r = data[key]

        print(Fore.CYAN + "╔══════════════════════════════╗")
        print(Fore.CYAN + f"        📂 RECORD {i}")
        print(Fore.CYAN + "╚══════════════════════════════╝")

        print(Fore.GREEN + f"👤 Name     : {r.get('name','N/A')}")
        print(Fore.GREEN + f"👨 Father   : {r.get('fname','N/A')}")
        print(Fore.GREEN + f"🏠 Address  : {r.get('address','N/A')}")
        print(Fore.GREEN + f"📡 Circle   : {r.get('circle','N/A')}")
        print(Fore.GREEN + f"🆔 ID       : {r.get('id','N/A')}")

        print(Fore.MAGENTA + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


def lookup(user, users):

    if users[user] <= 0:

        print(Fore.RED + "\n❌ No credits left\n")

        input("Press enter...")

        return

    number = input(Fore.YELLOW + "\n📱 Enter mobile number : ")

    print(Fore.CYAN + "\n🔎 Searching database...\n")

    time.sleep(1)

    try:

        r = requests.get(LOOKUP_API + number, timeout=15)

        data = r.json()

        show_results(data, number)

        history = load_history()

        history.append(number)

        save_history(history)

        users[user] -= 1

        save_users(users)

        print(Fore.YELLOW + f"\n💳 Credits left : {users[user]}\n")

    except:

        print(Fore.RED + "❌ API Error")

    input(Fore.CYAN + "Press ENTER to continue...")


def history():

    data = load_history()

    if not data:

        print("No history found")

    else:

        print("\n📜 SEARCH HISTORY\n")

        for i,n in enumerate(data,1):

            print(f"{i} - {n}")

    input("\nPress enter...")


def menu(user, users):

    while True:

        banner(user, users[user])

        print(Fore.GREEN + """

1️⃣  Single Lookup
2️⃣  Search History
3️⃣  Exit Tool

""")

        op = input(Fore.YELLOW + "Select option : ")

        if op == "1":

            lookup(user, users)

        elif op == "2":

            history()

        elif op == "3":

            print(Fore.RED + "\nTool Closed 👋\n")

            sys.exit()

        else:

            print("Invalid option")

            time.sleep(1)


def main():

    verify_password()

    users = load_users()

    user = input(Fore.YELLOW + "👤 Enter username : ")

    if user not in users:

        users[user] = 5

    save_users(users)

    menu(user, users)


if __name__ == "__main__":

    main()e','N/A')}")
            print(Fore.GREEN + f"🆔 ID       : {r.get('id','N/A')}")

            print(Fore.MAGENTA + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    else:

        print(data)


def search():

    users = load_users()

    user = input(Fore.YELLOW + "👤 Username : ")

    if user not in users:
        users[user] = 5

    if users[user] <= 0:

        print(Fore.RED + "\n❌ No credits left\n")
        time.sleep(2)
        return

    number = input(Fore.YELLOW + "\n📱 Enter mobile number: ")

    loading()

    try:

        r = requests.get(LOOKUP_API + number)

        data = r.json()

        show_results(data)

    except:

        print(Fore.RED + "\n❌ API Error\n")

    users[user] -= 1

    save_users(users)

    print(Fore.YELLOW + f"\n💳 Credits left : {users[user]}\n")

    input(Fore.CYAN + "Press ENTER to return dashboard...")


def dashboard():

    while True:

        banner()

        print(Fore.GREEN + """

1️⃣  Search Number
2️⃣  Exit Tool

""")

        op = input(Fore.YELLOW + "Select option: ")

        if op == "1":

            search()

        elif op == "2":

            clear()

            print(Fore.RED + """

Tool Closed Successfully

Goodbye Hacker 👋
""")

            sys.exit()

        else:

            print("Invalid option")
            time.sleep(1)


def main():

    banner()

    verify_password()

    dashboard()


main()
