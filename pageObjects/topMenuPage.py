from selenium.webdriver.common.by import By

class TopMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_dropdown = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def logout(self):
        self.driver.find_element(*self.user_dropdown).click()
        self.driver.find_element(*self.logout_button).click()