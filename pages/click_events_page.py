from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class ClickEventsPage(BasePage):
    """Page Object для страницы Click Events"""
    
    def open_click_events_page(self):
        """Открывает страницу Click Events"""
        return self.open_url("https://practice-automation.com/click-events/")

    def perform_click(self):
        """Выполняет одинарный клик"""
        return self.click(By.ID, "btn1")

    def perform_double_click(self):
        """Выполняет двойной клик"""
        element = self.find_element(By.ID, "dblclick")
        if element:
            try:
                action = ActionChains(self.driver)
                action.double_click(element).perform()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Double click error: {e}")
        return False

    def perform_right_click(self):
        """Выполняет правый клик"""
        element = self.find_element(By.ID, "rightclick")
        if element:
            try:
                action = ActionChains(self.driver)
                action.context_click(element).perform()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Right click error: {e}")
        return False

    def get_click_result(self):
        """Получает результат одинарного клика"""
        return self.get_text(By.ID, "demo1")

    def get_double_click_result(self):
        """Получает результат двойного клика"""
        return self.get_text(By.ID, "demo2")

    def get_right_click_result(self):
        """Получает результат правого клика"""
        return self.get_text(By.ID, "demo3")