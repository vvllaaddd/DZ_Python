# 🧪 Автоматизация тестирования сайта saucedemo.com и калькулятора

## 📂 Структура проекта

```
DZ_Python/
│
├── 10_lesson/
│   ├── test_shop.py              # Тест покупки товаров на saucedemo.com
│   ├── test_calculator.py        # Тест калькулятора
│
├── pages/                        # Page Object Model
│   ├── calculator_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── confest.py
│   ├── inventory_page.py
│   └── login_page.py
│
└── README.md

```

## 📦 Зависимости

Убедитесь, что у вас установлены:

- Python 3.7+
- [Google Chrome](https://www.google.com/chrome/)
- `pytest`
- `selenium`
- `allure-pytest`
- `webdriver-manager`

Установка зависимостей:

```bash
pip install -r requirements.txt
```

## 🚀 Как запустить тесты с Allure

powershell

### 1. Запустите тесты с генерацией данных для Allure:

```bash
pytest --alluredir=allure-results
```

### 2. Сгенерируйте HTML-отчёт:

```bash
allure generate allure-results --clean -o allure-report
```

### 3. Откройте отчёт в браузере:

```bash
allure open allure-report
```
