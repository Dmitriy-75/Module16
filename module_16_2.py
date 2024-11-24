# Задача "Аннотация и валидация":

from fastapi import FastAPI, Path
app = FastAPI()

@app.get("/")
async def basis_page():
    return "Главная станица"

@app.get("/user/admin")
async def page_of_admin():
    return "Вы вошли как администратор"

# Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
# '/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо
# написать следующую валидацию:
# Должно быть целым числом
# Ограничено по значению: больше или равно 1 и меньше либо равно 100.
# Описание - 'Enter User ID'

@app.get("/user/{user_id}")
async def user_id(user_id: int = Path(ge=1, le=100, description = "Enter your id")):
    return f"Вы вошли как пользователь № {user_id}"

# Пример - '1' (можете подставить свой пример не противоречащий валидации)
# '/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и
# age, для которых необходимо написать следующую валидацию:
# username - строка, age - целое число.
# username ограничение по длине: больше или равно 5 и меньше либо равно 20.
# age ограничение по значению: больше или равно 18 и меньше либо равно 120.
# Описания для username и age - 'Enter username' и 'Enter age' соответственно.


@app.get("/user/{username}/{age}")
async def data_user(username: str = Path(min_length=5, max_length=20, description="Enter username"),
                    age: int = Path(qe = 18,le=120, description="Enter age")):
    return f"Информация о пользователе.  Имя: {username}, Возраст: {age} "

# python -m uvicorn module_16_2:app


