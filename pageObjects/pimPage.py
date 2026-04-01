from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_btn = (By.XPATH, "//a[text()='Add Employee']")

    def click_add_employee(self):
        self.driver.find_element(*self.add_employee_btn).click()