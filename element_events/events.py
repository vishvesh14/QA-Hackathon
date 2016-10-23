__author__ = 'Vishvesh Savant'

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from element_locators.locators import PageLocators,Login,Search
import csv

page_locator_object= PageLocators()
login_object = Login()
search_object = Search()

class EventFunctions(object):

    def initial(self,driver):
        page_locator_object.main_page_locators(driver)
        x = driver.find_element_by_xpath(".//*[@id='email_create']").click()
        x.clear()

    def valid_login(self,driver):
        login_object.login_locators(driver)

    def invalid_search(self,driver):
        search_object.search_locators(driver)
        print("test 1")
        x = "Please enter a search keyword"
        print("test 2")

        search_object.search_button_locators(driver)
        actual_search_message = driver.find_element_by_xpath(".//*[@id='center_column']/p").text
        print("test 3")
        assert("Please enter a search keyword" in actual_search_message)
        print("test pass")

'''
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
        self.create_account_object.click()'''