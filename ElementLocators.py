__author__ = 'Vishvesh Savant'

from Main_File import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class CreateAccountElements:

    def Elements(self):
        Email_Address= driver.find_element_by_xpath(".//*[@id='email_create']")
        Email_Address.clear()
        Email_Address.send_keys("amdv1991@gmail.com")

    def ClickCreateAccountButton(self):
        driver.find_element_by_xpath(".//*[@id='SubmitCreate']").click()