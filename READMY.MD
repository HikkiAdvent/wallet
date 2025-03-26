# Wallet API

Это REST API для управления кошельками.

## Требования

* Python 3.12+
* Docker
* Docker Compose

## Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone <ваш_репозиторий>
    cd <ваш_репозиторий>
    ```

2.  Создайте виртуальное окружение (рекомендуется):

    ```bash
    python3.12 -m venv venv
    source venv/bin/activate # Для Linux/macOS
    venv\Scripts\activate # Для Windows
    ```

3.  Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4.  Создайте файл `.env` в корне проекта и добавьте переменные окружения для подключения к базе данных PostgreSQL:

    ```
    DB_HOST=db
    DB_PORT=5432
    POSTGRES_PASSWORD=wallet_api
    POSTGRES_USER=wallet_api
    POSTGRES_DB=wallet_api
    ```

    **Важно:** Замените `mysecretpassword` на надежный пароль.

## Запуск с помощью Docker Compose

1.  Запустите Docker Compose:

    ```bash
    sudo docker compose up -d
    ```

2.  Примените миграции Alembic:

    ```bash
    sudo docker compose exec backend alembic upgrade head
    ```

3.  API будет доступен по адресу `http://localhost:8000/api/v1/wallets/`.

## Запуск без Docker

1.  Запустите сервер PostgreSQL (убедитесь, что он запущен и доступен по указанным в `.env` настройкам).

2.  Примените миграции Alembic:

    ```bash
    alembic upgrade head
    ```

3.  Запустите приложение:

    ```bash
    uvicorn main:app --reload --host 0.0.0.0
    ```

4.  API будет доступен по адресу `http://localhost:8000/api/v1/wallets/`.

5. Документация по адресу `http://localhost:8000/doc`

## Тестирование

Для запуска тестов выполните следующую команду:

```bash
pytest