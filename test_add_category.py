# ==============================test_add_category.py
# Test Script: Add Category (ReadyGrocery Admin)
# Author: Ashraful Alam Akif
# Level: Beginner Friendly
# ==============================

# ---------- Import all required modules ----------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- STEP 1: Setup Chrome ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# ---------- STEP 2: Open Admin Login Page ----------
driver.get("https://uat-readygrocery.razinsoft.com/admin/login")
print("✅ Opened login page")
time.sleep(2)

# ---------- STEP 3: Login ----------
try:
    # Click the 'Copy' button (auto fills credentials)
    copy_btn = driver.find_element(By.CLASS_NAME, "copyBtn")
    copy_btn.click()
    print("✅ Clicked copy button (credentials auto-filled)")
    time.sleep(1)
except:
    # If not found, fill login manually
    print("⚠️ Copy button not found. Filling manually...")
    driver.find_element(By.ID, "email").send_keys("root@grocery.com")
    driver.find_element(By.ID, "password").send_keys("secret@123")

# Click login button
login_btn = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
login_btn.click()
print("✅ Clicked login button")
time.sleep(3)

# ---------- STEP 4: Click 'Categories' from sidebar ----------
categories_menu = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Categories"))
)
categories_menu.click()
print("✅ Clicked 'Categories' option from sidebar")
time.sleep(3)

# ---------- STEP 5: Fill 'Add Category' form ----------
timestamp = int(time.time())  # to make unique name
category_name = f"AutoCategory_{timestamp}"

# Fill Name
driver.find_element(By.ID, "name").send_keys(category_name)
print("✅ Filled category name")

# Fill Description
driver.find_element(By.ID, "description").send_keys("This is a test category created by automation.")
print("✅ Filled description")

# Toggle status (optional)
checkbox = driver.find_element(By.ID, "is_active")
if not checkbox.is_selected():
    checkbox.click()
print("✅ Checked 'Active' status")

# ---------- STEP 6: Submit the form ----------
submit_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "submitButton"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)
submit_btn.click()
print("✅ Clicked Submit button")

# ---------- STEP 7: Screenshot ----------
time.sleep(3)
driver.save_screenshot(f"category_add_{timestamp}.png")
print(f"📸 Screenshot saved as category_add_{timestamp}.png")
print(f"🎉 Category '{category_name}' added successfully!")

# ---------- STEP 8: Close Browser ----------
driver.quit()
print("✅ Browser closed successfully")
