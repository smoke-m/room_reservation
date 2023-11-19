from fastapi import FastAPI

# Импортируем роутер.
from app.api.meeting_room import router
from app.core.config import settings


app = FastAPI(
  title=settings.app_title,
  docs_url='/swagger',
  description=settings.app_description,
)

# Подключаем роутер.
app.include_router(router)
