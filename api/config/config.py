from pathlib import Path

BASE_DIR = Path(__file__).parent
TOKEN = "5424088548:AAHx-Psy3KEwNIPqyyDgu00dxMcgiXYImIs" # Токен телеграмма

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlit///{BASE_DIR / 'main.db'}"
