from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class PopupsPage(BasePage):
    """Page Object для страницы Popups"""
    
    def open_popups_page(self):
        """Открывает страницу Popups"""
        return self.open_url("https://practice-automation.com/popups/")

    def trigger_alert(self):
        """Активирует и обрабатывает Alert"""
        if self.click(By.ID, "alert"):
            time.sleep(1)
            return self._handle_alert()
        return False

    def trigger_confirm(self):
        """Активирует и обрабатывает Confirm"""
        if self.click(By.ID, "confirm"):
            time.sleep(1)
            return self._handle_alert()
        return False

    def trigger_prompt(self):
        """Активирует и обрабатывает Prompt"""
        if self.click(By.ID, "prompt"):
            time.sleep(1)
            return self._handle_prompt()
        return False

    def _handle_alert(self):
        """Обрабатывает стандартный алерт"""
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            print(f"Alert handled: {alert_text}")
            return True
        except:
            return False

    def _handle_prompt(self):
        """Обрабатывает prompt с вводом текста"""
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys("Test Input")
            alert.accept()
            print("Prompt handled with text input")
            return True
        except:
            return False

    def get_confirm_result(self):
        """Получает результат Confirm"""
        return self.get_text(By.ID, "confirmResult")

    def get_prompt_result(self):
        """Получает результат Prompt"""
        return self.get_text(By.ID, "promptResult")