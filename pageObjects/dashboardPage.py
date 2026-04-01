from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()

    def click_pim(self):
        self.driver.find_element(*self.pim_menu).click()