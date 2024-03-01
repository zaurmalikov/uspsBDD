from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    quick_tools_menu = (By.XPATH, "//a[@class='nav-first-element menuitem']")
    all_quick_tools_menu_items = (By.XPATH, "//li[@class='qt-nav menuheader']/div/ul/li")

    @staticmethod
    def navigate(driver):
        driver.get("https://www.usps.com/")
        driver.implicitly_wait(20)
        assert "https://www.usps.com/" == driver.current_url

    @staticmethod
    def move_to_quick_tools_menu(driver):
        action = ActionChains(driver)
        move = action.move_to_element(driver.find_element(*MainPage.quick_tools_menu)).perform()
        return move

    @staticmethod
    def click_on_look_ip_a_zipcode_icon(driver):
        menu_items = driver.find_elements(*MainPage.all_quick_tools_menu_items)
        for item in menu_items:
            if "Look Up a" in item.text:
                item.click()
                break
        assert "ZIP Code™ Lookup | USPS" in driver.title
