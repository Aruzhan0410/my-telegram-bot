<<<<<<< HEAD
import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
=======
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
>>>>>>> 6ecf98a2953e801f476002ad446bf5dff0e3c6fc
