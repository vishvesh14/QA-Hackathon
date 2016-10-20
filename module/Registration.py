__author__ = 'Vishvesh Savant'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from element_locators.locators import PageLocators
import csv
'''
class CreateAccountElements(object):

    def Elements(self,driver):
        email_address_object= PageLocators
        email_address_object.registration_page_locators()
        email_address_object = driver.find_element_(*email_address_object.email_address)
        self.Email_Address.clear()

        with open("C:/Users/Vishvesh Savant/Desktop/QA-Hackathon1/module/Registration_Details.csv") as csvfile:
            self.filecontent = csv.reader(csvfile,delimiter=',')
            self.emailaddress =[]

            for row in self.filecontent:
                user_email=row[0]
                self.emailaddress.append(user_email)

        self.Email_Address.send_keys(self.emailaddress)
        print(self.emailaddress)

    def ClickCreateAccountButton(self,driver):
        create_account_object=PageLocators
        create_account_object.registration_page_locators()
        create_account_object = driver.find_element(*create_account_object.create_account_button)
        create_account_object.click()'''