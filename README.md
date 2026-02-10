# URL Shortener

*URL Shortener* — это мини-приложение на Python для сокращения ссылок.  
Позволяет:  
- создавать короткие URL для длинных ссылок;  
- переходить по короткому URL (редирект);  
- логировать операции и ошибки.

Реализовано с использованием FastAPI и SQLite без ORM. 

## Требования
- Python 3.12+
- fastapi
- httpx
- pytest
- uvicorn

## Инструкция по запуску
### Установка
Сначала склонируйте репозиторий и перейдите в папку проекта:
```Bash
git clone https://github.com/Hunteena/url-shortener.git
cd url-shortener
```
#### Вариант А: Если установлен uv (Быстрый способ)

uv сам создаст виртуальное окружение и установит все нужные библиотеки одной командой:
```Bash
uv sync
```
После этого можно сразу переходить к запуску.
#### Вариант Б: Если uv не установлен (Стандартный способ)

Используем стандартные инструменты Python:

Создание виртуального окружения:
```Bash
python -m venv .venv
```
Активация окружения:

Windows:
```Bash
.venv\Scripts\activate
```
macOS / Linux:
```Bash
source .venv/bin/activate
```
Установка зависимостей:
```Bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Запуск приложения

Теперь, когда окружение настроено, запустите основной скрипт:

С использованием uv:
```Bash
uv run uvicorn src.main:app
```
Без использования uv (из активированного окружения):
```Bash
uvicorn src.main:app
```
### Запуск тестов

```Bash
pytest
```
