import json

# Подключаем классы асинхронной библиотеки
from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds
# Подключаем настройки
from app.core.config import settings

# Список разрешений
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Получаем объект учётных данных
cred = ServiceAccountCreds(
    scopes=SCOPES, **json.load(open(settings.credentials_file))
)


# Создаём экземпляр класса Aiogoogle
async def get_service():
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
