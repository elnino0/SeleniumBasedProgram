# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


targetLink = "http://4surfers.co.il/#/"
# Google Chrome
driver = webdriver.Chrome()
# Go to bitly
driver.get('https://bitly.com/')
linkShorterTextBox = driver.find_elements_by_id("shorten_url")[0]
linkShorterTextBox.send_keys(targetLink)
time.sleep(3)
driver.find_elements_by_id('shorten_btn')[0].click()

shortenUrlResolt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='short-url']")))
shortUrl = shortenUrlResolt.get_attribute('href')
print("short url ",shortUrl)
driver.get(shortUrl)
assert "<head>" in driver.page_source
assert "</head>" in driver.page_source
assert "<body" in driver.page_source
assert "</body>" in driver.page_source
assert "Images/Logo/share_site_sqaure.png" in driver.page_source
assert targetLink == driver.current_url

# Close the browser!
driver.quit()