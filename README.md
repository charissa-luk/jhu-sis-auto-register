# 💾 JHU SIS Auto Registration Bot

This Python script automates course registration on [JHU SIS](https://sis.jhu.edu/sswf/) using Selenium. It logs in via Microsoft SSO, navigates to the registration cart, selects all classes, and clicks register at your specified time — **with a 7-minute pre-login buffer**.

---

## 🚀 Features
- Logs in with your JHU Microsoft credentials
- Navigates to the registration cart
- Waits for the exact time to register
- Selects all classes and clicks "Register"
- Handles SIS slowness with retries and waits
- Interactive terminal prompts for credentials and time

---

## 🔧 Requirements

- **macOS** (tested; Windows not guaranteed)
- **Python 3.7+**
- **Google Chrome** (latest version)
- **ChromeDriver** matching your Chrome version  
  Download: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

---

## 📦 Installation & Setup

### 1. 🔁 Clone the Repo
```bash
git clone https://github.com/charissa-luk/jhu-sis-auto-register.git
cd jhu-sis-auto-register
```

### 2. 🐍 Create & Activate a Virtual Environment (Recommended)
```bash
python3 -m venv sis-bot-venv
source sis-bot-venv/bin/activate
```

### 3. 📦 Install Required Packages
```bash
pip install selenium python-dateutil
```

---

## ⏲️ Sync Your Clock (macOS Only)

SIS uses the US Naval Observatory (NIST) clock. You must sync your Mac to match this time source:

1. Open **System Preferences** → **Date & Time**
2. In the **Time Server** field, click **Set** and enter your Mac password
3. Change the server from `time.apple.com` ➜ `tick.usno.navy.mil`
4. Click the lock again to save your changes

---

## ▶️ Run the Bot
From the repo folder:
```bash
python sis_register.py
```

The script will prompt you for:

- 📧 **JHU email**
- 🔑 **Password**
- ⏰ **Registration time** (24-hour format, e.g., `07:00` for 7AM)

> ⏳ The bot logs in **7 minutes before** the registration time and waits.

---

## 🧠 Notes

- SIS is very slow — this bot uses long wait times (up to 2 mins per element)
- You **must** have already added classes to your Enrollment Cart
- If you use **2-Factor Authentication (2FA)**:
  - The script will **not work** through the 2FA page
  - **Workaround**: log into your Microsoft account **manually** earlier that day, so 2FA won’t be triggered

---

## 🧪 Troubleshooting

- 🧳 Make sure **Google Chrome** and **ChromeDriver** are:
  - Fully up to date
  - Exactly the same version

---

## 📄 License

[MIT License](LICENSE)

---

## 🙏 Credits

Created by Charissa for the JHU community. Feel free to fork and improve.
