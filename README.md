# Разработка системы управления заказами в кафе

## Описание
Веб-приложение на Django для управления заказами в кафе. Данное приложение позволяет добавлять, удалять, искать, обновлять, отображать заказы и выводить итоговую выручку.

## Функциональные возможности
- Добавление заказа
- Удаление заказа
- Поиск заказа по статусу и номеру заказа
- Отображение всех заказов
- Изменение статуса заказа
- Расчет выручки за смену

## Стек технологий
- Python 3.8+
- Django 4+
- HTML/CSS
- PostgreSQL
- Markdown

## Установка и запуск

### Шаги

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/yourusername/cafe_mng.git
    cd cafe_management
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Для Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройка баззы данных:**
    ```
   Данные для использования базы данных находятся в окружении .env
   ```
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('name'),  # Название базы данных
        'USER': os.getenv('user'),  # Пользователь
        'PASSWORD': os.getenv('password'),  # Пароль
        'HOST': 'localhost',
        'PORT': os.getenv('port'),
    }
    }
   ```
    
5. **Примените миграции:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

Теперь Django-приложение должно быть доступно по адресу `http://127.0.0.1:8000/`.
