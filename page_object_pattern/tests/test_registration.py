import pytest
import allure
from assertpy import assert_that


@pytest.mark.usefixtures('setup')
@allure.parent_suite('Registration')
@allure.description("Tests validating proper handling of registration feature")
class TestRegistration:

    @pytest.mark.usefixtures('setup')
    def test_sing_in_negative(self, setup):
        self.registration.click_signin()
        assert_that(self.registration.check_label()).contains('CREATE AN ACCOUNT')
        self.registration.enter_invalid_mail()
        assert_that(self.registration.invalid_mail_error()).contains("Invalid email address.")

    @pytest.mark.usefixtures('setup')
    def test_sing_in_negative2(self, setup):
        self.registration.enter_email()
        assert_that(self.registration.registration_screen()).contains('YOUR PERSONAL INFORMATION')
        self.registration.register_account()
        assert_that(self.registration.registration_error()).contains('There are 8 errors')

    @pytest.mark.usefixtures('setup')
    def test_sing_in_negative3():
        self.driver.find_element_by_class_name(signin_button()).click()
        self.driver.find_element_by_name(email_field()).send_keys("mobiy43402@cityroyal.org")
        self.driver.find_element_by_css_selector(createAccount_button()).click()
        error = self.driver.find_element_by_css_selector(createAccount_error())
        assert error.text == 'An account using this email address has already been registered. Please enter a valid password or request a new one.'

    @pytest.mark.usefixtures('setup')
    def test_sing_in_positive():
        self.driver.find_element_by_class_name(signin_button()).click()
        self.driver.find_element_by_name(email_field()).send_keys(dg.generate_email(ptf=False))
        self.driver.find_element_by_css_selector(createAccount_button()).click()
        self.driver.find_element_by_id(radio_button_title()).click()
        self.driver.find_element_by_name(input_customer_firstname()).send_keys("John")
        self.driver.find_element_by_name(input_customer_lastname()).send_keys("Doe")
        self.driver.find_element_by_name(input_password()).send_keys("XDWZP8123")
        self.driver.find_element_by_name(input_firstname()).send_keys("John")
        self.driver.find_element_by_name(input_lastname()).send_keys("Doe")
        self.driver.find_element_by_name(input_address()).send_keys("Westeria Lane")
        self.driver.find_element_by_name(input_city()).send_keys("Denver")
        dropdown = Select(self.driver.find_element_by_id(dropdown_state()))
        dropdown.select_by_index(6)
        self.driver.find_element_by_name(input_zipcode()).send_keys("90210")
        self.driver.find_element_by_name(input_mobile()).send_keys("8588489004")
        self.driver.find_element_by_id(register_button()).click()
        my_account = self.driver.find_element_by_css_selector(account_page())
        assert my_account.text == 'MY ACCOUNT'

