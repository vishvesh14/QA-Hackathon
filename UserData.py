__author__ = 'Vishvesh Savant'

import csv

class User(object):

    def userdataddt(self):
        with open('Emails.csv') as csvfile:
            filecontent = csv.reader(csvfile,delimiter=',')
            emailaddress =[]

            for row in filecontent:
                user_email=row[0]
                emailaddress.append(user_email)
