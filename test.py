__author__ = 'Vishvesh Savant'

from selenium import webdriver
import pytest


def Registration():
    driver = webdriver.Firefox()
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    driver.maximize_window()

def login():
    driver = webdriver.Firefox()
    driver.get("http://automationpractice.com/index.php")
    assert "My Store" in driver.title
    driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    driver.maximize_window()

@pytest.mark.slow
def test_Registration():
    Registration()

@pytest.mark.fast
def test_login():
    login()
