from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class FormPage(BasePage):
    """Page Object для страницы Form Fields"""
    
    def open_form_page(self):
        """Открывает страницу Form Fields"""
        return self.open_url("https://practice-automation.com/form-fields/")

    def fill_form(self, name: str, email: str, message: str):
        """Заполняет форму данными"""
        success = True
        success &= self.type_text(By.ID, "g1103-name", name)
        success &= self.type_text(By.ID, "g1103-email", email)
        success &= self.type_text(By.ID, "contact-form-comment-g1103-message", message)
        return success

    def submit_form(self):
        """Отправляет форму"""
        success = self.click(By.CSS_SELECTOR, "p.pushbutton-wide input[type='submit']")
        if success:
            time.sleep(2)
        return success

    def get_page_title(self):
        """Получает заголовок страницы"""
        try:
            return self.driver.title
        except:
            return ""