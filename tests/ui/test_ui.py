import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Creating the object for managing the browser
    driver = webdriver.Chrome(
        service = Service(r"/home/luzhok/GithubRepo/qa_framework/" + "chromedriver")
    )

    #open the page https://github.com/login
    driver.get("https://github.com/login")

    # Finding the login field for filling with incorrect data (wrong login or e-mail)
    login_elem = driver.find_element(By.ID, "login_field")

    # Set incorrect login or e-mail
    login_elem.send_keys("ksuLuzha@wrongemail.com")

    # Finding the password field for filling with incorrect data 
    pass_elem = driver.find_element(By.ID, "password")

    # Set incorrect password
    pass_elem.send_keys("paSSword1234")

    # Searching the Sign-in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # Press the button "Sign in"
    btn_elem.click()

    #Check that page title as expected
    assert driver.title == "Sign in to GitHub · GitHub"
    #time.sleep(3)

    #close the browser
    driver.close()