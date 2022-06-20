import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BOOK_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_shuld_be_add_to_basket_button(browser):
    browser.get(BOOK_PAGE_LINK)
    time.sleep(10) #allow to visual check selected language
    elements = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(elements) == 1, "No add to basket button"
