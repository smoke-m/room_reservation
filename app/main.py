from fastapi import FastAPI

# Импортируем роутер.
from app.api.routers import main_router
from app.core.config import settings


app = FastAPI(
  title=settings.app_title,
  docs_url='/swagger',
  description=settings.app_description,
)

# Подключаем роутер.
app.include_router(main_router)
