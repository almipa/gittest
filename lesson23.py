from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element(By.ID, 'book')
    button.click()

    
    x_elt = browser.find_element(By.ID, 'input_value')
    x = x_elt.text
    y = calc(x) 

    input_elt = browser.find_element(By.ID, 'answer')
    input_elt.send_keys(str(y))

    button = browser.find_element(By.ID, 'solve')
    button.click()

    time.sleep(1)


finally:
    time.sleep(5)
    browser.quit()


