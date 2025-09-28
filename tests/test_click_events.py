import pytest
import allure
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.click_events_page import ClickEventsPage

@allure.feature("Click Events")
class TestClickEvents:
    """Тесты для страницы Click Events"""
    
    @allure.story("Test different click events")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_events(self, driver):
        """Тестирование различных типов кликов"""
        click_page = ClickEventsPage(driver)
        
        with allure.step("Open Click Events page"):
            result = click_page.open_click_events_page()
            assert result is True, "Страница не открылась"
        
        with allure.step("Test single click"):
            result = click_page.perform_click()
            assert result is True, "Одинарный клик не сработал"
            
        with allure.step("Test double click"):
            result = click_page.perform_double_click()
            assert result is True, "Двойной клик не сработал"
            
        with allure.step("Test right click"):
            result = click_page.perform_right_click()
            assert result is True, "Правый клик не сработал"

        with allure.step("Verify click results"):
            click_result = click_page.get_click_result()
            double_click_result = click_page.get_double_click_result()
            right_click_result = click_page.get_right_click_result()
            
            print(f"Click result: {click_result}")
            print(f"Double click result: {double_click_result}")
            print(f"Right click result: {right_click_result}")
            
            assert click_result is not None, "Нет результата одинарного клика"
            assert double_click_result is not None, "Нет результата двойного клика"
            assert right_click_result is not None, "Нет результата правого клика"