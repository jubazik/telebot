import app
from telebot import TeleBot
import sqlalchemy
from api.config.config import TOKEN, Config


app.config.from_object(Config)
db = sqlalchemy(app)



bot = TeleBot(TOKEN, parse_mode=None) # Подключение токена
