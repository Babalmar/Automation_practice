class Login:
    def __init__(self, driver):
        self.registered_email_css = 'email'
        self.registered_passwd_css = 'passwd'
        self.account_page_css = 'div#center_column > h1'
        self.registration_error_css = 'div#center_column div > p'
        self.createAccount_error_css = '.alert.alert-danger#create_account_error li'
        self.invalidEmail_error_css = 'div#create_account_error li'