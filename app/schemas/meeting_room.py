from typing import Optional

from pydantic import BaseModel, Field, validator


# Базовый класс схемы, от которого наследуем все остальные.
class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]

    class Config:
        # title = 'Класс для приветствия'
        min_anystr_length = 1
        # Но это ещё не всё. Чтобы FastAPI мог сериализовать
        # объект ORM-модели в схему MeetingRoomDB, нужно указать,
        # что схема может принимать на вход объект базы данных,
        # а не только Python-словарь или JSON-объект.
        orm_mode = True


# Теперь наследуем схему не от BaseModel, а от MeetingRoomBase.
class MeetingRoomCreate(MeetingRoomBase):
    # Переопределяем атрибут name, делаем его обязательным.
    name: str = Field(..., max_length=100)
    # Описывать поле description не нужно: оно уже есть в базовом классе.


# Новый класс для обновления объектов.
class MeetingRoomUpdate(MeetingRoomBase):

    @validator('name')
    def name_cant_be_none(cls, value):
        if value is None:
            raise ValueError('Имя не может быть None')
        return value


# Возвращаемую схему унаследуем от MeetingRoomCreate,
# чтобы снова не описывать обязательное поле name.
class MeetingRoomDB(MeetingRoomCreate):
    id: int


# class MeetingRoomCreate(BaseModel):
#     name: str = Field(..., max_length=100)
#     description: Optional[str]

#     class Config:
#         # title = 'Класс для приветствия'
#         min_anystr_length = 1
