# app/schemas/user.py
from fastapi_users import schemas


# Для аннотации в квадратных скобках указан
# выбранный нами тип id пользователя — int
class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
