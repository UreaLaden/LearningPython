#! python 3
from selenium import webdriver as wd
import pyautogui ,time

def googleIt():
    keyphrase = input('What are you looking for? ' )
    url = 'https://www.google.com'
    driver = wd.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(url)
    time.sleep(1.25)
    searchBar = driver.find_element_by_name('q').send_keys(keyphrase)
    time.sleep(1.25)
    driver.find_element_by_name('btnK').click()

googleIt()

