import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def browser():
    driver = webdriver.Chrome()  
    return driver

def test_auth():
    browser().get("https://magento.softwaretestingboard.com/customer/account/login")

    email_input = browser().find_element(By.CSS_SELECTOR, "#email")
    password_input = browser().find_element(By.CSS_SELECTOR, "#pass") 
    submit_button = browser().find_element(By.CSS_SELECTOR, "#send2")
    
    def user_name():
        return browser().find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span")
    
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("password123Aa")

    submit_button.click()

    assert "Welcome, John Doe!" in user_name().text

def test_auth_failure():
    browser().get("https://magento.softwaretestingboard.com/customer/account/login")

    email_input = browser().find_element(By.CSS_SELECTOR, "#email")
    password_input = browser().find_element(By.CSS_SELECTOR, "#pass") 
    submit_button = browser().find_element(By.CSS_SELECTOR, "#send2")
    
    def error_message():
        return browser().find_element(By.CSS_SELECTOR, "#email-error")
    
    email_input.send_keys("john")
    password_input.send_keys("password123Aa")

    submit_button.click()

    assert "Please enter a valid email address (Ex: johndoe@domain.com)." in error_message().text