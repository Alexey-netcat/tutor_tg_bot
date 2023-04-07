import telebot
from telebot import types, TeleBot
import sqlite3

bot: TeleBot = telebot.TeleBot(token='6054508630:AAEVVbwbaFvgO8f4xIAprK3FriVPnCy6qf8')


# @bot.message_handler(commands=["inline_bottom"])
# def inline_bottom(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('гоу Яндекс', url='ya.ru'))
#     bot.send_message(message.chat.id, 'Перейди в Яндекс!', reply_markup=markup)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton('Записаться на урок'))
    bot.send_message(message.chat.id,
                     'Я бот Азата Бикзинурова. Могу помочь тебе записаться на занятие. Нажимай кнопку в меню!',
                     reply_markup=markup, parse_mode='html')


# @bot.message_handler(commands=["start"])
# def start(message):
#     conn = sqlite3.connect('test_db.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS test_table (id int auto_increment primary key, name varchar(50), vtime varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Записаться на урок':

        conn = sqlite3.connect('test_db.sql')
        cur = conn.cursor()

        cur.execute(
            'CREATE TABLE IF NOT EXISTS test_table (id int auto_increment primary key, name varchar(50), daynedeli '
            'varchar(50), daytime varchar(50))')
        conn.commit()
        cur.close()
        conn.close()

        bot.send_message(message.chat.id, 'Введи своё имя и фамилию, чтобы я мог тебя записать', parse_mode='html')
        bot.register_next_step_handler(message, user_name)

    else:
        bot.send_message(message.chat.id, 'Выбери функцию из меню :)', parse_mode='html')


def user_name(message):
    name = message.text.strip()

    conn = sqlite3.connect('test_db.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO test_table (name) VALUES('%s')" % (name))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    day1 = types.InlineKeyboardButton('Понедельник', callback_data='pn')
    markup.add(day1)
    day2 = types.InlineKeyboardButton('Вторник', callback_data='vt')
    markup.add(day2)
    day3 = types.InlineKeyboardButton('Среда', callback_data='sr')
    markup.add(day3)
    day4 = types.InlineKeyboardButton('Четверг', callback_data='cht')
    markup.add(day4)
    day5 = types.InlineKeyboardButton('Пятница', callback_data='pt')
    markup.add(day5)
    day6 = types.InlineKeyboardButton('Суббота', callback_data='sb')
    markup.add(day6)
    day7 = types.InlineKeyboardButton('Воскресенье', callback_data='vs')
    markup.add(day7)

    bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=markup)
    bot.register_next_step_handler(message, callback_message)


# def nedelya(message):
#     # сохранить mesage.text те сохранить фио
#     markup = types.InlineKeyboardMarkup()
#     day1 = types.InlineKeyboardButton('Понедельник', callback_data= 'pn')
#     markup.add(day1)
#     day2 = types.InlineKeyboardButton('Вторник', callback_data= 'vt')
#     markup.add(day2)
#     day3 = types.InlineKeyboardButton('Среда', callback_data= 'sr')
#     markup.add(day3)
#     day4 = types.InlineKeyboardButton('Четверг', callback_data= 'cht')
#     markup.add(day4)
#     day5 = types.InlineKeyboardButton('Пятница', callback_data= 'pt')
#     markup.add(day5)
#     day6 = types.InlineKeyboardButton('Суббота', callback_data= 'sb')
#     markup.add(day6)
#     day7 = types.InlineKeyboardButton('Воскресенье', callback_data= 'vs')
#     markup.add(day7)
#     bot.send_message(message.chat.id, 'Готово, теперь выбери день', parse_mode='html', reply_markup=markup)
#     bot.register_next_step_handler(message, callback_message)

# def user_nedelya(message):
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Выбери время')
#     bot.register_next_step_handler(message, nedelya)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    if call.data == 'pn':
        day_nedeli = 'Понедельник'
        conn = sqlite3.connect('test_db.sql')
        cur = conn.cursor()

        cur.execute("INSERT INTO test_table (daynedeli) VALUES('%s')" % (day_nedeli))
        conn.commit()
        cur.close()
        conn.close()

        markup = types.InlineKeyboardMarkup()

        time1 = types.InlineKeyboardButton('9-10', callback_data='910')
        markup.add(time1)
        time2 = types.InlineKeyboardButton('10-11', callback_data='1011')
        markup.add(time2)
        time3 = types.InlineKeyboardButton('13-14', callback_data='1314')
        markup.add(time3)

        bot.send_message(call.message.chat.id, 'Понедельник', parse_mode='html', reply_markup=markup)
        # bot.register_next_step_handler(call.message, save_time)

    elif call.data == 'vt':
        day_nedeli = 'Вторник'
        conn = sqlite3.connect('test_db.sql')
        cur = conn.cursor()

        cur.execute("INSERT INTO test_table (daynedeli) VALUES('%s')" % (day_nedeli))
        conn.commit()
        cur.close()
        conn.close()

        markup = types.InlineKeyboardMarkup()

        time1 = types.InlineKeyboardButton('14-15', callback_data='1415')
        markup.add(time1)
        time2 = types.InlineKeyboardButton('15-16', callback_data='1516')
        markup.add(time2)
        time3 = types.InlineKeyboardButton('17-18', callback_data='1617')
        markup.add(time3)

        bot.send_message(call.message.chat.id, 'Вторник', parse_mode='html')
        # bot.register_next_step_handler(call.message.chat.id, save_time)


# @bot.callback_query_handler(func=lambda call: True)
# def save_time(callback):
#     day_time = callback.data
#
#     conn = sqlite3.connect('test_db.sql')
#     cur = conn.cursor()
#
#     cur.execute("INSERT INTO test_table (daytime) VALUES('%s')" % (day_time))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(callback.message.chat.id, 'Готово', parse_mode='html')


bot.polling(non_stop = True)