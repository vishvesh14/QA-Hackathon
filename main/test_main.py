__author__ = 'Vishvesh Savant'

import pytest
from selenium import webdriver
from element_locators.locators import PageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from element_events.events import EventFunctions
import pytest


driver = webdriver.Firefox()
event_object = EventFunctions()
driver.get("http://www.automationpractice.com/index.php")
assert "My Store" in driver.title
driver.maximize_window()

#@pytest.mark.registration
'''def test_user_registration(driver):
    event_object.initial(driver)
    event_object.registation(driver)
    event_object.click_create_account_button(driver)'''

#@pytest.mark.login
def test_user_login(driver):
    event_object.valid_login(driver)

test_user_login(driver)


