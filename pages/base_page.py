from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import time

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url: str) -> bool:
        """Открывает URL и обрабатывает возможные алерты"""
        try:
            print(f"Opening URL: {url}")
            self.driver.get(url)
            
            # Ожидание загрузки страницы
            self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            time.sleep(2)
            
            # Обработка алертов при загрузке
            self._handle_possible_alerts()
            
            return True
        except Exception as e:
            print(f"Error opening URL {url}: {e}")
            self.take_screenshot(f"error_open_{url.split('/')[-1]}")
            return False

    def _handle_possible_alerts(self):
        """Обрабатывает возможные алерты на странице"""
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert detected: {alert_text}")
            alert.accept()
            print("Alert accepted")
            time.sleep(1)
        except TimeoutException:
            pass

    def find_element(self, by, value, timeout=10):
        """Находит элемент на странице"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            print(f"Element not found: {by}={value}, error: {e}")
            return None

    def click(self, by, value):
        """Выполняет клик по элементу"""
        element = self.find_element(by, value)
        if element:
            try:
                self.wait.until(EC.element_to_be_clickable((by, value)))
                element.click()
                time.sleep(1)
                return True
            except Exception as e:
                print(f"Click error: {e}")
        return False

    def type_text(self, by, value, text):
        """Вводит текст в поле"""
        element = self.find_element(by, value)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                return True
            except Exception as e:
                print(f"Type text error: {e}")
        return False

    def get_text(self, by, value):
        """Получает текст элемента"""
        element = self.find_element(by, value)
        if element:
            return element.text
        return ""

    def take_screenshot(self, name: str) -> None:
        """Создает скриншот для Allure отчета"""
        try:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Screenshot error: {e}")