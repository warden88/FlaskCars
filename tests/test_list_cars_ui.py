import pytest
from BaseClasses.driver import Driver, LocatorType
import requests
import time

class TestListCars:

    BASE_URL = "http://127.0.0.1:5000"

    def test_list_cars(self, page):
        driver = Driver(page)
        try:
            page.goto(self.BASE_URL)
            car_name_element = driver.find_element(LocatorType.ID, "qa-car")
            car_name_element.wait_for(state="visible", timeout=5000)
            car_name = car_name_element.inner_text()
            assert car_name == "BMW", f"Expected car name to be 'Honda', but got '{car_name}'"
        except AssertionError as e:
            print(f"Car element are not visible: {e}")
            raise e
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e
