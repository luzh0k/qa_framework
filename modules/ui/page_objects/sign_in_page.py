from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Searching the login field for filling with incorrect data (wrong login or e-mail)
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Set incorrect login or e-mail
        login_elem.send_keys(username)

        # Finding the password field for filling with incorrect data 
        pass_elem = self.driver.find_element(By.ID, "password")

        # Set incorrect password
        pass_elem.send_keys(password)

        # Searching the Sign-in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Press the button "Sign in"
        btn_elem.click()

    def check_title(self, expected_title):

        #Check that page title as expected 
        return self.driver.title == expected_title
    
    def check_alert_appearing(self):
        # Check that element of js-flsah-alert -class is on the Page
        return self.driver.find_element(By.CLASS_NAME, "js-flash-alert")
        