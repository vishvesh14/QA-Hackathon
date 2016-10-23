__author__ = 'Vishvesh Savant'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import csv


class PageLocators(object):
    sign_in = (By.CLASS_NAME,'login')

    def main_page_locators(self,driver):
        elem = PageLocators()
        elem = driver.find_element(*elem.sign_in)
        elem.click()

#Login Functionality
class Login(object):
    sign_in1 = (By.CLASS_NAME,'login')
    login_email = (By.ID,'email')
    login_password = (By.ID,'passwd')
    sign_in_button = (By.ID,'SubmitLogin')
    sign_out_button =(By.CLASS_NAME,'logout')

    def login_locators(self,driver):
        #Sign In Link on Homepage
        elem_sign_in = Login()
        elem_sign_in = driver.find_element(*elem_sign_in.sign_in1)
        elem_sign_in.click()

        #Email Address to Login
        elem_sign_in1 = Login()
        elem_sign_in1 = driver.find_element(*elem_sign_in1.login_email)
        elem_sign_in1.clear()
        print("test 1")

        #Password to login
        elem_sign_in2 = Login()
        elem_sign_in2 = driver.find_element(*elem_sign_in2.login_password)
        elem_sign_in2.clear()
        print("test 2")


        with open("C:/Users/Vishvesh Savant/Desktop/QA-Hackathon1/element_events/Login_Details.csv") as csvfile:
            login_file_content = csv.reader(csvfile,delimiter=",")
            login_email_address = []
            login_email_password = []
            for row in login_file_content:
                user_email = row[0]
                user_password = row[1]
            login_email_address.append(user_email)
            login_email_password.append(user_password)
            print("test 3")
            elem_sign_in1.send_keys(login_email_address)
            elem_sign_in2.send_keys(login_email_password)
            print("test 4")

        elem_sign_in3 = Login()
        elem_sign_in3 = driver.find_element(*elem_sign_in3.sign_in_button)
        elem_sign_in3.click()
        print("test 5")

        #Click on Sign Out Button
        elem_sign_in4 = Login()
        elem_sign_in4 = driver.find_element(*elem_sign_in4.sign_out_button)
        elem_sign_in4.click()
        print("test 6")

class registration_page_locators(object):
    email_address=(By.ID,'email_create')
    create_account_button=(By.ID,'SubmitCreate')
    title_radio_buttons=(By.ID,'id_gender1')
    first_name=(By.ID,'customer_firstname')
    last_name=(By.ID,'customer_lastname')
    password=(By.CLASS_NAME,'is_required validate form-control')
    first_name_address=(By.ID,'firstname')
    last_name_address=(By.ID,'lastname')
    address=(By.ID,'address1')

    def click_on_email_address(self, driver):
        driver.find_element(self.email_address).click()




