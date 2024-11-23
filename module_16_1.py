# Задача "Начало пути":

# Маршрутизация:

# 1.Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
from fastapi import FastAPI
app = FastAPI()

# 2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".

@app.get("/")
async def basis_page():
    return "Главная станица"

# 3.Создайте маршрут к странице администратора - "/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".

@app.get("/user/admin")
async def page_of_admin():
    return "Вы вошли как администратор"

# 4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}". По нему должно
# выводиться сообщение "Вы вошли как пользователь № <user_id>".

@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# 5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user". По нему должно
# выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

@app.get("/user/{username}/{age}")
async def data_user(username: str, age: int):
    return f"Информация о пользователе.  Имя: {username}, Возраст: {age} "

# python -m uvicorn module_16_1:app


