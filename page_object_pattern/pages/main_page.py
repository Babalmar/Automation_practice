"""moduł z funkcjami które zwracają nam stringa (nasz selektor)"""


def signin_button():
    return 'login'

def email_field():
    return 'email_create'

def createAccount_button():
    return '#SubmitCreate'

def accountform_header():
    return 'form#create-account_form > h3'

def registration_form():
    return 'form#account-creation_form div:nth-child(1) > h3'

def register_button():
    return 'submitAccount'

def radio_button_title():
    return 'uniform-id_gender1'

def input_customer_firstname():
    return 'customer_firstname'

def input_customer_lastname():
    return 'customer_lastname'

def input_password():
    return 'passwd'

def input_firstname():
    return 'firstname'

def input_lastname():
    return 'lastname'

def input_address():
    return 'address1'

def input_city():
    return 'city'

def dropdown_state():
    return 'id_state'

def input_zipcode():
    return 'postcode'

def input_mobile():
    return 'phone_mobile'

def loginform_header():
    return 'form#login_form > h3'

def auth_failed():
    return '#div#center_column li'

def registered_email():
    return 'email'

def registered_passwd():
    return 'passwd'

def account_page():
    return 'div#center_column > h1'

def registration_error():
    return 'div#center_column div > p'

def createAccount_error():
    return '.alert.alert-danger#create_account_error li'

def invalidEmail_error():
    return 'div#create_account_error li'

def addToCart_button():
    return 'Add to cart'

def checkout_button():
    return 'div#layer_cart a > span'

def cart_header():
    return 'cart_title'

def cart_checkout_button():
    return 'div#center_column a.button.btn.btn-default.standard-checkout.button-medium > span'
