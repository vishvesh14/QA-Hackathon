__author__ = 'Vishvesh Savant'

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class CreateAccountElements(object):

    def Elements(self, driver):
        Email_Address= driver.find_element_by_xpath(".//*[@id='email_create']")
        Email_Address.clear()
        Email_Address.send_keys("amdv1991@gmail.com")

    def ClickCreateAccountButton(self, driver):
        driver.find_element_by_xpath(".//*[@id='SubmitCreate']").click()