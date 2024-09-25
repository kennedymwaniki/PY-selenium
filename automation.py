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
chrome_browser.get('https://www.udemy.com')

# Check if 'Development' exists in the categories list
categories = chrome_browser.find_elements(
    By.CLASS_NAME, 'carousel-module--scroll-item--QZoY7')
# print('Web Development' in [category.text for category in categories])


assert "Udemy" in chrome_browser.page_source
# Print the title of the current page
print(chrome_browser.title)

# Test to ensure it's working
print(chrome_browser)


# Close the browser after finishing
chrome_browser.quit()
