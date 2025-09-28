import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    """Самая простая фикстура драйвера"""
    driver_instance = webdriver.Chrome()  # Простой вызов без параметров
    driver_instance.implicitly_wait(10)
    driver_instance.maximize_window()
    
    yield driver_instance
    
    # Даем время перед закрытием
    time.sleep(2)
    driver_instance.quit()

def pytest_runtest_makereport(item, call):
    pass