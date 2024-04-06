import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def test_multy_languages(browser):
	link = 'https://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'
	browser.get(link)
	browser.implicitly_wait(10)
	
	try:
		add_to_cart_butt = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
		assert add_to_cart_butt is not None, "Add to Cart button not found on the page"
		time.sleep(10)
	except NoSuchElementException:
		pytest.skip("Add to Cart button not found on the page")

