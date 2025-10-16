# add_multi_product_googlesheet_updated.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

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
time.sleep(2)
print("✅ Logged in successfully")

# ---------- STEP 2: Load Products from CSV ----------
products = []
with open("products.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        products.append(row)

print(f"📦 Loaded {len(products)} products from CSV file.")

# ---------- FUNCTION: Add Product ----------
def add_product(product):
    try:
        # ---------- Go to Add Product ----------
        product_menu = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Product Management']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", product_menu)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", product_menu)
        time.sleep(2)

        try:
            add_product_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='productMenu']//a[contains(@href, '/shop/product/create')]"))
            )
            driver.execute_script("arguments[0].click();", add_product_link)
        except:
            add_product_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='productMenu']//a[contains(., 'Add Product')]"))
            )
            driver.execute_script("arguments[0].click();", add_product_link)

        print(f"🧾 Navigated to Add Product page for '{product.get('name','Unnamed')}'")

        time.sleep(2)

        # ---------- Fill Product Info ----------
        driver.find_element(By.ID, "product_name").send_keys(product.get("name", ""))
        driver.find_element(By.NAME, "short_description").send_keys(product.get("desc", ""))
        print(f"✍️ Filling info for '{product.get('name','Unnamed')}'")

        # ---------- Description Field ----------
        description_text = product.get("description", "").strip()
        if description_text:
            try:
                editor = WebDriverWait(driver, 15).until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@id='editor' and contains(@class,'ql-editor')]"))
                )
                driver.execute_script("arguments[0].innerHTML = arguments[1];", editor, description_text)
                print("📝 Filled Description from CSV")
            except Exception as e:
                print("⚠️ Could not fill Description field:", e)
        else:
            try:
                generate_ai_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "generateAi"))
                )
                driver.execute_script("arguments[0].click();", generate_ai_btn)
                print("⚙️ Clicked Generate AI button")
                time.sleep(5)
            except:
                print("⚠️ Generate AI button not found, skipping...")

        # ---------- Unit ----------
        driver.find_element(By.ID, "unit").send_keys(product.get("unit",""))

        # ---------- SKU ----------
        try:
            generate_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(., 'Generate Code')]//span[contains(@onclick, 'generateCode')]"))
            )
            driver.execute_script("arguments[0].click();", generate_code)
            print("✅ SKU generated")
        except:
            print("⚠️ Could not generate SKU")

        # ---------- Prices ----------
        driver.find_element(By.ID, "buy_price").send_keys(product.get("buy_price",""))
        driver.find_element(By.ID, "price").send_keys(product.get("price",""))
        driver.find_element(By.ID, "discount_price").send_keys(product.get("discount_price",""))
        driver.find_element(By.ID, "quantity").send_keys(product.get("quantity",""))
        driver.find_element(By.ID, "min_order_quantity").send_keys(product.get("min_order",""))
        print("💰 Pricing and stock info filled")

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
            time.sleep(2)

            driver.switch_to.frame("lfmIframe")
            image_to_select = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"div.gridCart[data-id='{product.get('image_id','2')}']"))
            )
            image_to_select.click()
            time.sleep(1)
            confirm_button = driver.find_element(By.XPATH, "//nav[@id='actions']//a[@data-action='use']")
            confirm_button.click()
            driver.switch_to.default_content()
            print(f"🖼️ Selected image ID: {product.get('image_id','2')}")
        except Exception as e:
            print("⚠️ Thumbnail upload skipped:", e)

        # ---------- Submit ----------
        submit_btn = driver.find_element(By.XPATH, "//button[contains(.,'Submit') or contains(.,'Save')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        driver.execute_script("arguments[0].click();", submit_btn)
        print("📤 Submitted product")

        time.sleep(5)

        if "products" in driver.current_url:
            print(f"🎉 '{product.get('name','Unnamed')}' added successfully!\n")
        else:
            print(f"❌ Failed to add '{product.get('name','Unnamed')}'\n")

    except Exception as e:
        print(f"⚠️ Error adding '{product.get('name','Unnamed')}': {e}")

# ---------- STEP 3: Loop through products ----------
for p in products:
    add_product(p)

driver.quit()
print("✅ All products processed successfully!")
