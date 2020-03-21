import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.pages.login import Login
from page_object_pattern.pages.shopping_cart import ShoppingCart
from page_object_pattern.pages.registration import Registration
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
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
