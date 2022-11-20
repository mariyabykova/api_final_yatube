# Проект API для социальной сети Yatube

### Описание 
Незарегистрированные пользователи могут просматривать посты, комментарии, группы проекта.
Для зарегистрированных пользователей доступны подписка на понравившихся авторов, 
добавление постов, комментариев, а также удаление и редактирование собственных публикаций
и комментариев.

### В API доступны следующие эндпоинты:

* ```http://127.0.0.1:8000/api/v1/posts/``` При GET-запросе на этот эндпоинт будет получен список публикаций (при указании параметров limit и offset выдача будет осуществляться с пагинацией).
При POST-запросе буден создана новая публикация. Анонимные POST-запросы запрещены.

* ```http://127.0.0.1:8000/api/v1/posts/{id}/``` GET-запрос позволяет поучить публикацию по id.
PUT- и PATCH-запросы позволяют редактировать публикацию.
DELETE-запрос удаляет публикацию. Анонимные PUT-, PATCH- и DELETE-запросы запрещены. Обновить и удалить публикацию может только автор публикации.

* ```http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/``` При GET-запросе будут получены все комментарии к публикации.
При POST-запросе будет создан новый комментарий.

* ```http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/``` При GET-запросе будет получен комментарий по id. 
При PATCH- и PUT-запросах комментарий будет отредактирован.
DELETE-запрос удалит комментарий. Анонимные PUT-, PATCH- и DELETE-запросы запрещены.

* ```http://127.0.0.1:8000/api/v1/groups/``` При GET-запросе будет получен список сообществ.

* ```http://127.0.0.1:8000/api/v1/groups/{id}/``` При GET-запросе будет получена информация о сообществе по id.

* ```http://127.0.0.1:8000/api/v1/follow/``` При GET-запросе будет получен список всех подписок пользователя, сделавшего запрос.
При POST-запросе будет создана новая подписка пользователя, сделавшего запрос, на пользователя, переданного в теле запроса. Анонимные POST-запросы запрещены.

* ```http://127.0.0.1:8000/api/v1/jwt/create/``` Получение JWT-токена.

* ```http://127.0.0.1:8000/api/v1/jwt/refresh/``` Обновление JWT-токена.

* ```http://127.0.0.1:8000/api/v1/jwt/verify/``` Проверка JWT-токена.


### Примеры запросов:

* Пример POST-запроса на эндпоинт '/api/v1/posts/':
```
{
"text": "random text",
"group": 1
}
```

* Пример GET-запроса на эндпоинт '/api/v1/posts/{id}/'. В качестве ответа будет получена информация о публикации по id:
```
* {
"id": 1,
"author": "author",
"text": "random text",
"pub_date": "2019-08-24T14:15:22Z",
"group": 1
}
```

* Пример PATCH-запроса на эндпоинт '/api/v1/posts/1':
```
{
"text": "some text",
"group": 2
}
```

* Пример POST-запроса на эндпоинт '/api/v1/posts/1/comments/':
```
{
"text": "string"
}
```

* Пример GET-запроса на эндпоинт '/api/v1/posts/1/comments/1/':
```
{
"id": 1,
"author": "author",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 1
}
```

* Пример DELETE-запроса на эндпоинт '/api/v1/posts/1/comments/'. В ответе будет выведена следующая информация:
```
{
"detail": "Учетные данные не были предоставлены."
}
```

* Пример GET-запроса на эндпоинт '/api/v1/groups/1/'. В качестве ответа будет получена информаци о группе с id=1:
```
{
"id": 1,
"title": "title",
"slug": "slug",
"description": "description"
}
```

* Пример POST-запроса на эндпоинт '/api/v1/follow/':
```
* {
"following": "author"
}
```

* Пример GET-запроса на эндпоинт '/api/v1/follow/'. В ответ будет получен список всех подписок пользователя, сделавшего запрос:
```
[
{
"user": "user",
"following": "author"
}
]
```


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/mariyabykova/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Автор
Мария Быкова