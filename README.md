# Foodgram, «Продуктовый помощник»

Cайт Foodgram, «Продуктовый помощник». На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

# Документация

Документация для API после установки доступна по адресу
```
http://127.0.0.1/redoc/
```
# Запуск проекта в dev-режиме
- Клонируйте репозиторий
```
git@github.com:DenisLukianov21/foodgram-project-react.git
```
- Установите и активируйте виртуальное окружение
```
python3 -m venv venv
source /venv/bin/activate
```

- Установите зависимости из файла requirements.txt

``` pip install -r requirements.txt ```

- Перейдите в папку с файлом docker-compose.yaml и запустите контейнеры

``` docker-compose up -d --build ```
- Выполните миграции и создайте суперпользователя
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```
- Соберите статику
``` docker-compose exec backend python manage.py collectstatic --no-input ```

# Используемые технологии

- Python

- Django

- Django Rest Framework

- Simple-JWT

- PostreSQL

- Docker

# Импорт ингредиентов

В директории manage.py выполните команду, предварительно выполнив миграции
```
python manage.py loaddata ingredients.json
```

# Автор backend

Лукьянов Денис