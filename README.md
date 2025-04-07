# JHU SIS Auto Registration Bot

This Python script automates course registration on [JHU SIS](https://sis.jhu.edu/sswf/) using Selenium. It navigates through the Microsoft SSO login, expands the registration menu, selects all courses in your cart, and clicks register right at the time you choose.

---

## 🚀 Features
- Automatic login via Microsoft SSO
- Navigates to "My Cart"
- Selects all classes
- Clicks "Register" at your target time
- Built-in retry and wait logic for slow SIS loads
- Prompts for email, password, and registration time interactively

---

## 🔧 Requirements
- macOS (script is tested only on Mac — Windows compatibility not guaranteed)
- Python 3.7+
- Google Chrome (latest version)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (must match your Chrome version)

Install required Python libraries:
```bash
pip install selenium python-dateutil
```

---

## 🧪 How to Use

### 1. 📦 Download or Clone the Repo
```bash
git clone https://github.com/open-minded-you/jhu-sis-auto-register.git
cd jhu-sis-auto-register
```

### 2. ▶️ Run the Bot
```bash
python sis_register.py
```

You will be prompted to enter:
- Your **JHU email**
- Your **JHU password**
- Your **registration time** in **24-hour format** (e.g., `07:00` for 7:00 AM, `13:30` for 1:30 PM)

> ⏰ **Important**: Use [NIST Time](https://time.gov) to sync your system clock before running this script.

> 💡 The script automatically logs in **7 minutes before** your chosen registration time and patiently waits.

---

## ⚠️ Notes
- SIS is **extremely slow**. This script uses long wait times (up to 2 minutes per element) to ensure reliability.
- If you use **2-Factor Authentication**, this script will **not work**. As a workaround, log into your Microsoft account manually earlier in the day.
- You must already have classes in your Enrollment Cart.
- Always double-check SIS afterward to confirm your enrollment.

---

## 📸 Screenshots
Any failure will auto-save a screenshot to help you debug what went wrong.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits
Created by Charissa for the JHU community. Fork, improve, and share freely!

---

## 👾 Disclaimer
This bot is a helpful assistant, not an exploit. Please use it responsibly and at your own risk. Confirm all course registrations manually on SIS afterward.

Works on **macOS** only. Windows support is untested and not guaranteed.
