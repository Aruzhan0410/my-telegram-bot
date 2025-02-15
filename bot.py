import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

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

# Импортируем keep_alive для Render
from keep_alive import keep_alive
keep_alive()

# Запускаем бота
print("Бот запущен...")
app.run_polling()
