from selenium import webdriver
import  time

url = 'https://www.codewars.com'

EMAIL= 'pytechdrae@gmail.com'
PASSWORD = 'O603023626x'

def accessCodeWars(url,user_email=EMAIL,password=PASSWORD):
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url)

    login_button = browser.find_element_by_css_selector('#header_section > ul > li:nth-child(3) > a')
    login_button.click()    
    time.sleep(3)
    
    email_box = browser.find_element_by_css_selector('#user_email')
    email_box.click()
    email_box.send_keys(user_email)

    password_box = browser.find_element_by_css_selector('#user_password')
    password_box.click()
    password_box.send_keys(password)        

    password_box.submit()

accessCodeWars(url)