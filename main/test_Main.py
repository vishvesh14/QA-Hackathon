__author__ = 'Vishvesh Savant'

import pytest
from selenium import webdriver
from module.Registration import CreateAccountElements


def User_Registration(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://automationpractice.com/index.php")
    assert "My Store" in self.driver.title
    self.driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    self.driver.maximize_window()

    RegistrationObject = CreateAccountElements()
    RegistrationObject.Elements(self.driver)
    RegistrationObject.ClickCreateAccountButton(self.driver)

'''def User_Login(driver):
    LoginObject = LoginModule()
    LoginObject.login_elements(driver)'''
print("test")

#@pytest.mark.reg
#def test_Registration():
User_Registration()
