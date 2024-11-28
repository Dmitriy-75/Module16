# Задача "Модель пользователя":

# Подготовка:
# Используйте CRUD запросы из предыдущей задачи.


from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
app = FastAPI()

# Создайте пустой список users = []
users = []


# Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
# id - номер пользователя (int)
# username - имя пользователя (str)
# age - возраст пользователя (int)
class User(BaseModel):
    id: int
    username: str
    age: int

# Измените и дополните ранее описанные 4 CRUD запроса:
# get запрос по маршруту '/users' теперь возвращает список users.


@app.get("/users", response_model=users)
async def get_list():
    return users

# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.


@app.post("/user/{username}/{age}")
async def new_user(username:str, age:int):
    id_new: int = max((t.id for t in users),default=0)+1
    new_user = User(id=id_new, username=username, age=age)
    users.append(new_user)
    return new_user

# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.


@app.put("/user/{user_id}/{username}/{age}")
async def renew_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.

@app.delete("/user/{user_id}")
async def del_user(user_id:int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# python -m uvicorn module_16_4:app

