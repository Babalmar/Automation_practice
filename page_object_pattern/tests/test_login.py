import pytest
import allure
from assertpy import assert_that


@pytest.mark.usefixtures('setup')
@allure.parent_suite('Login')
@allure.description("Tests validating proper login behaviour")
class TestLogin:

    @allure.title('Login with invalid email address')
    def test_log_in_incorrect_email(self, setup):
        self.login.click_signin_btn()
        self.login.enter_credentials('asd', 'sddd')
        assert_that(self.login.display_email_alert()).contains('Invalid email address.')

    @allure.title('Login with invalid password')
    def test_log_in_incorrect_password(self, setup):
        self.login.click_signin_btn()
        self.login.enter_credentials('asd@sd.pl', 'sddd')
        assert_that(self.login.display_email_alert()).contains('Invalid password.')

    @allure.title('Login with valid email address / password')
    def test_log_in_valid_credentials(self, setup):
        self.login.click_signin_btn()
        self.login.enter_credentials('mobiy43403@cityroyal.org', 'qwerty123')
        assert_that(self.login.display_my_account()).contains('MY ACCOUNT')




