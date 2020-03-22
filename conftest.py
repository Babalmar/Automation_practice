import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.pages.login import Login
from page_object_pattern.pages.shopping_cart import ShoppingCart
from page_object_pattern.pages.registration import Registration


@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.set_capability('browseName', 'Chrome')
    options.add_argument('headless')
    options.add_argument('start-maximized')
    options.set_capability('version', '80.0.3987.106')
    driver = webdriver.Remote('http://localhost:4444/wd/hub', options=options)
    driver.get('http://automationpractice.com/index.php')
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 15)
    request.cls.shoppingCart = ShoppingCart(driver)
    request.cls.registration = Registration(driver)
    request.cls.login = Login(driver)
    yield
    time.sleep(2)
    driver.quit()
