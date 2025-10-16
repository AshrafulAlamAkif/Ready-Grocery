# # test_readygrocery_login_updated.py
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# URL = "https://readygrocery.razinsoft.com/admin/login"
# EMAIL = "root@readygrocery.com"
# PASSWORD = "secret@123"

# # Setup Chrome driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# wait = WebDriverWait(driver, 10)

# try:
#     driver.get(URL)

#     # --------------------------
#     # Step 1: Try clicking copy button
#     # --------------------------
#     try:
#         copy_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "copyBtn")))
#         # JS click to avoid interception
#         driver.execute_script("arguments[0].click();", copy_btn)
#         print("Copy button clicked, credentials auto-filled")
#         time.sleep(0.5)
#     except:
#         print("Warning: Copy button not found / not clickable")

#     # --------------------------
#     # Step 2: Fill email & password manually if needed
#     # --------------------------
#     email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
#     password_field = driver.find_element(By.ID, "password")

#     email_field.clear()
#     email_field.send_keys(EMAIL)
#     password_field.clear()
#     password_field.send_keys(PASSWORD)

#     # --------------------------
#     # Step 3: Click Login
#     # --------------------------
#     login_btn = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
#     driver.execute_script("arguments[0].click();", login_btn)

#     # --------------------------
#     # Step 4: Wait for dashboard / URL change
#     # --------------------------
#     try:
#         wait.until(EC.url_contains("/admin"))
#         print("Login successful")
#         driver.save_screenshot("login_success.png")
#     except:
#         print("Login failed")
#         driver.save_screenshot("login_failed.png")

# finally:
#     time.sleep(2)
#     driver.quit()



# ----------beginner_readygrocery_login_easy.py----------
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

# ---------- STEP 1: Fill email & password ----------
driver.find_element(By.ID, "email").send_keys("root@readygrocery.com")
driver.find_element(By.ID, "password").send_keys("secret@123")

# ---------- STEP 2: Click Login (Safe JS click) ----------
login_button = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", login_button)

# ---------- STEP 3: Wait & Screenshot ----------
time.sleep(3)  # wait for dashboard to load
if "/admin" in driver.current_url:
    print("✅ Login successful")
    driver.save_screenshot("login_success.png")
else:
    print("❌ Login failed")
    driver.save_screenshot("login_failed.png")

# ---------- STEP 4: Close Browser ----------
driver.quit()
