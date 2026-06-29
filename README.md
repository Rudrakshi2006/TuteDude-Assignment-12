# Selenium Automation Using Python

**Automation using Selenium – Getting Data**

## Objective

The objective of this assignment is to automate web browser actions using Selenium WebDriver in Python. The program demonstrates opening web pages, searching for products, locating web elements using different locator strategies, extracting data from a webpage, refreshing pages, and closing the browser.

---

## Features

* Launches Google Chrome using Selenium WebDriver
* Opens Google and Amazon websites
* Maximizes the browser window
* Performs Google search using `send_keys()`
* Opens Amazon website
* Refreshes the web page
* Searches for a product on Amazon
* Locates elements using:

  * `By.NAME`
  * `By.ID`
  * `By.CLASS_NAME`
  * `By.LINK_TEXT`
  * `By.XPATH`
* Extracts multiple product titles using `find_elements()`
* Displays extracted data in the terminal
* Closes the browser using `driver.quit()`

---

## Technologies Used

* Python 3.x
* Selenium WebDriver
* Google Chrome

---

## Prerequisites

Before running the project, install the following:

* Python 3.x
* Google Chrome browser
* Selenium library

Install Selenium using:

```bash
pip install selenium
```

---

## Project Structure

```
SeleniumAutomation/
│
├── automation.py
├── README.md
└── requirements.txt
```

---

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Install Selenium (if not already installed):

```bash
pip install selenium
```

4. Run the program:

```bash
python automation.py
```

---

## Expected Output

The program will:

* Open Google Chrome.
* Navigate to Google.
* Search for **Amazon India**.
* Open Amazon.
* Refresh the page.
* Search for **Laptop**.
* Extract and display product titles in the terminal.
* Navigate to **Today's Deals** (if available).
* Demonstrate locating an element using XPath.
* Close the browser successfully.

Example console output:

```
Google opened successfully.
Google Search Completed.
Amazon website opened.
Amazon page refreshed.
Laptop search completed.

Top Product Titles:

1. HP Laptop
2. Lenovo IdeaPad
3. Dell Inspiron
4. ASUS Vivobook
5. Acer Aspire

Today's Deals page opened.

XPath Example Successful

Browser Closed Successfully.
```

*(The displayed product titles may vary depending on Amazon's current listings.)*

---

## Selenium Concepts Demonstrated

* `webdriver.Chrome()`
* `driver.get()`
* `driver.maximize_window()`
* `find_element()`
* `find_elements()`
* `By.NAME`
* `By.ID`
* `By.CLASS_NAME`
* `By.LINK_TEXT`
* `By.XPATH`
* `send_keys()`
* `click()`
* `time.sleep()`
* `driver.refresh()`
* `driver.quit()`

---

## Conclusion

This project demonstrates the basics of browser automation using Selenium WebDriver with Python. It covers browser navigation, searching, locating web elements using different locator strategies, extracting webpage data, refreshing pages, and automating user interactions. It serves as a foundation for web automation and web scraping projects.
