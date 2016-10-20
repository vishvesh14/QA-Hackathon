__author__ = 'Vishvesh Savant'

from selenium import webdriver
from element_locators.locators import PageLocators
import csv

class Event_Functions(object):

    def initial(self, driver):
        elem=PageLocators()
        signin = elem.main_page_locators()
        elem=driver.find_element(signin.sign_in)
        elem.click()
        driver.maximize_window()

    def registation(self, driver):
        email_address_object= PageLocators()
        a = email_address_object.registration_page_locators()
        email_address_object = driver.find_element_(*a.email_address)
        email_address_object.clear()
        with open("C:/Users/Vishvesh Savant/Desktop/QA-Hackathon1/module/Registration_Details.csv") as csvfile:
            filecontent = csv.reader(csvfile,delimiter=',')
            emailaddress =[]
            for row in filecontent:
                user_email=row[0]
                emailaddress.append(user_email)
        email_address_object.send_keys(emailaddress)
        print(emailaddress)

    def click_create_account_button(self,driver):
        self.create_account_object=PageLocators
        self.create_account_object.registration_page_locators()
        self.create_account_object=driver.find_element(*self.create_account_object.create_account_button)
        self.create_account_object.click()