from datetime import datetime, timedelta

from pydantic import BaseModel, Extra, Field, root_validator, validator

FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')

TO_TIME = (
    datetime.now() + timedelta(hours=1)
).isoformat(timespec='minutes')


class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        orm_mode = True
        # Чтобы запретить пользователю передавать параметры,
        # не описанные в схеме, в подклассе Config устанавливается
        # значение extra = Extra.forbid
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):

    # валидатор, проверяющий, что начало бронирования не меньше
    # текущего времени, назовите check_from_reserve_later_than_now.
    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value

    # валидатор, проверяющий, что время начала бронирования меньше
    # времени окончания, назовите check_from_reserve_before_to_reserve
    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
