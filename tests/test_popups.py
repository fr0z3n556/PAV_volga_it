import pytest
import allure
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.popups_page import PopupsPage

@allure.feature("Popups")
class TestPopups:
    """Тесты для страницы Popups"""
    
    @allure.story("Test all popup types")
    @allure.severity(allure.severity_level.NORMAL)
    def test_all_popups(self, driver):
        """Тестирование всех типов модальных окон"""
        popups_page = PopupsPage(driver)
        
        with allure.step("Open Popups page"):
            result = popups_page.open_popups_page()
            assert result is True, "Страница не открылась"

        with allure.step("Test alert popup"):
            result = popups_page.trigger_alert()
            assert result is True, "Alert не сработал"
            
        with allure.step("Test confirm popup"):
            result = popups_page.trigger_confirm()
            assert result is True, "Confirm не сработал"
            
        with allure.step("Test prompt popup"):
            result = popups_page.trigger_prompt()
            assert result is True, "Prompt не сработал"

        with allure.step("Verify popup results"):
            confirm_result = popups_page.get_confirm_result()
            prompt_result = popups_page.get_prompt_result()
            
            print(f"Confirm result: {confirm_result}")
            print(f"Prompt result: {prompt_result}")