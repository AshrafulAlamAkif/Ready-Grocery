# add_product_auto.py
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
driver.get("https://uat-readygrocery.razinsoft.com/shop/login")
time.sleep(1)

# ---------- STEP 1: Login ----------
driver.find_element(By.ID, "email").send_keys("muky@mailinator.com")
driver.find_element(By.ID, "password").send_keys("12345678")

login_button = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", login_button)

# Wait for dashboard
time.sleep(1)
print("✅ Logged in successfully")

# ---------- STEP 2: Go to Add Product ----------
# Click "Product Management"
product_menu = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Product Management']"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", product_menu)
time.sleep(1)
driver.execute_script("arguments[0].click();", product_menu)
print("📦 Clicked Product Management menu")

# wait for dropdown to expand fully
time.sleep(1)

# ✅ Option 1: Try by href (most accurate)
try:
    add_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='productMenu']//a[contains(@href, '/shop/product/create')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", add_product)
    driver.execute_script("arguments[0].click();", add_product)
    print("🧾 Opened Add Product page successfully! (via href)")
except:
    print("⚠️ First try failed, trying fallback locator...")

    # ✅ Option 2: fallback locator by visible text
    add_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='productMenu']//a[contains(., 'Add Product')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", add_product)
    driver.execute_script("arguments[0].click();", add_product)
    print("🧾 Opened Add Product page successfully! (via text)")

time.sleep(2)


# ---------- STEP 3: Fill Product Form ----------
driver.find_element(By.ID, "product_name").send_keys("Misti Kumra Fali (Sweet Pumpkin Slice) ± 40 gm")
driver.find_element(By.NAME, "short_description").send_keys("This product was added using automation test.")
print("✍️ Filled basic info")

# Click "Generate AI" button (wait 65 sec)
try:
    generate_ai_btn = driver.find_element(By.ID, "generateAi")
    generate_ai_btn.click()
    print("⚙️ Clicked Generate AI button")
    time.sleep(65)
except:
    print("⚠️ Generate AI button not found, skipping...")

# Fill Unit
driver.find_element(By.ID, "unit").send_keys("kg")

#Product SKU Generate Code (force click via JS)
Generate_Code = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Generate Code')]//span[contains(@onclick, 'generateCode')]"))
)
driver.execute_script("arguments[0].click();", Generate_Code)
print("✅ Product SKU generated successfully")



# Buying price, Selling price, Discount, Stock, etc.
driver.find_element(By.ID, "buy_price").send_keys("100")
driver.find_element(By.ID, "price").send_keys("150")
driver.find_element(By.ID, "discount_price").send_keys("140")
driver.find_element(By.ID, "quantity").send_keys("20")
driver.find_element(By.ID, "min_order_quantity").send_keys("1")

print("💰 Filled pricing and quantity details")

# ---------- STEP 4: Select Category ----------
category_checkbox = driver.find_element(By.ID, "category_2")  # Example: Fruits
driver.execute_script("arguments[0].click();", category_checkbox)
print("🍎 Selected category: Fruits")

time.sleep(1)

# ---------- STEP 5: Upload Thumbnail ----------
try:
    thumb_label = driver.find_element(By.CSS_SELECTOR, "label.mainThumbnail")
    driver.execute_script("arguments[0].click();", thumb_label)
    print("🖼️ Opened image upload modal")

    time.sleep(2)
    driver.switch_to.frame("lfmIframe")
    print("🔄 Switched to image frame")

    # Select image (you can change data-id as needed)
    image_to_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.gridCart[data-id='5']"))
    )
    image_to_select.click()
    print("📸 Selected an image")

    time.sleep(2)

    confirm_button = driver.find_element(By.XPATH, "//nav[@id='actions']//a[@data-action='use']")
    confirm_button.click()
    print("✅ Clicked Confirm button successfully")

    # Switch back to main content
    driver.switch_to.default_content()
    print("⬅️ Returned to main admin page")

except Exception as e:
    print("⚠️ Thumbnail upload skipped:", e)

# ---------- STEP 6: Submit the Product ----------

submit_btn = driver.find_element(By.XPATH, "//button[contains(.,'Submit') or contains(.,'Save')]")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", submit_btn)
print("📤 Submitted the product")


# ---------- STEP 7: Wait & Verify ----------
time.sleep(5)
if "products" in driver.current_url:
    print("🎉 Product added successfully!")
else:
    print("❌ Something went wrong while adding product.")

driver.quit()

