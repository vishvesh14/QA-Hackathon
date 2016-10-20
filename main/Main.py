__author__ = 'Vishvesh Savant'

import pytest
from selenium import webdriver
from module.Login import LoginModule
from element_locators.locators import PageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from element_events.events import Event_Functions


driver=webdriver.Firefox()
event_object=Event_Functions()
driver.get("http://automationpractice.com/index.php")
assert "My Store" in driver.title

def user_registration(driver):
    event_object.initial(driver)
    event_object.registation(driver)
    event_object.click_create_account_button(driver)

user_registration(driver)
