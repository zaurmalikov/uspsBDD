from selenium.webdriver.common.by import By


class LookUpPage:
    def __init__(self, driver):
        self.driver = driver

    find_cities_by_zip_button = (By.LINK_TEXT, "Find Cities by ZIP")

    @staticmethod
    def click_on_find_cities_by_zip_button(driver):
        button = driver.find_element(*LookUpPage.find_cities_by_zip_button)
        button.click()
        assert "https://tools.usps.com/zip-code-lookup.htm?citybyzipcode" == driver.current_url