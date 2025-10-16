# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # ---------- Setup ----------
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)

# # ---------- STEP 1: Open login page ----------
# driver.get("https://readygrocery.razinsoft.com/admin/login")
# print("Opened login page")
# time.sleep(2)

# # ---------- STEP 2: Login ----------
# try:
#     # click copy button if available
#     copy_btn = driver.find_element(By.CLASS_NAME, "copyBtn")
#     copy_btn.click()
#     print("Clicked copy button")
#     time.sleep(1)
# except:
#     print("Copy button not found. Filling manually.")
#     driver.find_element(By.ID, "email").send_keys("root@readygrocery.com")
#     driver.find_element(By.ID, "password").send_keys("secret@123")

# # click login
# login_btn = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
# login_btn.click()
# print("Clicked login button")
# time.sleep(3)

# # ---------- STEP 3: Navigate to 'Add Vendor' page ----------
# # expand 'Vendors' dropdown
# vendors_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-bs-toggle='collapse'][href='#shopMenu']")))
# vendors_menu.click()
# print("Clicked Vendors dropdown")
# time.sleep(1)

# # click 'Add Vendor'
# add_vendor = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Vendor")))
# add_vendor.click()
# print("Clicked Add Vendor option")
# time.sleep(3)

# # ---------- STEP 4: Fill vendor form ----------
# timestamp = int(time.time())
# unique_email = f"vendor{timestamp}@gmail.com"
# unique_shop = f"Shop{timestamp}"

# # Fill user info
# driver.find_element(By.ID, "first_name").send_keys("Akif")
# driver.find_element(By.ID, "last_name").send_keys("Alam")
# driver.find_element(By.ID, "phone").send_keys("01700000000")

# # Select gender dropdown
# gender_dropdown = Select(driver.find_element(By.ID, "gender"))
# gender_dropdown.select_by_visible_text("Male")

# # ---------- Account Information ----------
# driver.find_element(By.ID, "email").send_keys(unique_email)
# driver.find_element(By.ID, "password").send_keys("12345678")
# driver.find_element(By.ID, "password_confirmation").send_keys("12345678")

# # ---------- Shop Information ----------
# driver.find_element(By.ID, "shop_name").send_keys(unique_shop)
# driver.find_element(By.ID, "address").send_keys("Dhaka, Bangladesh")
# driver.find_element(By.ID, "description").send_keys("This is a test vendor created by automation.")

# # ---------- STEP 5: Submit ----------
# # submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
# # submit_btn.click() 
# submit_btn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
# print("Clicked Submit button")

# # Step 6: Scroll and click safely
# driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", submit_btn)

# # ---------- STEP 7: Verify & Screenshot ----------
# time.sleep(3)
# driver.save_screenshot(f"add_vendor_{timestamp}.png")
# print(f"Vendor created with email: {unique_email}")
# print("Screenshot saved!")

# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # ---------- Setup ----------
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# wait = WebDriverWait(driver, 15)

# # ---------- STEP 1: Open login page ----------
# driver.get("https://uat-readygrocery.razinsoft.com/admin/login")
# print("Opened login page")
# time.sleep(2)

# # ---------- STEP 2: Login ----------
# try:
#     copy_btn = driver.find_element(By.CLASS_NAME, "copyBtn")
#     copy_btn.click()
#     print("Clicked copy button")
#     time.sleep(1)
# except:
#     print("Copy button not found. Filling manually.")
#     driver.find_element(By.ID, "email").send_keys("root@grocery.com")
#     driver.find_element(By.ID, "password").send_keys("secret@123")

# # Click login button
# login_btn = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
# login_btn.click()
# print("Clicked login button")
# time.sleep(3)

# # ---------- STEP 3: Navigate to Add Vendor ----------
# vendors_menu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-bs-toggle='collapse'][href='#shopMenu']")))
# vendors_menu.click()
# print("Clicked Vendors dropdown")
# time.sleep(1)

# add_vendor = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Vendor")))
# add_vendor.click()
# print("Clicked Add Vendor option")
# time.sleep(3)

# # ---------- STEP 4: Fill vendor form ----------
# timestamp = int(time.time())
# unique_email = f"vendor{timestamp}@gmail.com"
# unique_shop = f"Shop{timestamp}"

# driver.find_element(By.ID, "first_name").send_keys("Akif")
# driver.find_element(By.ID, "last_name").send_keys("Alam")
# driver.find_element(By.ID, "phone").send_keys("01700000000")

# gender_dropdown = Select(driver.find_element(By.ID, "gender"))
# gender_dropdown.select_by_visible_text("Male")

# driver.find_element(By.ID, "email").send_keys(unique_email)
# driver.find_element(By.ID, "password").send_keys("12345678")
# driver.find_element(By.ID, "password_confirmation").send_keys("12345678")

# driver.find_element(By.ID, "shop_name").send_keys(unique_shop)
# driver.find_element(By.ID, "address").send_keys("Dhaka, Bangladesh")
# driver.find_element(By.ID, "description").send_keys("This is a test vendor created by automation.")

# # ---------- STEP 5: Click Submit (Safely) ----------
# try:
#     # Wait for button to appear (by multiple options)
#     submit_btn = wait.until(
#         EC.element_to_be_clickable((
#             By.XPATH, "//button[contains(., 'Submit') or contains(., 'Save') or @type='submit']"
#         ))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
#     time.sleep(1)
#     driver.execute_script("arguments[0].click();", submit_btn)
#     print("✅ Clicked Submit button successfully")
# except Exception as e:
#     print("❌ Submit button not found or not clickable:", e)

# # ---------- STEP 6: Verify & Screenshot ----------
# time.sleep(3)
# driver.save_screenshot(f"add_vendor_{timestamp}.png")
# print(f"Vendor created with email: {unique_email}")
# print("📸 Screenshot saved successfully!")

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ---------- Setup ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 20)  # Increased wait for slow load

# ---------- STEP 1: Open login page ----------
driver.get("https://uat-readygrocery.razinsoft.com/admin/login")
print("Opened login page")
time.sleep(2)

# ---------- STEP 2: Login ----------
try:
    copy_btn = driver.find_element(By.CLASS_NAME, "copyBtn")
    driver.execute_script("arguments[0].click();", copy_btn)
    print("Clicked copy button via JS")
    time.sleep(1)
except:
    print("Copy button not found. Filling manually.")
    driver.find_element(By.ID, "email").send_keys("root@grocery.com")
    driver.find_element(By.ID, "password").send_keys("secret@123")

# Click login button safely
login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.loginButton")))
driver.execute_script("arguments[0].click();", login_btn)
print("Clicked login button via JS")
time.sleep(3)

# ---------- STEP 3: Navigate to Add Vendor ----------
vendors_menu = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "a[data-bs-toggle='collapse'][href='#shopMenu']")
))
driver.execute_script("arguments[0].scrollIntoView(true);", vendors_menu)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", vendors_menu)
print("Clicked Vendors dropdown via JS")
time.sleep(1)

add_vendor = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Vendor")))
driver.execute_script("arguments[0].scrollIntoView(true);", add_vendor)
driver.execute_script("arguments[0].click();", add_vendor)
print("Clicked Add Vendor option via JS")
time.sleep(3)

# ---------- STEP 4: Fill vendor form ----------
timestamp = int(time.time())
unique_email = f"vendor{timestamp}@gmail.com"
unique_shop = f"Shop{timestamp}"

driver.find_element(By.ID, "first_name").send_keys("Akif")
driver.find_element(By.ID, "last_name").send_keys("Alam")
driver.find_element(By.ID, "phone").send_keys("01700000000")

gender_dropdown = Select(driver.find_element(By.ID, "gender"))
gender_dropdown.select_by_visible_text("Male")

driver.find_element(By.ID, "email").send_keys(unique_email)
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.ID, "password_confirmation").send_keys("12345678")

driver.find_element(By.ID, "shop_name").send_keys(unique_shop)
driver.find_element(By.ID, "address").send_keys("Dhaka, Bangladesh")
driver.find_element(By.ID, "description").send_keys("This is a test vendor created by automation.")

# ---------- STEP 4.1: Upload Profile Photo ----------
image_path = r"C:\Users\Ashraful Alam Akif\ReadyGrocery\image.png"  # Path to your image
if os.path.exists(image_path):
    file_input = driver.find_element(By.ID, "thumbnail")
    file_input.send_keys(image_path)
    print("✅ Profile photo uploaded successfully")
    time.sleep(1)  # wait for preview update
else:
    print("❌ Profile photo not found at:", image_path)

# ---------- STEP 5: Click Submit safely ----------
try:
    submit_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[contains(., 'Submit') or contains(., 'Save') or @type='submit']"
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", submit_btn)
    print("✅ Clicked Submit button via JS successfully")
except Exception as e:
    print("❌ Submit button not found or not clickable:", e)

# ---------- STEP 6: Verify & Screenshot ----------
time.sleep(3)
driver.save_screenshot(f"add_vendor_{timestamp}.png")
print(f"Vendor created with email: {unique_email}")
print("📸 Screenshot saved successfully!")

driver.quit()
