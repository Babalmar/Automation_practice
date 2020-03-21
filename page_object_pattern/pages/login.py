class Login:
    def __init__(self, driver):
        self.driver = driver
        self.registered_email_css = '#email'
        self.registered_passwd_css = '#passwd'
        self.email_alert_css = '.alert.alert-danger li'
        self.sign_in_btn_css = '.login'
        self.log_in_btn_css = '#SubmitLogin'
        self.my_account_css = '#center_column > h1'

    def click_signin_btn(self):
        self.driver.find_element_by_css_selector(self.sign_in_btn_css).click()

    def enter_credentials(self, email, password):
        self.driver.find_element_by_css_selector(self.registered_email_css).send_keys(email)
        self.driver.find_element_by_css_selector(self.registered_passwd_css).send_keys(password)
        self.driver.find_element_by_css_selector(self.log_in_btn_css).click()

    def display_email_alert(self):
        email_alert = self.driver.find_element_by_css_selector(self.email_alert_css)
        return email_alert.text

    def display_my_account(self):
        my_account = self.driver.find_element_by_css_selector(self.my_account_css)
        return my_account.text