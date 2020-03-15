import pytest
from locators import main_page as loc
from Generator import Data_generator as dg


@pytest.mark.usefixtures('setup')
def test_log_in_negative():
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    auth_label = pytest.driver.find_element_by_css_selector(loc.loginform_header())
    assert auth_label.text == "ALREADY REGISTERED?"
    pytest.driver.find_element_by_id(loc.registered_email()).send_keys("avcdf")
    pytest.driver.find_element_by_id(loc.registered_passwd()).send_keys("asd12")
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    email_alert = pytest.driver.find_element_by_css_selector(".alert.alert-danger li")
    assert email_alert.text == "Invalid email address."

@pytest.mark.usefixtures('setup')
def test_log_in_positive():
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    auth_label = pytest.driver.find_element_by_css_selector(loc.loginform_header())
    assert auth_label.text == "ALREADY REGISTERED?"
    pytest.driver.find_element_by_id(loc.registered_email()).send_keys('mobiy43403@cityroyal.org')
    pytest.driver.find_element_by_id(loc.registered_passwd()).send_keys('qwerty123')
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    my_account = pytest.driver.find_element_by_css_selector(loc.account_page())
    assert my_account.text == 'MY ACCOUNT'


