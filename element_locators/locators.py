__author__ = 'Vishvesh Savant'

from selenium import webdriver
from selenium.webdriver.common.by import By


class PageLocators(object):
    sign_in = (By.CLASS_NAME, 'login')

    def main_page_locators(self):
        sign_in=(By.CLASS_NAME,'login')

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




