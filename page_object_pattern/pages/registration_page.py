from selenium.webdriver.support.ui import Select


class Registration:
    def __init__(self, driver):
        self.driver = driver
        self.signin_button_css = 'login'
        self.email_field_css = 'email_create'
        self.createAccount_btn_css = '#SubmitCreate'
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

    def create_account(self):
        self.driver.find_element_by_css_selector(self.createAccount_btn_css).click()

    def invalid_mail_error(self):
        element = self.driver.find_element_by_css_selector(self.invalidEmail_error_css)
        return element.text

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_field_css).send_keys(email)

    def register_account(self):
        self.driver.find_element_by_id(self.register_button_css).click()

    def registration_screen(self):
        reg_form_label = self.driver.find_element_by_css_selector(self.registration_form_css)
        return reg_form_label.text

    def registration_error(self):
        error = self.driver.find_element_by_css_selector(self.registration_error_css)
        return error.text

    def exisiting_account_error(self):
        error = self.driver.find_element_by_css_selector(self.createAccount_error_css)
        return error.text

    def populate_registration_form(self):
        self.driver.find_element_by_name(self.email_field_css).send_keys('mobiy43412@cityroyal.org')
        self.driver.find_element_by_css_selector(self.createAccount_btn_css).click()
        self.driver.find_element_by_id(self.radio_button_title_css).click()
        self.driver.find_element_by_name(self.input_customer_firstname_css).send_keys("John")
        self.driver.find_element_by_name(self.input_customer_lastname_css).send_keys("Doe")
        self.driver.find_element_by_name(self.input_password_css).send_keys("XDWZP8123")
        self.driver.find_element_by_name(self.input_firstname_css).send_keys("John")
        self.driver.find_element_by_name(self.input_lastname_css).send_keys("Doe")
        self.driver.find_element_by_name(self.input_address_css).send_keys("Westeria Lane")
        self.driver.find_element_by_name(self.input_city_css).send_keys("Denver")
        dropdown = Select(self.driver.find_element_by_id(self.dropdown_state_css))
        dropdown.select_by_index(6)
        self.driver.find_element_by_name(self.input_zipcode_css).send_keys("90210")
        self.driver.find_element_by_name(self.input_mobile_css).send_keys("8588489004")

    def account_landing_page(self):
        my_account = self.driver.find_element_by_css_selector(self.account_page_css)
        return my_account.text

    @staticmethod
    def random_mail():
        import random
        email = 'mobiy' + str(random.randint(43455, 99000)) + '@cityroyal.org'
        return email