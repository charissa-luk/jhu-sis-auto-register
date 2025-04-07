# jhu-sis-auto-register
# JHU SIS Auto Registration Bot

This Python script automates course registration on [JHU SIS](https://sis.jhu.edu/sswf/) using Selenium. It navigates through the Microsoft SSO login, expands the registration menu, selects all courses in your cart, and clicks register right at the time you choose.

---

## 🚀 Features
- Automatic login via Microsoft SSO
- Navigates to "My Cart"
- Selects all classes
- Clicks "Register" at your target time
- Built-in retry and wait logic for slow SIS loads

---

## 🔧 Requirements
- Python 3.7+
- Google Chrome (latest version)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (must match your Chrome version)

Install required Python libraries:
```bash
pip install selenium python-dateutil
```

---

## 🧪 Usage
Run from the terminal:
```bash
python sis_register.py
```
You will be prompted interactively to enter:
- Your JHU email
- Your JHU password
- Time to register (24-hour format: HH:MM)

> ⏰ **Important**: Make sure your Mac's clock is synced with [NIST Time](https://time.gov) for accurate registration.

> 🔐 **2-Factor Auth Note**: If 2-Factor Authentication is required when logging in, the script will not work. To workaround, make sure you have logged into your Microsoft account manually using 2-Factor Authentication earlier in the day.

---

## ⚠️ Notes
- **SIS is extremely slow.** This script uses long wait times (up to 2 minutes per element) to avoid breaking.
- Works best with stable internet and if you're pre-logged in to Chrome.
- Automatically logs in **7 minutes before registration time**.

---

## 📸 Screenshots
Any failures in the process will auto-save screenshots to help with debugging.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits
Created by Charissa for the JHU community. Feel free to fork and contribute!

---

## 👾 Disclaimer
Use responsibly. This is an automation tool meant to assist, not to exploit. Always verify registration results on SIS manually.

