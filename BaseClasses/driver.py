from playwright.sync_api import Page
from enum import Enum

class LocatorType(Enum):
    CSS = "css"
    XPATH = "xpath"
    TEXT = "text"
    ROLE = "role"
    ID = "id"

class Driver:
    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator_type: LocatorType, locator_value: str):
        if locator_type == LocatorType.CSS:
            return self.page.locator(locator_value)
        elif locator_type == LocatorType.XPATH:
            return self.page.locator(f"xpath={locator_value}")
        elif locator_type == LocatorType.TEXT:
            return self.page.locator(f"text={locator_value}")
        elif locator_type == LocatorType.ROLE:
            return self.page.locator(f"role={locator_value}")
        elif locator_type == LocatorType.ID:
            return self.page.locator(f"id={locator_value}")
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def is_element_visible(self, locator_type: LocatorType, locator_value: str) -> bool:
        element = self.find_element(locator_type, locator_value)
        return element.is_visible()

    def click(self, locator_type: LocatorType, locator_value: str):
        element = self.find_element(locator_type, locator_value)
        element.click()

    def fill(self, locator_type: LocatorType, locator_value: str, value: str):
        element = self.find_element(locator_type, locator_value)
        element.fill(value)

    def get_text(self, locator_type: LocatorType, locator_value: str) -> str:
        element = self.find_element(locator_type, locator_value)
        return element.inner_text()
