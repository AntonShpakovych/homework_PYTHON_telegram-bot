import telebot
import config
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from datetime import datetime, time, timedelta


request = requests.get("https://ua.sinoptik.ua/погода-рівне")
html = BeautifulSoup(request.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)

tabs = html.select_one('.tabs')
first_day = tabs.select_one('#bd1').text.strip()
day_2 = tabs.select_one('#bd2').text.strip()
day_3 = tabs.select_one('#bd3').text.strip()
day_4 = tabs.select_one('#bd4').text.strip()
day_5 = tabs.select_one('#bd5').text.strip()
day_6 = tabs.select_one('#bd6').text.strip()
day_7 = tabs.select_one('#bd7').text.strip()


@bot.message_handler(commands=['start'])
def buttons(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(
        text=first_day, callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_2, callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_3, callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_4, callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_5, callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_6, callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(
        text=day_7, callback_data=7))
    bot.send_message(
        message.chat.id, text='Вибери погоду на дату', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(
        callback_query_id=call.id, text="You check some button!")
    answer = ''
    if call.data == '1':
        wind = html.select_one(
            '#bd1c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1 > div').text
        desc_1 = html.select_one(
            '#bd1c > div.wDescription.clearfix > div.rSide > div').text
        humidity = f"{html.select_one('#bd1c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1').text}-{html.select_one('#bd1c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p8').text}"
        current_temp = html.select_one('.tabsContent .today-temp').text
        max_temp = tabs.select_one('.temperature .max').text.strip()
        min_temp = tabs.select_one('.temperature .min').text.strip()
        answer = f'''Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nПоточна.темп:{current_temp}\nВологість:{humidity}\nСил.напр.вітру:{wind}\nОпис:{desc_1}'''
    elif call.data == '2':
        today = datetime.today().date()+timedelta(days=1)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_2 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_2.select_one(
            '#bd2 > div.temperature > div.min > span').text
        max_temp = html_2.select_one(
            '#bd2 > div.temperature > div.max > span').text
        wind_2 = html_2.select_one(
            '#bd2c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1 > div').text
        humidity_2 = html_2.select_one(
            '#bd2c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1').text
        desc_2 = html_2.select_one(
            '#bd2c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_2}\nСил.напр.вітру:{wind_2}\nОпис:{desc_2}'

    elif call.data == '3':
        today = datetime.today().date()+timedelta(days=2)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_3 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_3.select_one(
            '#bd3 > div.temperature > div.min > span').text
        max_temp = html_3.select_one(
            '#bd3 > div.temperature > div.max > span').text
        wind_3 = html_3.select_one(
            '#bd3c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1.bR').text
        humidity_3 = html_3.select_one(
            '#bd3c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1.bR').text
        desc_3 = html_3.select_one(
            '#bd3c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_3}\nСил.напр.вітру:{wind_3}\nОпис:{desc_3}'
    elif call.data == '4':
        today = datetime.today().date()+timedelta(days=3)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_4 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_4.select_one(
            '#bd4 > div.temperature > div.min > span').text
        max_temp = html_4.select_one(
            '#bd4 > div.temperature > div.max > span').text
        wind_4 = html_4.select_one(
            '#bd4c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1.bR').text
        humidity_4 = html_4.select_one(
            '#bd4c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1.bR').text
        desc_4 = html_4.select_one(
            '#bd4c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_4}\nСил.напр.вітру:{wind_4}\nОпис:{desc_4}'
    elif call.data == '5':
        today = datetime.today().date()+timedelta(days=4)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_5 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_5.select_one(
            '#bd5 > div.temperature > div.min > span').text
        max_temp = html_5.select_one(
            '#bd5 > div.temperature > div.max > span').text
        wind_5 = html_5.select_one(
            '#bd5c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1.bR').text
        humidity_5 = html_5.select_one(
            '#bd5c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1.bR').text
        desc_5 = html_5.select_one(
            '#bd5c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_5}\nСил.напр.вітру:{wind_5}\nОпис:{desc_5}'
    elif call.data == '6':
        today = datetime.today().date()+timedelta(days=5)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_6 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_6.select_one(
            '#bd6 > div.temperature > div.min > span').text
        max_temp = html_6.select_one(
            '#bd6 > div.temperature > div.max > span').text
        wind_6 = html_6.select_one(
            '#bd6c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1.bR').text
        humidity_6 = html_6.select_one(
            '#bd6c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1.bR').text
        desc_6 = html_6.select_one(
            '#bd6c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_6}\nСил.напр.вітру:{wind_6}\nОпис:{desc_6}'
    elif call.data == '7':
        today = datetime.today().date()+timedelta(days=6)
        request = requests.get(f"https://ua.sinoptik.ua/погода-рівне/{today}")
        html_7 = BeautifulSoup(request.content, 'html.parser')

        min_temp = html_7.select_one(
            '#bd7 > div.temperature > div.min > span').text
        max_temp = html_7.select_one(
            '#bd7 > div.temperature > div.max > span').text
        wind_7 = html_7.select_one(
            '#bd7c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(7) > td.p1.bR').text
        humidity_6 = html_7.select_one(
            '#bd7c > div.wMain.clearfix > div.rSide > table > tbody > tr:nth-child(6) > td.p1.bR').text
        desc_7 = html_7.select_one(
            '#bd7c > div.wDescription.clearfix > div.rSide > div').text
        answer = f'Інформація\nМакс.темп:{max_temp}\nМін.темп:{min_temp}\nВологість:{humidity_6}\nСил.напр.вітру:{wind_7}\nОпис:{desc_7}'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()
