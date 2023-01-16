# тестовый 
тестовое задание Intern Backend Developer

REST-API (Python)
1. Развернуть локальную базу данных PostgreSQL с созданием архитектуры под следующие пункты задания
2. Реализовать следующий метод: GET | /PLATE/GENERATE (Генерация государственных номеров автомобилей)
3. Метод должен принимать следующие параметры: token, amount
4. Где: token – Bearer-токен авторизации, amount – количество государственных номеров автомобилей в ответе
5. Примечание: token – любой формат, amount – int or null, если не указано, вернуть один номер. Если не указан токен, вернуть соответствующий ответ клиенту.
6. Реализовать следующий метод: GET | /PLATE/GET (Получение государственных номеров автомобилей)
7. Метод должен принимать следующие параметры: token, id
8. Вернуть в JSON формате все данные по записи
9. Где: token – Bearer-токен авторизации, id – идентификатор записи о государственном номере авто
10. Примечание: token – любой формат, id – любой (Предпочтительно uuid4 😊). Если не указан токен, вернуть соответствующий ответ клиенту.

11. Реализовать следующий метод: POST | /PLATE/ADD (Добавление государственных номеров автомобилей в базу данных)
12. Метод должен принимать следующие параметры: token, plate
13. Перед добавлением должна проводиться проверка на корректность государственного номера автомобиля
14. Где: token – Bearer-токен авторизации, plate – государственный номер
15. Примечание: token – любой формат, plate – str. Оба значения обязательны к передаче, если не указаны, вернуть соответствующие ответы клиенту.
16. Технологии: Любые с использование языка Python
17. В случае ошибок выдавать в ответе с понятным объяснением проблемы.

для запуска локально нужно
python3 -m venv venv  
source venv/bin/activate 

pip install Django

pip install -r requirements.txt

для работы с запросами request 
pip install requests

Создание и запуск скриптов миграции

python manage.py makemigrations <APPS>

python manage.py migrate <APPS>

Создание admin
python manage.py createsuperuser

Первый запуск сервера
python3 manage.py runserver


АУТЕНТИФИКАЦИЯ юзера выполнена на JWT

```python
pip install djoser djangorestframework_simplejwt 
PyJWT==1.7.1 
```
``` python
 JSON Web Token
# можно СОЗДАВАТЬ новых пользователей через
# POST запрос на http://127.0.0.1:8000/auth/users/
# {
#     "username": "oleg-1",
#     "password": "12345poiuy"
# }
# ответ {
#     "email": "",
#     "username": "oleg-1",
#     "id": 2
# }

# далее получаем новый Token - Bearer для пользователя
# по POST запросу
# http://127.0.0.1:8000/auth/jwt/create/
# в виде
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODQ3NjU2NiwianRpIjoiYzFmNTY4MjQ3M2Q4NGE4MzlhZWZmYTdmMzQ0MzExZTIiLCJ1c2VyX2lkIjo0fQ.U7fP2I-jyGzTojrZ8Y4ZHWjDDVMMYwCs-ga5h2ObXrk",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MDMwMTY2LCJqdGkiOiIwODU3OTQ5OWYwZWI0MmY5YWE1OGNhMTQzZjhmOTZmYyIsInVzZXJfaWQiOjR9.Y9q6nSEh7ihe-IeLbEvPSG6xLZx9RQrdOwPFC32EThk"
# }
```
###Эндпоинт для фронта
http://127.0.0.1:8000/




