🔎 TABBO NUMBER INFO TOOL

A professional OSINT mobile number lookup tool designed for Termux / Linux environments.

The tool allows users to search mobile numbers and display structured information such as:

- Name
- Father Name
- Address
- Network Circle
- Unique ID

---

⚡ Features

Feature| Description
🔎 Mobile Lookup| Search mobile number information
🎨 Colored UI| Professional terminal interface
💳 Credit System| Each user has limited search credits
📜 Search History| View previously searched numbers
🧹 Clear History| Reset search history
📖 Guide| Built-in usage guide
🔐 Password Protection| Secure login system

---

📦 Requirements

- Python 3
- Termux / Linux
- Internet Connection

Install required libraries:

pip install requests colorama

---

🚀 Installation (Termux)

Update packages

pkg update -y

Install dependencies

pkg install git python -y

Clone repository

git clone https://github.com/tabrej12787/tabbo-info-tool.git

Enter project folder

cd tabbo-info-tool

Install Python libraries

pip install requests colorama

Create required files

echo {} > users.json
echo [] > history.json

Run the tool

python tabbo.py

---

🔐 Authentication

The tool requires password authentication before usage.

If you do not have access, contact the administrator:

📩 Telegram: @tabbo73

---

💳 Credit System

Each user receives 5 default credits.

Action| Credits Used
Mobile Search| 1 Credit

When credits are exhausted the tool will display:

YOUR CREDITS FINISHED
Contact Admin For More Credits
Telegram : @tabbo73

---

📊 Example Output (Sample Data)

RESULTS FOR : 9000000000

RECORD 1

👤 Name : Demo User
👨 Father : Example Person

🏠 ADDRESS DETAILS
Village  : Demo Village
City     : Sample City
District : Example District
State    : Example State
Pincode  : 000000

📡 Circle : Demo Network
🆔 ID : 123456789012

---

⚠️ Disclaimer

This tool is created strictly for educational and research purposes.

The developer is not responsible for misuse or illegal activities performed using this tool.

---

👨‍💻 Developer

TABBO

Telegram: https://t.me/tabbo73

---

⭐ If you found this project useful, consider giving it a star on GitHub.
