# You need to install selenium and python before running the script

# Import the necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Base Url for your application you want to test
base_url="https://www.flipkart.com"

# Provide the path for the chromedriver.exe file matching your system chrome version
driver = webdriver.Chrome("/home/ashish/Desktop/chromedriver")

# Maximize the chrome window
driver.maximize_window()

# Wait there are two types of waiting - implicit and explicit
driver.implicitly_wait(10)

# Open the url in browser
driver.get(base_url)

# Find the element in the current view of the page - there are multiple ways to find elements like by css attributes, id, namem, link etc.
driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()

# Find the inout field and enter the keyword to search
driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("Mobiles")
# Press ENTER to search
driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys(Keys.RETURN)

# Wait for some time to see results are shown
time.sleep(5)

# Close the driver/chrome window
driver.close()

