from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
print("Google opened")

time.sleep(2)

# Search in Google
search = driver.find_element(By.NAME, "q")
search.send_keys("Python Selenium")
search.submit()

print("Search completed")

time.sleep(3)

# Open Books to Scrape
driver.get("http://books.toscrape.com/")
print("Books website opened")

time.sleep(2)

# Refresh page
driver.refresh()
print("Page refreshed")

time.sleep(2)

# Click Travel category
travel = driver.find_element(By.LINK_TEXT, "Travel")
travel.click()

print("Travel category opened")

time.sleep(2)

# Print first few book titles
books = driver.find_elements(By.CLASS_NAME, "product_pod")

print("Book Names")

for book in books[:5]:
    title = book.find_element(By.TAG_NAME, "h3")
    print(title.text)

time.sleep(2)

# XPath example
price = driver.find_element(By.XPATH, "//p[@class='price_color']")
print("First Book Price:", price.text)

time.sleep(3)

driver.quit()

print("Browser Closed")
