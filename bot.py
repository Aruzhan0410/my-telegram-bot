import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask
import threading

# Получаем токен из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    print("Ошибка: отсутствует TELEGRAM_TOKEN")
    exit(1)

# Создаём объект бота
app = Application.builder().token(TELEGRAM_TOKEN).build()

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я работаю!")

# Добавляем команду /start в бота
app.add_handler(CommandHandler("start", start))

# Создаём Flask приложение для работы на Render
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Бот работает!"

# Функция для запуска Flask сервера
def run():
    flask_app.run(host='0.0.0.0', port=8080)

# Запускаем Flask сервер в отдельном потоке
def keep_alive():
    server = threading.Thread(target=run)
    server.start()

# Импортируем keep_alive и запускаем сервер
keep_alive()

# Начинаем слушать и обрабатывать обновления Telegram
print("Бот запущен...")
app.run_polling()
  
