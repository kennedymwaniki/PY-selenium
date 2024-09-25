
#! DOCS FOR LEARNING
# * https://selenium-python.readthedocs.io/locating-elements.html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to your chromedriver.exe
chrome_service = Service('./chromedriver.exe')

# Create a WebDriver instance
chrome_browser = webdriver.Chrome(service=chrome_service)

# Maximize the browser window
chrome_browser.maximize_window()

# Navigate to Udemy
chrome_browser.get(
    'https://www.udemy.com/join/signup-popup/?locale=en_US&next=https%3A%2F%2Fwww.udemy.com%2F&response_type=html')


# getting inputs
name = chrome_browser.find_element(By.ID, 'form-group--1')
name.clear()
name.send_keys("Kennedy")

email = chrome_browser.find_element(By.ID, 'form-group--3')
email.clear()
email.send_keys("your email")

password = chrome_browser.find_element(By.ID, 'form-group--3')
password.clear()
password.send_keys("password")


# get button for signing up and simulate click
sign_up_button = chrome_browser.find_element(
    By.CLASS_NAME, 'ud-btn ud-btn-large ud-btn-brand ud-heading-md helpers--auth-submit-button--W3Tqk')

# click event
sign_up_button.click()
# Close the browser after finishing
# chrome_browser.quit()
