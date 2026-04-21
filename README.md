# Books Exchange

Учебный Django-проект для сервиса обмена книгами.

В проекте уже реализованы:
- главная страница со списком книг из базы данных
- детальная страница книги
- форма обратной связи
- создание и редактирование книг через `ModelForm`
- админ-панель Django
- подключение PostgreSQL через Docker
- хранение секретов в `.env`

## Технологии

- Python 3.10+
- Django 5.2
- PostgreSQL 15
- Docker Compose
- psycopg 3
- python-dotenv
- Bootstrap 5

## Структура проекта

```text
WEB_SEMESTR_2/
├── config/
├── pages/
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── .env
```

## Подготовка окружения

1. Клонируйте репозиторий.
2. Перейдите в папку проекта.
3. Создайте и активируйте виртуальное окружение.
4. Установите зависимости.

### Linux / WSL / macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Настройка `.env`

Создайте файл `.env` в корне проекта на основе `.env.example`.

Пример содержимого:

```env
DB_NAME=books_exchange
DB_USER=postgres
DB_PASSWORD=supersecretpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Важно:
- файл `.env` не должен попадать в Git
- если в `SECRET_KEY` есть символ `$`, для Docker Compose лучше заменить его на `$$`

## Запуск PostgreSQL через Docker

Убедитесь, что Docker Desktop запущен и WSL Integration включена, если вы работаете через WSL.

Запуск контейнера:

```bash
docker compose up -d
```

Проверка контейнера:

```bash
docker compose ps
```

Остановка контейнера:

```bash
docker compose down
```

## Применение миграций

После запуска базы данных выполните:

```bash
python manage.py migrate
```

## Создание суперпользователя

Для входа в админку:

```bash
python manage.py createsuperuser
```

## Запуск сервера

```bash
python manage.py runserver
```

После запуска проект будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

## Основные маршруты

- `/` — главная страница со списком книг
- `/about/` — страница "О проекте"
- `/contact/` — форма обратной связи
- `/books/<pk>/` — детальная страница книги
- `/books/create/` — создание новой книги
- `/books/<pk>/edit/` — редактирование книги
- `/admin/` — админ-панель Django

## Заполнение базы

### Через админку

1. Откройте `/admin/`
2. Войдите под суперпользователем
3. Перейдите в раздел `Books`
4. Создайте нужные записи

### Через Django shell

```bash
python manage.py shell
```

Пример:

```python
from pages.models import Book

Book.objects.create(
    title='1984',
    description='Антиутопия Джорджа Оруэлла.',
    copies_available=2
)
```

## Что реализовано по функционалу

### Книги

- список книг выводится на главной странице
- у каждой книги есть детальная страница
- книгу можно создать через форму
- книгу можно редактировать через форму

### Обратная связь

- форма контактов доступна на `/contact/`
- используется `forms.Form`
- при успешной отправке данные выводятся в консоль сервера
- после отправки выполняется редирект на главную страницу

## Полезные команды

Проверка проекта:

```bash
python manage.py check
```

Создание миграций:

```bash
python manage.py makemigrations
```

Изменение пароля суперпользователя:

```bash
python manage.py changepassword <username>
```

## Примечания

- проект учебный и использует `DEBUG=True`
- встроенный сервер Django подходит только для разработки
- если порт `8000` занят, можно запустить:

```bash
python manage.py runserver 8001
```

## Автор

Проект выполнен в рамках учебных занятий по Django.
