import os
import sys
import time
import datetime
from dateutil import parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import tempfile

# --------------------------
# Interactive input setup
# --------------------------
print("📝 Enter the following information to set up the SIS bot:")
email = input("📧 Your JHU email address: ")
password = input("🔐 Your JHU password: ")
time_input = input("⏰ Time to register (24-hour format HH:MM): ")

# --------------------------
# Time setup
# --------------------------
registration_time = parser.parse(time_input)
now = datetime.datetime.now()
registration_time = registration_time.replace(year=now.year, month=now.month, day=now.day)

# If it's already past the input time today, register tomorrow
if registration_time <= now:
    registration_time += datetime.timedelta(days=1)

# --------------------------
# Chrome Setup: Use saved Chrome login session
# --------------------------
unique_user_data_dir = tempfile.mkdtemp()
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={unique_user_data_dir}")
chrome_options.add_argument("profile-directory=Default")
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://sis.jhu.edu/sswf/")

# --------------------------
# Handling "Sign In" Button
# --------------------------
print("🔑 Searching for the 'Sign In' button and logging in with provided credentials...")

try:
    sign_in_button = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sign In')]"))
    )
    sign_in_button.click()
    print("✅ 'Sign In' button clicked.")

    # Wait for the Microsoft login page and make sure the email field is visible & interactable
    WebDriverWait(browser, 69).until(
        EC.visibility_of_element_located((By.NAME, "loginfmt"))
    )
    email_field = browser.find_element(By.NAME, "loginfmt")

    # Ensure it's clickable
    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.NAME, "loginfmt")))
    email_field.click()  # This helps in some cases
    email_field.clear()  # Just in case it's prefilled and can't be typed into
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

    time.sleep(2)

    WebDriverWait(browser, 69).until(EC.element_to_be_clickable((By.NAME, "passwd")))
    password_field = browser.find_element(By.NAME, "passwd")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    try:
        continue_btn = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.ID, 'ctl00_contentPlaceHolder_btnContinueToIsis'))
        )
        print("✅ SIS post-login page loaded.")
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_btn)
        browser.execute_script("arguments[0].click();", continue_btn)
        print("✅ Clicked 'Continue to SIS' button.")
    except Exception as e:
        print(f"❌ Failed to click 'Continue to SIS'. Error: {e}")
        sys.exit(1)

except Exception as e:
    print(f"❌ Login failed. Error: {str(e)}")
    sys.exit(1)

# --------------------------
# Navigate to My Cart
# --------------------------
try:
    registration_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Registration']]"))
    )
    registration_link.click()
    print("✅ Clicked 'Registration'")
except Exception as e:
    print(f"❌ Failed to click 'Registration': {e}")
    browser.quit()
    sys.exit(1)

try:
    my_cart_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "My Cart"))
    )
    my_cart_link.click()
    print("✅ Clicked 'My Cart'")
except Exception as e:
    print(f"❌ Failed to click 'My Cart': {e}")
    browser.quit()
    sys.exit(1)

MAX_RETRIES = 10
WAIT_TIME = 120

for attempt in range(MAX_RETRIES):
    try:
        print(f"🔄 Attempt {attempt + 1} to load cart elements...")

        WebDriverWait(browser, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, 'SelectAllCheckBox'))
        )
        select_all = browser.find_element(By.ID, 'SelectAllCheckBox')
        select_all.click()
        print("✅ Clicked 'Select All' checkbox.")

        WebDriverWait(browser, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, 'ctl00_contentPlaceHolder_ibEnroll'))
        )
        register_button = browser.find_element(By.ID, 'ctl00_contentPlaceHolder_ibEnroll')
        print("✅ Register button is ready.")
        break

    except (TimeoutException, NoSuchElementException) as e:
        print(f"⚠️ Attempt {attempt + 1} failed: {str(e)}")
        if attempt == MAX_RETRIES - 1:
            print("❌ SIS is too slow or DOM broke. Exiting.")
            browser.save_screenshot("load_cart_fail.png")
            browser.quit()
            sys.exit(1)
        else:
            print("🔁 Retrying...")

# WAIT for registration time
print(f"⏳ Waiting for registration at {registration_time.strftime('%H:%M:%S')}...")
while datetime.datetime.now() < registration_time:
    time.sleep(1)

# Click register
try:
    print("🚀 Clicking Register...")
    register_button.click()
    print("✅ Register clicked!")
    time.sleep(10)
except Exception as e:
    print(f"❌ Failed to click register: {e}")
    browser.quit()
    sys.exit(1)
