from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- Setup ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# ---------- STEP 1: Open login page ----------
driver.get("https://uat-readygrocery.razinsoft.com/admin/login")
print("Opened login page")
time.sleep(2)

# ---------- STEP 2: Login ----------
driver.find_element(By.ID, "email").send_keys("root@grocery.com")
driver.find_element(By.ID, "password").send_keys("secret@123")
driver.find_element(By.CSS_SELECTOR, "button.loginButton").click()
print("Clicked login button")
time.sleep(3)

# ---------- STEP 3: Navigate to 'Categories' ----------
categories_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Categories")))
categories_menu.click()
print("Clicked Categories option")
time.sleep(2)

# ---------- STEP 4: Fill category form ----------
driver.find_element(By.ID, "name").send_keys("Automation Category")
driver.find_element(By.ID, "description").send_keys("This is a test category created by automation.")

# Ensure 'Active' checkbox is selected
is_active_checkbox = driver.find_element(By.ID, "is_active")
if not is_active_checkbox.is_selected():
    is_active_checkbox.click()

# ---------- STEP 5: Image Upload ----------
# Click on image container to open uploader
image_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label.mainThumbnail")))
driver.execute_script("arguments[0].click();", image_container)
print("Clicked image container to open uploader")
time.sleep(2)

# Switch to iframe
iframe = wait.until(EC.presence_of_element_located((By.ID, "lfmIframe")))
driver.switch_to.frame(iframe)
print("Switched to iframe")

# Wait for images to appear inside iframe
modal_images = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, "div.gridCart div.square"))
print(f"Found {len(modal_images)} images inside iframe")

# Select the first image (you can choose a specific data-id if needed)
if modal_images:
    driver.execute_script("arguments[0].scrollIntoView(true);", modal_images[7])
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", modal_images[7])
    print("Selected first image")
    time.sleep(2) # wait 2 seconds before confirming

# Wait for Confirm button inside iframe and click
confirm_btn = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "a[data-action='use']"))
driver.execute_script("arguments[0].click();", confirm_btn)
print("Clicked Confirm button")
time.sleep(2)  # wait 2 seconds after confirming

# Switch back to main content
driver.switch_to.default_content()

# ---------- STEP 6: Submit the form ----------
submit_btn = driver.find_element(By.ID, "submitButton")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", submit_btn)
print("Clicked Submit button")

# ---------- STEP 7: Screenshot ----------
time.sleep(3)
driver.save_screenshot("category_added.png")
print("Category created and screenshot saved!")

driver.quit()
