import pytest
from locators import main_page as loc
from selenium.webdriver.support.ui import Select
from Generator import Data_generator as dg


@pytest.mark.usefixtures('setup')
def test_sing_in_negative():
    pytest.driver.get('http://automationpractice.com/index.php')
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    auth_label = pytest.driver.find_element_by_css_selector(loc.accountform_header())
    assert auth_label.text == "CREATE AN ACCOUNT"
    pytest.driver.find_element_by_name(loc.email_field()).send_keys("asd")
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    element = pytest.driver.find_element_by_css_selector(loc.invalidEmail_error())
    assert element.text == "Invalid email address."


@pytest.mark.usefixtures('setup')
def test_sing_in_negative2():
    pytest.driver.get('http://automationpractice.com/index.php')
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    pytest.driver.find_element_by_name(loc.email_field()).send_keys("asd2@asd.pl")
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    reg_form_label = pytest.driver.find_element_by_css_selector(loc.registration_form())
    assert reg_form_label.text == "YOUR PERSONAL INFORMATION"
    pytest.driver.find_element_by_id(loc.register_button()).click()
    error = pytest.driver.find_element_by_css_selector(loc.registration_error())
    assert error.text == 'There are 8 errors'


@pytest.mark.usefixtures('setup')
def test_sing_in_negative3():
    pytest.driver.get('http://automationpractice.com/index.php')
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    pytest.driver.find_element_by_name(loc.email_field()).send_keys("mobiy43402@cityroyal.org")
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    error = pytest.driver.find_element_by_css_selector(loc.createAccount_error())
    assert error.text == 'An account using this email address has already been registered. Please enter a valid password or request a new one.'


@pytest.mark.usefixtures('setup')
def test_sing_in_positive():
    pytest.driver.get('http://automationpractice.com/index.php')
    pytest.driver.find_element_by_class_name(loc.signin_button()).click()
    pytest.driver.find_element_by_name(loc.email_field()).send_keys(dg.generate_email(ptf=False))
    pytest.driver.find_element_by_css_selector(loc.createAccount_button()).click()
    pytest.driver.find_element_by_id(loc.radio_button_title()).click()
    pytest.driver.find_element_by_name(loc.input_customer_firstname()).send_keys("John")
    pytest.driver.find_element_by_name(loc.input_customer_lastname()).send_keys("Doe")
    pytest.driver.find_element_by_name(loc.input_password()).send_keys("XDWZP8123")
    pytest.driver.find_element_by_name(loc.input_firstname()).send_keys("John")
    pytest.driver.find_element_by_name(loc.input_lastname()).send_keys("Doe")
    pytest.driver.find_element_by_name(loc.input_address()).send_keys("Westeria Lane")
    pytest.driver.find_element_by_name(loc.input_city()).send_keys("Denver")
    dropdown = Select(pytest.driver.find_element_by_id(loc.dropdown_state()))
    dropdown.select_by_index(6)
    pytest.driver.find_element_by_name(loc.input_zipcode()).send_keys("90210")
    pytest.driver.find_element_by_name(loc.input_mobile()).send_keys("8588489004")
    pytest.driver.find_element_by_id(loc.register_button()).click()
    my_account = pytest.driver.find_element_by_css_selector(loc.account_page())
    assert my_account.text == 'MY ACCOUNT'

