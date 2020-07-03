from rotating_users import rotating_ua
from selenium import webdriver
from rotating_users import rotating_ua
import webbrowser, sys, pyperclip
import time

def open_amu():
    url = 'https://www.amu.apus.edu/index.htm'
    browser = webdriver.Firefox()
    browser.get(url)

    elem1 = browser.find_element_by_css_selector('#utilityLoginWrapper > div > div > span')
    elem2 = browser.find_element_by_css_selector('#login-links-desktop-wrapper > ul > li:nth-child(1) > a')
    elem1.click()
    elem2.click()
    time.sleep(3)

    userElem = browser.find_element_by_css_selector('#FormModel_Username')
    passElem = browser.find_element_by_css_selector('#FormModel_Password')
    userElem.send_keys('***This is your username***')
    passElem.send_keys('***This is your password***')
    passElem.submit()

open_amu()
