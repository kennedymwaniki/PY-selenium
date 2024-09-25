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
email = chrome_browser.find_element(By.ID, 'form-group--1')
email.clear()
email.send_keys("Kennedymwaniki")
# Close the browser after finishing
# chrome_browser.quit()
