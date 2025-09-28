import pytest
import allure
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.form_page import FormPage

@allure.feature("Form Page")
class TestForm:
    """Тесты для страницы Form Fields"""
    
    @allure.story("Fill and submit form")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_and_submit_form(self, driver):
        """Тестирование заполнения и отправки формы"""
        form_page = FormPage(driver)
        
        with allure.step("Open Form page"):
            result = form_page.open_form_page()
            assert result is True, "Страница не открылась"

        with allure.step("Fill form fields"):
            result = form_page.fill_form("Test User", "test@example.com", "This is a test message")
            assert result is True, "Не удалось заполнить форму"
            
        with allure.step("Submit form"):
            result = form_page.submit_form()
            assert result is True, "Не удалось отправить форму"

        with allure.step("Verify form submission"):
            page_title = form_page.get_page_title()
            print(f"Page title: '{page_title}'")
            
            assert page_title != "", "Заголовок страницы пустой"
            assert len(page_title) > 0, "Заголовок страницы отсутствует"