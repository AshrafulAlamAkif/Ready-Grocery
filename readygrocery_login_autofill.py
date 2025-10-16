# readygrocery_login_autofill.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- Setup ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://readygrocery.razinsoft.com/admin/login")
time.sleep(2)  # wait for page load

# ---------- STEP 1: Try copy button auto-fill ----------
try:
    copy_btn = driver.find_element(By.CLASS_NAME, "copyBtn")
    # JS click to avoid interception issues
    driver.execute_script("arguments[0].click();", copy_btn)
    print("Copy button clicked, credentials auto-filled")
    time.sleep(1)
except:
    print("Copy button not found / cannot click, will fill manually")

# ---------- STEP 2: Fill email & password manually (fallback) ----------
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

# Clear first just in case
email_field.clear()
email_field.send_keys("root@readygrocery.com")
password_field.clear()
password_field.send_keys("secret@123")

# ---------- STEP 3: Click Login ----------
login_button = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", login_button)

# ---------- STEP 4: Wait & Screenshot ----------
time.sleep(3)
if "/admin" in driver.current_url:
    print("Login successful")
    driver.save_screenshot("login_success.png")
else:
    print("Login failed")
    driver.save_screenshot("login_failed.png")

# ---------- STEP 5: Close Browser ----------
driver.quit()
