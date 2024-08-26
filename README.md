# API MOEX App

## Описание

API MOEX app - это веб-приложение, которое предоставляет информацию об акциях, торгующихся на Москвоской бирже.

---

Оно предоставляет возможность:

- Кэширования данных, которые были взяты с веб-сервиса TradingView, в базе данных SQLite
- Получения актуальных данных о компании по ее биржевому тикеру с помощью официльного API Московской биржи

## Стек технологий

- **Backend**: FastAPI (Python)
- **База данных**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Установка и запуск

### Установка приложения

1. Клонируйте репозиторий:
    
    ```sh
    git clone https://github.com/nikitaaav/api-moex-app.git
   ```

2. Перейдите в директорию проекта:

   ```sh
   cd api-moex-app
   ```

### Запуск приложения с помощью Docker

1. Клонируйте репозиторий и перейдите в директорию проекта:

   ```sh
   git clone https://github.com/nikitaaav/api-moex-app.git
   cd api-moex-app
   ```

2. Постройте Docker-образ:

   ```sh
   docker build -t api-moex-app .
   ```

3. Запустите Docker-контейнер:

   ```sh
   docker run -d -p 8000:8000 api-moex-app
   ```

4. Откройте браузер и перейдите по адресу:

   ```sh
   http://localhost:8000
   ```
5. Остановка контейнера:

   ```sh
   docker stop <id контейнера, которое можно узнать с помощью команды "docker ps">
   ```

### Запуск приложения

1. Создайте и активируйте виртуальное окружение:

   ```sh
   python -m venv venv
   source venv/bin/activate # Для Windows используйте venv\Scripts\activate
   ```

2. Установите зависимости:

   ```sh
   pip install -r requirements.txt
   ```

3. Запустите файл main.py:

   ```sh
   uvicorn src.main:app --reload
   ```

4. Откройте браузер и перейдите по адресу:

   ```sh
   http://localhost:8000
   ```

## Использование

- Введите тикер акции в поле ввода
- Нажмите на кнопку "Search"
- Информация о запросе отобразиться на главной странице
- Для обновления базы данных, которая используется для кэширования данных (логотип компании и веб-сайт), запустите файл cache_alg.py из папки src

## API

### Получение информации об акции

- **URL**: `/api/stock/{tkr}`
- **Метод**: `GET`
- **Параметры**:
  - `tkr` - тикер акции
- **Ответ (пример)**:
  ```json
  {
    "shortname": "Аэрофлот",
    "prev": "50.39",
    "fullname": "Аэрофлот-росс.авиалин(ПАО)ао",
    "ticker": "AFLT",
    "logo": "https://s3-symbol-logo.tradingview.com/aeroflot--big.svg",
    "webpage": "http://www.aeroflot.ru/"
  }
  ```
