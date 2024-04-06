import pytest
from selenium.webdriver.common.by import By
import time


def test_en_lang(browser):
	link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	browser.get(link)
	browser.implicitly_wait(10)

	browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
	time.sleep(3)
	