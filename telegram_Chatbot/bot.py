from lib2to3.fixes.fix_input import context

import requests
import json
import datetime
import time
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, update
from Toyproject.telegram_Chatbot.data import gubun_list, incDec_list, defCnt_list, nowdate2

# bot info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# token
token = ""


# /start message
def start(update, context):
    # username
    print(update.message.chat.username)
    t = '''
%s님 안녕하세요?
지역별 코로나 확진자 수를
알려주는 챗봇입니다.
전국 확진자 수는 /total
도움말은 /help 를 눌러주세요.
    ''' % update.message.chat.first_name  # username
    context.bot.send_message(chat_id=update.message.chat_id, text=t)


# /help  message
def help(update, context):
    print(update.message.chat.username)
    t = '''
지역을 입력해주시면 
오늘의 확진자 수를 알려드립니다
이 챗봇은 광역시 / 도 단위만 지원합니다.
ex ) 광주 , 서울 , 전남 , 제주
    '''
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
    time.sleep(0.3)


# 지역별 확진자 수
def get_message(update, context):
    msg = update.message.text

    for i in range(0, 18):
        if msg == gubun_list[i]:
            t = nowdate2 + '\n지역 : ' + gubun_list[i] + '\n신규 확진자 수 : ' + incDec_list[i] + ' 명\n누적 확진자 수 : ' + \
                defCnt_list[i] + ' 명'
            context.bot.send_message(chat_id=update.message.chat_id, text=t)
            return
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="/help 도움말을 참고하세요")


# 총 확진자 수
def total(update, context):
    print(update.message.chat.username)
    t = nowdate2 + '의 \n전체 신규 확진자 수는 ' + incDec_list[18] + ' 명.\n누적 확진자 수는 ' + defCnt_list[18] + ' 명입니다.'
    context.bot.send_message(chat_id=update.message.chat_id, text=t)
    time.sleep(0.3)


# error
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    total_handler = CommandHandler('total', total)
    dispatcher.add_handler(total_handler)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    message_handler = MessageHandler(Filters.text, get_message)
    dispatcher.add_handler(message_handler)

    # log all errors
    dispatcher.add_error_handler(logging.error)
    updater.start_polling(timeout=3)
    updater.idle()


if __name__ == '__main__':
    main()
