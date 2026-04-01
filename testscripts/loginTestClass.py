import pytest
from selenium import webdriver
from pageObjects.loginPagePOM import LoginPage
from pageObjects.dashboardPage import DashboardPage
from pageObjects.topMenuPage import TopMenuPage

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
    loginPage.login("Admin", "admin123")

    # ✅ ADD THIS PART
    dashboard = DashboardPage(driver)

    assert dashboard.is_dashboard_visible()

    # ✅ OPTIONAL NEXT STEP
    dashboard.click_pim()
    assert "pim" in driver.current_url.lower()



def test_logout(setup):
    driver = setup

    loginPage = LoginPage(driver)
    loginPage.login("Admin", "admin123")

    topMenu = TopMenuPage(driver)
    topMenu.logout()

    assert "login" in driver.current_url.lower()