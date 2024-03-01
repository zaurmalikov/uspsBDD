from selenium.webdriver.common.by import By

class CitiesByZipSubPage:
    def __init__(self, driver):
        self.driver = driver

    zip_code_text_box = (By.CSS_SELECTOR, "#tZip")
    find_button = (By.CSS_SELECTOR, "#cities-by-zip-code")

    @staticmethod
    def enter_zip_code(driver, zip_code_value):
        text_box = driver.find_element(*CitiesByZipSubPage.zip_code_text_box).send_keys(zip_code_value)
        return text_box

    @staticmethod
    def click_find_button(driver):
        driver.find_element(*CitiesByZipSubPage.find_button).click()
