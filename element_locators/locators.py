__author__ = 'Vishvesh Savant'

from selenium import webdriver
from selenium.webdriver.common.by import By


class PageLocators(object):

    def main_page_locators(self):
        sign_in= (By.CLASS_NAME,'login')

    def registration_page_locators(self):
        title_radio_buttons=(By.ID,'id_gender1')
        first_name=(By.ID,'customer_firstname')
        last_name=(By.ID,'customer_lastname')
        password=(By.CLASS_NAME,'is_required validate form-control')
        first_name_address=(By.ID,'firstname')
        last_name_address=(By.ID,'lastname')



