import pytest
from selenium import webdriver
from pageObjects.loginPagePOM import LoginPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_login(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login("Manar", "saidi123")