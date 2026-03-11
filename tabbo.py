import requests
import os
import json
import sys
import time
from dotenv import load_dotenv
from colorama import Fore, Style, init

init()
load_dotenv()

PASS = os.getenv("TABBO_PASS")
KEY = os.getenv("API_KEY")
API = os.getenv("API_URL")

def banner():

    print(Fore.CYAN + """

████████╗ █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
   ██║   ███████║██████╔╝██████╔╝
   ██║   ██╔══██║██╔══██╗██╔══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝

✨ TABBO INFO LOOKUP ✨
Credit By ❤️ Tabbo
""")

def loading():

    print(Fore.GREEN + "\n🔎 Scanning database", end="")

    for i in range(3):
        time.sleep(0.5)
        print(".", end="")

    print("\n")

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

    if not isinstance(data,list):

        print(data)
        return

    print(Fore.YELLOW + f"\n📊 Found {len(data)} Records\n")

    for i,r in enumerate(data,1):

        print(Fore.CYAN + f"━━━ RECORD {i} ━━━")

        print(Fore.GREEN + f"👤 Name   : {r.get('name','NA')}")
        print(f"👨 Father : {r.get('fname','NA')}")
        print(f"🏠 Address: {r.get('address','NA')}")
        print(f"☎ Alt    : {r.get('alt','NA')}")
        print(f"🆔 ID     : {r.get('id','NA')}")

        print(Fore.CYAN + "━━━━━━━━━━━━━━\n")

def lookup():

    users = load_users()

    user = input("👤 Username : ")

    if user not in users:
        users[user] = 5

    if users[user] <= 0:

        print(Fore.RED + "❌ No credits left")
        return

    num = input("📱 Enter mobile number : ")

    loading()

    url = f"{API}?key={KEY}&mobile={num}"

    try:

        r = requests.get(url).json()

        show_results(r)

    except:

        print("❌ API Error")

    users[user] -= 1

    save_users(users)

    print(Fore.MAGENTA + f"💳 Credits left : {users[user]}")

def admin_panel():

    p = input("🔒 Admin Password : ")

    if p != PASS:

        print("❌ Wrong password")
        return

    users = load_users()

    while True:

        print(Fore.CYAN + """

╔════ ADMIN PANEL ════╗
1 - Show Users
2 - Add Credits
3 - Reset User Credits
4 - Exit
╚═════════════════════╝
""")

        op = input("Select : ")

        if op == "1":

            for u in users:

                print(f"{u} → Credits : {users[u]}")

        elif op == "2":

            u = input("Username : ")

            c = int(input("Add credits : "))

            if u not in users:

                users[u] = 0

            users[u] += c

            save_users(users)

            print("✅ Credits added")

        elif op == "3":

            u = input("Username : ")

            users[u] = 5

            save_users(users)

            print("♻️ Credits reset")

        elif op == "4":

            break

def main():

    banner()

    if "--admin" in sys.argv:

        admin_panel()

    else:

        lookup()

main()    key = request.form["key"]
    expiry = request.form["expiry"]
    limit = request.form["limit"]

    cursor.execute(
        "INSERT INTO users VALUES(?,?,?)",
        (key, expiry, limit)
    )

    db.commit()

    return "API Created"


@app.route("/lookup")
def lookup():

    key = request.args.get("key")
    mobile = request.args.get("mobile")

    cursor.execute(
        "SELECT expiry FROM users WHERE api_key=?",
        (key,)
    )

    user = cursor.fetchone()

    if not user:
        return {"error":"invalid api key"}

    expiry = user[0]

    if datetime.now().date() > datetime.fromisoformat(expiry).date():
        return {"error":"api expired"}

    url=f"https://api.vectorxo.online/lookup?key={VECTOR_KEY}&mobile={mobile}"

    r=requests.get(url)

    return jsonify(r.json())


app.run(host="0.0.0.0", port=5000)
