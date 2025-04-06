from BaseClasses.driver import Driver, LocatorType
import requests


class TestListCars:

    BASE_URL = "http://127.0.0.1:5000"

    def test_add_car(self, page):
        driver = Driver(page)
        try:
            page.goto(self.BASE_URL)
            driver.find_element(LocatorType.TEXT, "Add Car").click()
            car_element = driver.find_element(LocatorType.TEXT, "BMW")
            car_element.wait_for(state="visible", timeout=5000)
            car_name = car_element.inner_text().split('\n')[0].strip()
            print(f"Car name: {car_name}")
            assert car_name == "BMW", f"Expected car name to be 'BMW', but got '{car_name}'"
        except AssertionError as e:
            print(f"Car element are not visible: {e}")
            raise e
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e
        finally:
            driver.find_element(LocatorType.TEXT, "Delete").click()
            
        