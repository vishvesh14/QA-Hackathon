__author__ = 'Vishvesh Savant'

import pytest
from selenium import webdriver
from module.Registration import CreateAccountElements
from module.Login import LoginModule
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def User_Registration(self,driver):
    driver = webdriver.Firefox()
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    driver.maximize_window()
    RegistrationObject = CreateAccountElements()
    RegistrationObject.Elements(driver)
    RegistrationObject.ClickCreateAccountButton(driver)

'''def User_Login(driver):
    LoginObject = LoginModule()
    LoginObject.login_elements(driver)'''


#@pytest.mark.reg
def test_Registration():
    User_Registration()
