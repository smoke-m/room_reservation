# Импортируем из Алхимии нужные классы.
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

# Импортируем базовый класс для моделей.
from app.core.db import Base


class MeetingRoom(Base):
    # Имя переговорки должно быть не больше 100 символов,
    # уникальным и непустым.
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # reservations — атрибут relationship, описывающий взаимосвязи между
    # моделями, по которому можно будет получить все объекты бронирования
    # для данной переговорки.

    # Установите связь между моделями через функцию relationship.

    # Чтобы в случае удаления переговорки удалялись
    # и объекты модели Reservation
    # в аргументах функции relationship() укажите параметр cascade='delete'
    reservations = relationship('Reservation', cascade='delete')
