from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)

prise = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

button = browser.find_element(By.CSS_SELECTOR, '[id="book"]')
button.click()

def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))

x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
num = x.get_attribute('innerHTML')

res = calc(num)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(res)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()

time.sleep(12)