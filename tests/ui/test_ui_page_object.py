from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    #create the object of SignInPage class
    sign_in_page = SignInPage()

    # open the login page
    sign_in_page.go_to()

    # try to sign in ti Github
    sign_in_page.try_login("incorrectUsername@shmail.com", "IncorrectPass")

    # check that page title as expected
    sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close the browser
    sign_in_page.close()
