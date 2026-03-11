import requests
import sys
import os
import json
import time
import random
from colorama import init

init()

AUTH_SERVER = "https://tabbo-auth.vercel.app/api/auth"
LOOKUP_API = "https://tabbo-proxy.vercel.app/api/search?mobile="

USER_FILE = "users.json"
HISTORY_FILE = "history.json"
PROXY_FILE = "proxies.txt"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def load_proxies():
    try:
        with open(PROXY_FILE) as f:
            return [p.strip() for p in f if p.strip()]
    except:
        return []


def get_proxy():

    proxies = load_proxies()

    if not proxies:
        return None

    p = random.choice(proxies)

    return {
        "http": p,
        "https": p
    }


def banner(user, credits):

    clear()

    print("""
\033[95m████████╗\033[96m █████╗\033[92m ██████╗\033[93m ██████╗
\033[95m╚══██╔══╝\033[96m██╔══██╗\033[92m██╔══██╗\033[93m██╔══██╗
\033[95m   ██║   \033[96m███████║\033[92m██████╔╝\033[93m██████╔╝
\033[95m   ██║   \033[96m██╔══██║\033[92m██╔══██╗\033[93m██╔══██╗
\033[95m   ██║   \033[96m██║  ██║\033[92m██████╔╝\033[93m██████╔╝
\033[95m   ╚═╝   \033[96m╚═╝  ╚═╝\033[92m╚═════╝ \033[93m╚═════╝
""")

    print("\033[95m╔══════════════════════════════╗")
    print("\033[95m        ⚡ TABBO OSINT TOOL ⚡")
    print("\033[95m╚══════════════════════════════╝")

    print("\033[93mMobile Info Lookup Engine\n")

    print(f"\033[92m👤 User    : {user}")
    print(f"\033[92m💳 Credits : {credits}\n")


def verify_password():

    print("""
╔════════════════════════════════╗
🔒 ACCESS REQUIRED

Generate password contact admin

Telegram : @tabbo73
╚════════════════════════════════╝
""")

    password = input("🔒 Enter Tool Password : ")

    try:

        r = requests.get(
            AUTH_SERVER,
            params={"pass": password},
            timeout=10,
            proxies=get_proxy()
        ).json()

        if r.get("status") != "ok":

            print("\n❌ Invalid password")
            print("Telegram : @tabbo73\n")

            sys.exit()

        clear()

        print("✅ Access granted\n")

    except Exception as e:

        print("❌ Server connection failed")
        print(e)
        sys.exit()


def load_users():
    try:
        with open(USER_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_users(data):
    with open(USER_FILE,"w") as f:
        json.dump(data,f,indent=2)


def load_history():
    try:
        with open(HISTORY_FILE) as f:
            return json.load(f)
    except:
        return []


def save_history(data):
    with open(HISTORY_FILE,"w") as f:
        json.dump(data,f,indent=2)


def show_results(data, number):

    print("\n\033[93mRESULTS FOR :", number)

    if not isinstance(data, dict):
        print(data)
        return

    print(f"\n\033[92mFound {len(data)} record(s)\n")

    for i, key in enumerate(data,1):

        r = data[key]

        print("\033[96m━━━━━━━━ RECORD", i, "━━━━━━━━\n")

        print("\033[93mPERSONAL INFORMATION")
        print("\033[92mName   :", r.get("name","NA"))
        print("\033[92mFather :", r.get("fname","NA"))

        print("\n\033[93mADDRESS DETAILS")
        print("\033[92mLocation :", r.get("address","NA"))

        print("\n\033[93mNETWORK INFO")
        print("\033[92mCircle :", r.get("circle","NA"))
        print("\033[92mID     :", r.get("id","NA"))

        print("\n\033[96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


def lookup(user, users):

    if users[user] <= 0:
        print("❌ No credits left")
        input("Press enter...")
        return

    number = input("\n📱 Enter mobile number : ")

    print("🔎 Searching...")
    time.sleep(1)

    try:

        r = requests.get(
            LOOKUP_API + number,
            timeout=15,
            proxies=get_proxy()
        )

        data = r.json()

        show_results(data, number)

        history = load_history()
        history.append(number)
        save_history(history)

        users[user] -= 1
        save_users(users)

        print(f"\n💳 Credits left : {users[user]}\n")

    except Exception as e:

        print("❌ API Error")
        print(e)

    input("Press enter...")


def history():

    data = load_history()

    if not data:
        print("No history found")
    else:
        print("\n📜 SEARCH HISTORY\n")

        for i,n in enumerate(data,1):
            print(f"{i} - {n}")

    input("\nPress enter...")


def statistics():

    users = load_users()
    history_data = load_history()

    print("\n📊 STATISTICS\n")

    print(f"Total Users : {len(users)}")
    print(f"Total Searches : {len(history_data)}")

    input("\nPress enter...")


def clear_history():

    save_history([])
    print("History cleared")
    input("Press enter...")


def menu(user, users):

    while True:

        banner(user, users[user])

        print("""
╔════════════ MAIN MENU ════════════╗
[1] 🔎 Single Lookup
[2] 📜 Search History
[3] 📊 Statistics
[4] 🧹 Clear History
[5] ❌ Exit
╚═══════════════════════════════════╝
""")

        op = input("Select option : ")

        if op == "1":
            lookup(user, users)

        elif op == "2":
            history()

        elif op == "3":
            statistics()

        elif op == "4":
            clear_history()

        elif op == "5":
            print("Bye 👋")
            sys.exit()


def main():

    verify_password()

    users = load_users()

    user = input("👤 Enter username : ")

    if user not in users:
        users[user] = 5

    save_users(users)

    menu(user, users)


main()            sys.exit()

        clear()

        print("✅ Access granted\n")

    except:

        print("❌ Server connection failed")
        sys.exit()


def load_users():
    try:
        with open(USER_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_users(data):
    with open(USER_FILE,"w") as f:
        json.dump(data,f,indent=2)


def load_history():
    try:
        with open(HISTORY_FILE) as f:
            return json.load(f)
    except:
        return []


def save_history(data):
    with open(HISTORY_FILE,"w") as f:
        json.dump(data,f,indent=2)


def show_results(data, number):

    print("\n\033[93mRESULTS FOR :", number)

    if not isinstance(data, dict):
        print(data)
        return

    print(f"\n\033[92mFound {len(data)} record(s)\n")

    for i, key in enumerate(data,1):

        r = data[key]

        print("\033[96m━━━━━━━━ RECORD", i, "━━━━━━━━\n")

        print("\033[93mPERSONAL INFORMATION")
        print("\033[92mName   :", r.get("name","NA"))
        print("\033[92mFather :", r.get("fname","NA"))

        print("\n\033[93mADDRESS DETAILS")
        print("\033[92mLocation :", r.get("address","NA"))

        print("\n\033[93mNETWORK INFO")
        print("\033[92mCircle :", r.get("circle","NA"))
        print("\033[92mID     :", r.get("id","NA"))

        print("\n\033[96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


def lookup(user, users):

    if users[user] <= 0:
        print("❌ No credits left")
        input("Press enter...")
        return

    number = input("\n📱 Enter mobile number : ")

    print("🔎 Searching...")
    time.sleep(1)

    try:

        r = requests.get(LOOKUP_API + number)
        data = r.json()

        show_results(data, number)

        history = load_history()
        history.append(number)
        save_history(history)

        users[user] -= 1
        save_users(users)

        print(f"\n💳 Credits left : {users[user]}\n")

    except:
        print("❌ API Error")

    input("Press enter...")


def history():

    data = load_history()

    if not data:
        print("No history found")
    else:
        print("\n📜 SEARCH HISTORY\n")

        for i,n in enumerate(data,1):
            print(f"{i} - {n}")

    input("\nPress enter...")


def statistics():

    users = load_users()
    history_data = load_history()

    print("\n📊 STATISTICS\n")

    print(f"Total Users : {len(users)}")
    print(f"Total Searches : {len(history_data)}")

    input("\nPress enter...")


def clear_history():

    save_history([])
    print("History cleared")
    input("Press enter...")


def menu(user, users):

    while True:

        banner(user, users[user])

        print("""
╔════════════ MAIN MENU ════════════╗
[1] 🔎 Single Lookup
[2] 📜 Search History
[3] 📊 Statistics
[4] 🧹 Clear History
[5] ❌ Exit
╚═══════════════════════════════════╝
""")

        op = input("Select option : ")

        if op == "1":
            lookup(user, users)

        elif op == "2":
            history()

        elif op == "3":
            statistics()

        elif op == "4":
            clear_history()

        elif op == "5":
            print("Bye 👋")
            sys.exit()


def main():

    verify_password()

    users = load_users()

    user = input("👤 Enter username : ")

    if user not in users:
        users[user] = 5

    save_users(users)

    menu(user, users)


main()
    except:

        print(Fore.RED + "\n❌ Server connection failed\n")
        sys.exit()


def load_users():

    try:
        with open("users.json") as f:
            return json.load(f)
    except:
        return {}


def save_users(data):

    with open("users.json","w") as f:
        json.dump(data,f,indent=2)


def show_results(data):

    print(Fore.YELLOW + "\n📊 DATABASE RESULTS\n")

    if isinstance(data, dict):

        for i, key in enumerate(data,1):

            r = data[key]

            print(Fore.CYAN + "╔══════════════════════════════╗")
            print(Fore.CYAN + f"        📂 RECORD {i}")
            print(Fore.CYAN + "╚══════════════════════════════╝")

            print(Fore.GREEN + f"👤 Name     : {r.get('name','N/A')}")
            print(Fore.GREEN + f"👨 Father   : {r.get('fname','N/A')}")
            print(Fore.GREEN + f"🏠 Address  : {r.get('address','N/A')}")
            print(Fore.GREEN + f"☎ Alt Num   : {r.get('alt','N/A')}")
            print(Fore.GREEN + f"📡 Circle   : {r.get('circle','N/A')}")
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
