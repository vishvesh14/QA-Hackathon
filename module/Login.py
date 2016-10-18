__author__ = 'Vishvesh Savant'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import csv

class LoginModule(object):
    def login_elements(self,driver):

        with open('C:/Users/Vishvesh Savant/Desktop/QA-Hackathon1/module/Login_Details.csv') as csvfile:                    #Calling CSV file with name "Login_Details"
            self.filecontent = csv.reader(csvfile,delimiter=',')
            self.emailaddress =[]                                 #Creating empty list to store email address after append in for loop
            self.password=[]                                       #Creating empty list to store password after append in for loop

            for row in self.filecontent:
                user_email=row[0]
                user_password=row[1]
                self.emailaddress.append(user_email)
                self.password.append(user_password)

        self.Email_Address= driver.find_element_by_xpath(".//*[@id='email']")    #Email Address Field
        self.Email_Address.clear()
        self.Email_Address.send_keys(self.emailaddress)
        print(self.emailaddress)

        self.Email_Address= driver.find_element_by_xpath(".//*[@id='passwd']")
        self.Email_Address.clear()
        self.Email_Address.send_keys(self.password)
        print(self.password)
