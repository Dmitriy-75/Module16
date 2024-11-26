# Задача "Имитация работы с БД":


# Создайте новое приложение FastAPI и сделайте CRUD запросы.

from fastapi import FastAPI, HTTPException
app=FastAPI()


# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}

users = {'1': 'Имя: Example, возраст: 18'}


# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.

@app.get("/users")
async def get_dict():
    return users

# post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение
# строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".

@app.post("/user/{username}/{age}")
async def get_dict(username:str, age:int):
    key_max = max(users.keys())
    users[str(int(key_max)+1)] = f"Имя: {username}, возраст: {age}"
    return f"User {int(key_max)+1} is registered"


# put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id
# на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
@app.put("/user/{user_id}/{username}/{age}")
async def get_dict(user_id, username:str, age:int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete("/user/{user_id}")
async def get_dict(user_id):
    del users[user_id]
    return users


#python -m uvicorn module_16_3:app
