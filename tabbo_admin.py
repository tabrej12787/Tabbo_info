import json
import sys

USERS_FILE = "users.json"

ADMIN_ID = "admin"
ADMIN_PASS = "tabboadmin"


def load_users():
    try:
        with open(USERS_FILE) as f:
            return json.load(f)
    except:
        return {}


def save_users(data):
    with open(USERS_FILE,"w") as f:
        json.dump(data,f,indent=2)


print("""

█████ ADMIN PANEL █████

""")

admin_id = input("Admin ID : ")
admin_pass = input("Password : ")

if admin_id != ADMIN_ID or admin_pass != ADMIN_PASS:

    print("❌ Invalid admin login")
    sys.exit()


while True:

    print("""

1 Total Users
2 User Info
3 Give Credits
4 Exit

""")

    op = input("Select : ")

    users = load_users()

    if op == "1":

        print("\n👥 Total Users :",len(users))


    elif op == "2":

        for u in users:

            print("\n👤 User :",u)
            print("🌐 IP :",users[u]["ip"])
            print("💳 Credits :",users[u]["credits"])
            print("📊 Used :",users[u]["used"])


    elif op == "3":

        u = input("Username : ")

        if u not in users:
            print("User not found")
            continue

        c = int(input("Credits to add : "))

        users[u]["credits"] += c

        save_users(users)

        print("✅ Credits added")


    elif op == "4":
        sys.exit()
