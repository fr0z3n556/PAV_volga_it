# Automation Project - UI Testing

Проект автоматизации тестирования UI для сайта [Practice Automation](https://practice-automation.com/).

## 📋 О проекте

Проект содержит автоматизированные тесты для трех страниц:
- **Form Fields** - тестирование заполнения и отправки формы
- **Click Events** - тестирование различных типов кликов
- **Popups** - тестирование модальных окон (alert, confirm, prompt)

## 🛠 Технологии

- **Python 3.12+**
- **Selenium WebDriver**
- **Pytest** - фреймворк для тестирования
- **Allure** - система отчетов
- **Page Object Pattern** - архитектурный паттерн

## 📁 Структура проекта

automation_project/

├── pages/ # Page Object классы

│ ├── base_page.py # Базовый класс страницы

│ ├── click_events_page.py

│ ├── form_page.py

│ └── popups_page.py

├── tests/ # Тестовые сценарии

│ ├── test_click_events.py

│ ├── test_form.py

│ └── test_popups.py

├── allure-results/ # Результаты Allure (генерируется)

├── conftest.py # Конфигурация Pytest

├── requirements.txt # Зависимости проекта

└── README.md # Документация

## ⚙️ Установка и настройка

1. **Клонируйте репозиторий**

git clone <repository-url>
cd automation_project

2. **Установите зависимости**
pip install -r requirements.txt

3. **Убедитесь, что установлен Chrome браузер**

4. **Настройка settings.json**


{

    "python.analysis.typeCheckingMode": "off",
    
    "python.analysis.autoImportCompletions": true,
    
    "python.analysis.extraPaths": [".", "./typings"],
    
    "python.languageServer": "Pylance",
    
    "python.envFile": "${workspaceFolder}/.env",
    
    "python.testing.pytestEnabled": true,
    
    "python.testing.unittestEnabled": false,
    
    "python.testing.nosetestsEnabled": false,
    
    "python.testing.pytestArgs": [
    
        "-v",
        
        "-s",
        
        "--alluredir=allure-results"
    ],
    
    
    "python-envs.defaultEnvManager": "ms-python.python:system",
    
    "python-envs.pythonProjects": []

}

## 🚀 Запуск тестов

### Запуск всех тестов
pytest --alluredir=allure-results -v -s

### Запуск конкретных тестов
**Только тесты формы**
pytest tests/test_form.py -v -s

**Только тесты кликов**
pytest tests/test_click_events.py -v -s

**Только тесты попапов**
pytest tests/test_popups.py -v -s

### Просмотр отчетов Allure
**Генерация и просмотр отчета**
allure serve allure-results

**Или генерация статического отчета**
allure generate allure-results -o allure-report
