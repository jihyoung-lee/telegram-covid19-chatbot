from lib2to3.fixes.fix_input import context

import requests
import json
import datetime
import time
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

# bot info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# token
token = ""


# start message
def start(update, context):
    # username
    print(update.message.chat.username)
    t = "%s! please click /test" % update.message.chat.first_name  # username
    context.bot.send_message(chat_id=update.message.chat_id, text=t)


"""
# echo
def echo(update, context):
    print(update.message.chat.username)
    t = "error"
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
"""


# buttons
"""
def button(buttons, n_cols, header_buttons=None, footer_buttons=None):
    for i in range(0, len(buttons), n_cols):
        menu = [buttons[i:i + n_cols]]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu

"""
# /test  message
def test(update, context):
    print(update.message.chat.username)
    t = "test!"
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
    time.sleep(0.3)
    t1 = "test 1 or test 2"
    context.bot.send_message(chat_id=update.message.chat_id, text=t1)
    time.sleep(0.3)
    """
    show_list = [InlineKeyboardButton("test1", callback_data="test1"),
                 InlineKeyboardButton("test2", callback_data="test2")]

    show_markup = InlineKeyboardMarkup(button(show_list, len(show_list) - 1))

    reply_markup = InlineKeyboardMarkup(show_list)
    query.edit_message_text(
        text="Choose a route", reply_markup=reply_markup
    )

    # context.bot.send_message("select", reply_markup=show_markup)
    """


# callback
def callback_get(update, context):
    print("callback")
    if update.callback_query.data == "test1":
        context.edit_message_text(text="select test1",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id)
    if update.callback_query.data == "test2":
        context.edit_message_text(text="select test2",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id)


# error
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


# def error(update, context, error):
#     logger.warning('Update "%s" caused error "%s"', context, error)


# main function
def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    # dispatcher.add_handler(MessageHandler(Filters.text, echo))
    test_handler = CommandHandler('test', test)
    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(CallbackQueryHandler(callback_get))

    # log all errors
    dispatcher.add_error_handler(logging.error)
    updater.start_polling(timeout=3)
    updater.idle()


if __name__ == '__main__':
    main()
