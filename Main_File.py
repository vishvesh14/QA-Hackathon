__author__ = 'Vishvesh Savant'

import time
from selenium import webdriver
from ElementLocators import CreateAccountElements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
def First():
    #driver = webdriver.Firefox()
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    driver.maximize_window()
    obj1 = CreateAccountElements()
    obj1.Elements()
    obj1.ClickCreateAccountButton()

First()

