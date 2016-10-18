__author__ = 'Vishvesh Savant'

import pytest
from selenium import webdriver
from module.Registration import CreateAccountElements
from module.Login import LoginModule
from locators.locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
def User_Registration():
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    elem=driver.find_element(*MainPageLocators.Sign_In)
    elem.click()
    driver.maximize_window()
    '''RegistrationObject = CreateAccountElements()
    RegistrationObject.Elements(driver)
    RegistrationObject.ClickCreateAccountButton(driver)'''

    '''LoginObject = LoginModule()
    LoginObject.login_elements(driver)'''


driver=User_Registration()

