import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()