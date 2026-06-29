from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -----------------------------
# Create Chrome WebDriver
# -----------------------------
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

try:
    # -----------------------------
    # Open Google
    # -----------------------------
    driver.get("https://www.google.com")
    print("Google opened successfully.")

    time.sleep(2)

    # -----------------------------
    # Search on Google (By.NAME)
    # -----------------------------
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Amazon India")
    search_box.submit()

    print("Google Search Completed.")

    time.sleep(3)

    # -----------------------------
    # Open Amazon directly
    # -----------------------------
    driver.get("https://www.amazon.in")
    print("Amazon website opened.")

    time.sleep(3)

    # -----------------------------
    # Refresh Page
    # -----------------------------
    driver.refresh()
    print("Amazon page refreshed.")

    time.sleep(2)

    # -----------------------------
    # Search Product (By.ID)
    # -----------------------------
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("Laptop")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    print("Laptop search completed.")

    time.sleep(4)

    # -----------------------------
    # Extract Product Titles
    # (find_elements + CLASS_NAME)
    # -----------------------------
    products = driver.find_elements(By.CLASS_NAME, "a-size-medium")

    print("\nTop Product Titles:\n")

    count = 0
    for product in products:
        title = product.text.strip()
        if title:
            count += 1
            print(f"{count}. {title}")
        if count == 10:
            break

    if count == 0:
        print("No product titles found.")

    time.sleep(2)

    # -----------------------------
    # Click Today's Deals
    # (LINK_TEXT)
    # -----------------------------
    driver.get("https://www.amazon.in")

    time.sleep(3)

    try:
        deals = driver.find_element(By.LINK_TEXT, "Today's Deals")
        deals.click()
        print("\nToday's Deals page opened.")
    except:
        print("\n'Today's Deals' link not found.")

    time.sleep(3)

    # -----------------------------
    # Find element using XPath
    # -----------------------------
    try:
        logo = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
        print("\nXPath Example Successful")
        print("Logo Text:", logo.get_attribute("aria-label"))
    except:
        print("\nXPath element not found.")

    time.sleep(2)

finally:
    # -----------------------------
    # Close Browser
    # -----------------------------
    driver.quit()
    print("\nBrowser Closed Successfully.")