# add_multi_product.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# import pandas as pd
# # 🔗 Google Sheet CSV Link
# csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQEQPLmKdFSH3NZzxvKYC28CzsDx0Zk5ox62LM9POcpRUS1bU46nwsXVHZMoe73gqB9pxutsoSI_y-C/pub?gid=1498794614&single=true&output=csv"
# # 📥 Read products from Google Sheet CSV
# df = pd.read_csv(csv_url)
# # 🛒 Convert to list of dicts
# products = df.to_dict(orient="records")



# ---------- Setup ----------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://uat-readygrocery.razinsoft.com/admin/login")
time.sleep(2)

# ---------- STEP 1: Login ----------
driver.find_element(By.ID, "email").send_keys("root@grocery.com")
driver.find_element(By.ID, "password").send_keys("secret@123")

login_button = driver.find_element(By.CSS_SELECTOR, "button.loginButton")
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", login_button)
time.sleep(1)
print("✅ Logged in successfully")

# ---------- STEP 2: Product List ----------
products = [
    {
        "name": "Test Product 1",
        "desc": "This product was added automatically.",
        "unit": "kg",
        "buy_price": "100",
        "price": "150",
        "discount_price": "10",
        "quantity": "50",
        "min_order": "1",
        "image_id": "7"
    },
    {
        "name": "Test Product 2",
        "desc": "Added using Selenium automation script.",
        "unit": "pcs",
        "buy_price": "200",
        "price": "260",
        "discount_price": "15",
        "quantity": "30",
        "min_order": "2",
        "image_id": "3"
    }
]

# ---------- HELPER FUNCTION: Open Menu Once ----------
def open_product_menu_once():
    try:
        submenu_visible = driver.find_elements(By.XPATH, "//div[@id='productMenu']//a[contains(@href, '/shop/product/create')]")
        if submenu_visible:
            print("📂 Product Management menu already expanded")
            return
        product_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Product Management']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", product_menu)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", product_menu)
        time.sleep(1)
        print("📦 Clicked Product Management menu")
    except Exception as e:
        print("⚠️ Failed to expand product menu:", e)

# ---------- FUNCTION: Add Product ----------
def add_product(product):
    try:
        # ---------- STEP 3: Go to Add Product ----------
        try:
            add_product_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='productMenu']//a[contains(@href, '/shop/product/create')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", add_product_btn)
            driver.execute_script("arguments[0].click();", add_product_btn)
            print("🧾 Opened Add Product page successfully! (via href)")
        except:
            print("⚠️ First try failed, trying fallback locator...")
            add_product_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='productMenu']//a[contains(., 'Add Product')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", add_product_btn)
            driver.execute_script("arguments[0].click();", add_product_btn)
            print("🧾 Opened Add Product page successfully! (via text)")

        time.sleep(2)

        # ---------- STEP 4: Fill Product Form ----------
        driver.find_element(By.ID, "product_name").send_keys(product["name"])
        driver.find_element(By.NAME, "short_description").send_keys(product["desc"])
        print(f"✍️ Filling info for {product['name']}")

        # ---------- Generate AI Description (optional) ----------
        try:
            generate_ai_btn = driver.find_element(By.ID, "generateAi")
            generate_ai_btn.click()
            print("⚙️ Clicked Generate AI button")
            time.sleep(65)
        except:
            print("⚠️ Generate AI button not found, skipping...")

        # ---------- Unit ----------
        driver.find_element(By.ID, "unit").send_keys(product["unit"])

        # ---------- SKU Generate ----------
        try:
            generate_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//label[contains(., 'Generate Code')]//span[contains(@onclick, 'generateCode')]")
                )
            )
            driver.execute_script("arguments[0].click();", generate_code)
            print("✅ Product SKU generated successfully")
        except:
            print("⚠️ Could not generate SKU")

        # ---------- Prices ----------
        driver.find_element(By.ID, "buy_price").send_keys(product["buy_price"])
        driver.find_element(By.ID, "price").send_keys(product["price"])
        driver.find_element(By.ID, "discount_price").send_keys(product["discount_price"])
        driver.find_element(By.ID, "quantity").send_keys(product["quantity"])
        driver.find_element(By.ID, "min_order_quantity").send_keys(product["min_order"])
        print("💰 Filled pricing and quantity details")

        # ---------- Category ----------
        try:
            category_checkbox = driver.find_element(By.ID, "category_2")
            driver.execute_script("arguments[0].click();", category_checkbox)
            print("🍎 Selected category: Fruits")
        except:
            print("⚠️ Category not found, skipping...")

        # ---------- Upload Thumbnail ----------
        try:
            thumb_label = driver.find_element(By.CSS_SELECTOR, "label.mainThumbnail")
            driver.execute_script("arguments[0].click();", thumb_label)
            print("🖼️ Opened image upload modal")

            time.sleep(3)
            driver.switch_to.frame("lfmIframe")
            print("🔄 Switched to image frame")

            image_to_select = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"div.gridCart[data-id='{product.get('image_id', '2')}']"))
            )
            image_to_select.click()
            print("📸 Selected an image")

            time.sleep(2)
            confirm_button = driver.find_element(By.XPATH, "//nav[@id='actions']//a[@data-action='use']")
            confirm_button.click()
            print("✅ Clicked Confirm button successfully")

            driver.switch_to.default_content()
            print("⬅️ Returned to main admin page")
        except Exception as e:
            print("⚠️ Thumbnail upload skipped:", e)

        # ---------- Submit ----------
        submit_btn = driver.find_element(By.XPATH, "//button[contains(.,'Submit') or contains(.,'Save')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", submit_btn)
        print("📤 Submitted the product")

        # ---------- Verify ----------
        time.sleep(3)
        if "products" in driver.current_url:
            print(f"🎉 '{product['name']}' added successfully!\n")
        else:
            print(f"❌ Something went wrong while adding '{product['name']}'\n")

    except Exception as e:
        print(f"⚠️ Error adding product {product['name']}: {e}")

# ---------- STEP 3: Open Menu Once & Add All Products ----------
open_product_menu_once()

for p in products:
    add_product(p)

# ---------- Close Browser ----------
driver.quit()
print("✅ All products processed successfully!")
