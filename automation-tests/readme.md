# Automation QA Portfolio

Два проекта по автоматизации тестирования на Python.

## Структура

- `ui_tests/saucedemo/` – E2E тесты интернет-магазина SauceDemo (Selenium + Pytest)
- `api_tests/restcountries/` – API тесты Rest Countries (Requests + Pytest)

---

## UI Тесты (SauceDemo)

Полный сценарий покупки товара с применением Page Object Model, фикстур и ожиданий.

**Стек:** Python 3.9+, Selenium, Pytest, WebDriver Manager

**Как запустить (macOS):**
```bash
cd ui_tests/saucedemo
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pytest -v tests/
```

 **Ключевые особенности:**

- Page Object Model (LoginPage, InventoryPage, CartPage, CheckoutPage)
- Фикстура драйвера (открытие/закрытие браузера)
- Явные и неявные ожидания
- Позитивный E2E сценарий

## API Тесты (Rest Countries)

Проверки публичного REST API: получение списка стран, поиск по названию, коду, региону, обработка 404.

**Стек: Python 3.9+, Requests, Pytest**

**Как запустить (macOS):**

```bash
cd api_tests/restcountries
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v tests/
```
**Ключевые особенности:**

- Фикстура сессии Requests
- Параметризация запросов (по имени, коду, региону)
- Проверка структуры JSON и статус-кодов
- Обработка негативных сценариев (404)