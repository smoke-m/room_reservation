from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_meeting_room_exists, check_reservation_intersections,
    check_reservation_before_edit,
)
from app.core.db import get_async_session
from app.crud.reservation import reservation_crud
from app.schemas.reservation import ReservationCreate, ReservationDB


router = APIRouter()


@router.post(
        '/',
        # Указываем схему ответа.
        response_model=ReservationDB,
        # ведь у объектов Reservation нет опциональных полей
        # response_model_exclude_none=True,
)
async def create_new_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(
        # Так как валидатор принимает **kwargs,
        # аргументы должны быть переданы с указанием ключей.
        **reservation.dict(), session=session
    )
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation


@router.get(
    '/',
    response_model=list[ReservationDB],
)
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session),
):
    return await reservation_crud.get_multi(session)


@router.delete(
    '/{reservation_id}',
    response_model=ReservationDB,
)
async def remove_reservation(
        reservation_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    reservation = await check_reservation_before_edit(
        reservation_id, session
    )
    reservation = await reservation_crud.remove(
        reservation, session
    )
    return reservation
