import pytest
import allure
from assertpy import assert_that
from page_object_pattern.pages.registration import Registration


@pytest.mark.usefixtures('setup')
@allure.parent_suite('Registration')
@allure.description("Tests validating proper handling of registration feature")
class TestRegistration:

    @allure.title('Register account - negative (invalid email address)')
    def test_sing_in_negative(self, setup):
        self.registration.click_signin()
        self.registration.enter_email('asd')
        self.registration.create_account()
        assert_that(self.registration.invalid_mail_error()).contains("Invalid email address.")

    @allure.title('Register account - negative (mandatory fields not populated)')
    def test_sing_in_negative2(self, setup):
        self.registration.click_signin()
        self.registration.enter_email('asd2@asd.pl')
        self.registration.create_account()
        self.registration.register_account()
        assert_that(self.registration.registration_error()).contains('There are 8 errors')

    @allure.title('Register account - negative (existing account)')
    def test_sing_in_negative3(self, setup):
        self.registration.click_signin()
        self.registration.enter_email('mobiy43402@cityroyal.org')
        self.registration.create_account()
        assert_that(self.registration.exisiting_account_error()).contains('An account using this email address has '
                                                                          'already been registered. Please enter a '
                                                                          'valid password or request a new one.')

    @allure.title('Register account - positive')
    def test_sing_in_positive(self, setup):
        self.registration.click_signin()
        self.registration.enter_email(Registration.random_mail())
        self.registration.create_account()
        self.registration.populate_registration_form()
        self.registration.register_account()
        assert_that(self.registration.account_landing_page()).contains('MY ACCOUNT')

