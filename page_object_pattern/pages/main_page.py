class Registration:
    def __init__(self, driver):
        self.driver = driver
        self.signin_button_css = 'login'
        self.email_field_css = 'email_create'
        self.createAccount_btn_css = '#SubmitCreate'
        self.accountform_header_css = 'form#create-account_form > h3'
        self.registration_form_css = 'form#account-creation_form div:nth-child(1) > h3'
        self.register_button_css = 'submitAccount'
        self.radio_button_title_css = 'uniform-id_gender1'
        self.input_customer_firstname_css = 'customer_firstname'
        self.input_customer_lastname_css = 'customer_lastname'
        self.input_password_css = 'passwd'
        self.input_firstname_css = 'firstname'
        self.input_lastname_css = 'lastname'
        self.input_address_css = 'address1'
        self.input_city_css = 'city'
        self.dropdown_state_css = 'id_state'
        self.input_zipcode_css = 'postcode'
        self.input_mobile_css = 'phone_mobile'
        self.loginform_header_css = 'form#login_form > h3'
        self.auth_failed_css = '#div#center_column li'
        self.registered_email_css = 'email'
        self.registered_passwd_css = 'passwd'
        self.account_page_css = 'div#center_column > h1'
        self.registration_error_css = 'div#center_column div > p'
        self.createAccount_error_css = '.alert.alert-danger#create_account_error li'
        self.invalidEmail_error_css = 'div#create_account_error li'

    def click_signin(self):
        self.driver.find_element_by_class_name(self.signin_button_css).click()

    def check_label(self):
        auth_label = self.driver.find_element_by_css_selector(self.accountform_header_css)
        return auth_label.text

    def enter_invalid_mail(self):
        self.driver.find_element_by_name(self.email_field_css).send_keys("asd")
        self.driver.find_element_by_css_selector(self.createAccount_btn_css).click()

    def invalid_mail_error(self):
        element = self.driver.find_element_by_css_selector(self.invalidEmail_error_css)
        return element.text

