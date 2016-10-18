__author__ = 'Vishvesh Savant'

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import csv

class CreateAccountElements(object):
    self = ""
    def __init__(self):
        print(self)

    def Elements(self,driver):
        self.Email_Address= driver.find_element_by_xpath(".//*[@id='email_create']")
        self.Email_Address.clear()

        #using Content Manager to open CSV
        with open('Registration_Details.csv') as csvfile:                    #Calling CSV file with name "Registration_Details"
            self.filecontent = csv.reader(csvfile,delimiter=',')
            self.emailaddress =[]                                       #Creating empty list to store value after append in for loop

            for row in self.filecontent:
                user_email=row[0]
                self.emailaddress.append(user_email)

        self.Email_Address.send_keys(self.emailaddress)
        print(self.emailaddress)

    def ClickCreateAccountButton(self,driver):
        driver.find_element_by_xpath(".//*[@id='SubmitCreate']").click()