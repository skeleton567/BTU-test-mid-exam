import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def browser():
    driver = webdriver.Chrome()  
    return driver

def test_registration():
    browser().get("https://magento.softwaretestingboard.com/customer/account/create/")

    first_name_input = browser().find_element(By.CSS_SELECTOR, "#firstname") 
    last_name_input = browser().find_element(By.CSS_SELECTOR, "#lastname") 
    email_input = browser().find_element(By.CSS_SELECTOR, "#email_address")
    password_input = browser().find_elementBy.CSS_SELECTOR, ("#password")
    confirm_password_input = browser().find_element(By.CSS_SELECTOR, "#password-confirmation")
    submit_button = browser().find_element(By.XPATH, "//*[@id='form-validate']/div/div[1]/button")
    
    def succes_message():
        return browser().find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div")
    
    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("password123Aa")
    confirm_password_input.send_keys("password123Aa")

    submit_button.click()

    assert "Thank you for registering with Main Website Store." in succes_message().text

def test_registration_failure():
    browser().get("https://magento.softwaretestingboard.com/customer/account/create/")

    first_name_input = browser().find_element(By.CSS_SELECTOR, "#firstname") 
    last_name_input = browser().find_element(By.CSS_SELECTOR, "#lastname") 
    email_input = browser().find_element(By.CSS_SELECTOR, "#email_address")
    password_input = browser().find_elementBy.CSS_SELECTOR, ("#password")
    confirm_password_input = browser().find_element(By.CSS_SELECTOR, "#password-confirmation")
   
    def error_message():
        return browser().find_element(By.SS_SELECTOR, "#password-error")
    
    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    email_input.send_keys("john.doe@example.com")
    password_input.send_keys("123")
    confirm_password_input.send_keys("123")

    assert "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored." in error_message().text