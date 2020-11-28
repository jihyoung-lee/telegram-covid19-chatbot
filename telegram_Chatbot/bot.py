import requests
import json
import datetime
import time
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# bot info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# token
token = "1420258828:AAH8tGeVR00zwDwKm0nAnBQEl9mu1UpAIyE"


# start message


def start(update, context):
    # username
    print(update.message.chat.username)
    t = ("%s! test!") % update.message.chat.first_name  # username
    context.bot.send_message(chat_id=update.message.chat_id, text=t)


# /test  message
def test(bot, update):
    t = "test!"
    bot.sendMessage(chat_id=update.message.chat_id, test=t)


# buttons 
"""
def button(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols]] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
"""


# error
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


# message & function
def main():
    updater = Updater(token=token, use_context=True)

    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # log all errors
    dispatcher.add_error_handler(error)
    updater.start_polling(timeout=3)
    updater.idle()


if __name__ == '__main__':
    main()
