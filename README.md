# Автотесты REST API Яндекс Диска

Тестовое задание: автотесты для API Яндекс Диска (https://cloud-api.yandex.net).
Стек: Python 3, pytest, requests, Allure.

## Что проверяется
- GET: информация о Диске, метаинформация папки, ответ 401 без токена
- PUT: создание папки (201), повторное создание (409)
- POST: копирование и перемещение папки
- DELETE: удаление папки (204), удаление несуществующей (404)

## Подготовка
1. Python 3.10+
2. Установить зависимости:

Windows:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Получить OAuth-токен тестового аккаунта в Полигоне: https://yandex.ru/dev/disk/poligon/
4. Задать токен в переменной окружения:

Windows:
```
$env:YANDEX_DISK_TOKEN="ваш_токен"
```

macOS/Linux:
```
export YANDEX_DISK_TOKEN="ваш_токен"
```

## Запуск
```
pytest -v
```
Тесты создают временные папки в `disk:/autotests` и удаляют их после себя.

## Отчёт Allure

Нужны Java 11+ и Allure CLI (Windows: `scoop install allure`, macOS: `brew install allure`).
```
pytest --alluredir=allure-results
allure serve allure-results
```

## Структура
- `disk_api/config.py` — адрес API и чтение токена
- `disk_api/client.py` — клиент: методы для запросов к API
- `tests/conftest.py` — фикстуры: клиент и временная папка для каждого теста
- `tests/test_*.py` — тесты, разбитые по функциям API