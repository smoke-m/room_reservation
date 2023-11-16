from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
  title=settings.app_title,
  docs_url='/swagger',
  description=settings.app_description,
)
