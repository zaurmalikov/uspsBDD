import pytest
from pytest_bdd import *

from test_data.test_data_dict import TestData
from page_objects.cities_by_zip_code_sub_page import CitiesByZipSubPage
from page_objects.look_up_page import LookUpPage
from page_objects.main_page import MainPage
from page_objects.validation_sub_page import ResultValidationSubPage
from test_data.test_data_dict import TestData
from tests.conftest import driver


@pytest.fixture(params=TestData.test_data_values)  # this will pull data from mentioned dictionary in test data
def value(request):
    return request.param


@given("I am on the main page of usps web site")
def navigate_to_main_page():
    MainPage.navigate(driver)


@when("I am navigating to the quick tools menu")
def navigate_to_quick_tools_menu():
    MainPage.move_to_quick_tools_menu(driver)


@when("clicking on Look up a zip code icon")
def click_on_look_up_a_zip_code():
    MainPage.click_on_look_ip_a_zipcode_icon(driver)


@when("clicking find cities by zip code")
def click_find_cities_by_zip_button():
    LookUpPage.click_on_find_cities_by_zip_button(driver)


@when("entering zip code")
def zip_code_entry():
    CitiesByZipSubPage.enter_zip_code(value["zip_code"])


@when("clicking Find button")
def find_button_click():
    CitiesByZipSubPage.click_find_button(driver)


@then("relevant city and state name should be displayed")
def validation():
    assert value["city"] in ResultValidationSubPage.result_validation(driver)




