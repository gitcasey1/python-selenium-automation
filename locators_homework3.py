from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

# Amazon logo:
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# Create account:
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Your name field:
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

# Email field:
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# Password field:
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# "Passwords must be at least 6 characters" text:
driver.find_element(By.CSS_SELECTOR, "div.a-box.a-alert-inline.a-alert-inline-info")

# Re-enter password field:
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

# "Create your Amazon account" or "Continue" button:
driver.find_element(By.CSS_SELECTOR, "#continue")

# "Conditions of Use" link:
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# "Privacy Notice" link:
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# "Sign in" link:
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid']")