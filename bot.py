import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Получаем токен из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    print("Ошибка: отсутствует TELEGRAM_TOKEN")
    exit(1)

# Создаём объект бота
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я работаю!")

# Добавляем команду /start в бота
dispatcher.add_handler(CommandHandler("start", start))

# Импортируем keep_alive для поддержки работы на Render
from keep_alive import keep_alive
keep_alive()

# Запускаем бота
updater.start_polling()
updater.idle()
