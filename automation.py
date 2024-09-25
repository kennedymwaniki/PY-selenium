from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#  try out selenium easy website


# Path to your chromedriver.exe
chrome_service = Service('./chromedriver.exe')

# Create a WebDriver instance
chrome_browser = webdriver.Chrome(service=chrome_service)

# Maximize the browser window
chrome_browser.maximize_window()

chrome_browser.get('https://www.google.com')

# Print the title of the current page
print(chrome_browser.title)


# Test to ensure it's working
print(chrome_browser)
