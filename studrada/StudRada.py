import telebot
from telebot import types

bot = telebot.TeleBot('Your token')


@bot.message_handler(commands=['start'])
def start_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_reply = types.KeyboardButton('Залишити анонімне повідомлення')
    item_rating = types.KeyboardButton('Рейтинг')
    item_link = types.KeyboardButton('Інформаційний лист')
    markup.add(item_reply, item_rating,  item_link)
    bot.send_photo(message.chat.id, photo='your url', parse_mode='HTTP')
    bot.send_message(message.chat.id, "Привіт!\nТут ви можете проконсультуватися з будь-яких питань НАУ.\nНапишіть — ми відповімо.", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Залишити анонімне повідомлення')
def not_anonymous(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_reply = types.KeyboardButton('Написати свій відгук')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_reply, item_back)
    bot.send_message(message.chat.id,
                     text='Для написання анонімного повідомлення натисність "Написати свій відгук".\nВаш відгук буде відправлено в групу СР НАУ',
                     reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Написати свій відгук', content_types=["text"])
def anonymous_question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_back = types.KeyboardButton('На головну')
    markup.add(item_back)

    chatid = -478102820

    if message.text == "Написати свій відгук":
        markup2 = telebot.types.ReplyKeyboardRemove()
        send = bot.send_message(message.chat.id, 'Напишіть свій відгук, та натисніть відправити', reply_markup=markup2)
        bot.register_next_step_handler(send, anonymous_question)
    else:
        bot.send_message(message.chat.id, 'Дякую за відгук, натисніть "На головну" для подальшого вибору',
                         reply_markup=markup)
        if message.text == "На головну":
            send = message.text
            bot.register_next_step_handler(send, question)
        else:
            bot.send_message(chat_id=chatid, text=message.text)


@bot.message_handler(func=lambda mess: mess.text == 'Рейтинг')
def rating(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='АКФ', callback_data=1),
               telebot.types.InlineKeyboardButton(text='ФАЕТ', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='ФАБД', callback_data=3),
               telebot.types.InlineKeyboardButton(text='ФЕБІТ', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='ФЕБА', callback_data=5),
               telebot.types.InlineKeyboardButton(text='ФККПІ', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='ФЛСК', callback_data=7),
               telebot.types.InlineKeyboardButton(text='ФМВ', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='ФТМЛ', callback_data=9),
               telebot.types.InlineKeyboardButton(text='ЮФ', callback_data=10))
    bot.send_message(message.chat.id, text="Виберіть факультет", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Зачекайте, рейтинг вашого факультету завантажується!')
    if call.data == '1':
        markup1 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='your url')
        markup1.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup1)
    elif call.data == '2':
        markup2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_1 = types.KeyboardButton('1 курс')
        item_2 = types.KeyboardButton('2 курс')
        item_3 = types.KeyboardButton('3 курс')
        item_4 = types.KeyboardButton('5 курс')
        item_5 = types.KeyboardButton('1 стн курс')
        item_6 = types.KeyboardButton('2 стн курс')
        item_back = types.KeyboardButton('На головну')
        markup2.add(item_1, item_2, item_3, item_4, item_5, item_6, item_back)
        bot.send_message(call.message.chat.id, "Виберіть курс", reply_markup=markup2)
    elif call.data == '3':
        markup3 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='your url')
        markup3.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup3)
    elif call.data == '4':
        markup4 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='your url')
        markup4.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup4)
    elif call.data == '5':
        markup5 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть сюди',
                                                 url='htyour url')
        markup5.add(btn_my_site)
        bot.send_message(call.message.chat.id, text='Ваш рейтинг знаходиться тут', reply_markup=markup5)
    elif call.data == '6':
        markup6 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть сюди',
                                                 url='https://docs.google.com/spreadsheets/d/1i2T96ChhAQDD6_buQED4Uz6rIkBlh9JG/edit#gid=616102691')
        markup6.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup6)
    elif call.data == '7':
        markup7 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть сюди',
                                                 url='https://drive.google.com/file/d/18-Y5u96DpWWFExEG3bml9Pklv82kVwIo/view')
        markup7.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup7)
    elif call.data == '8':
        markup8 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='hyour url')
        markup8.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup8)
    elif call.data == '9':
        markup9 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть сюди', url='your url')
        markup9.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup9)
    elif call.data == '10':
        markup10 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='your url')
        markup10.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup10)


@bot.message_handler(func=lambda mess: mess.text == '1 курс')
def kurs_one(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='your url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == '2 курс')
def kurs_two(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='your url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == '3 курс')
def kurs_three(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='hyour url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == '5 курс')
def kurs_five(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='your url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == '1 стн курс')
def kurs_one_stn(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='your url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == '2 стн курс')
def kurs_two_stn(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                             url='your url')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Ваш рейтинг знаходиться тут", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Інформаційний лист')
def link(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на канал НАУ",
                                            url="your url")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привіт, нажми на кнопку для перегляду корисної інформації", reply_markup=keyboard)


@bot.message_handler(func=lambda mess: mess.text == 'На головну' and mess.content_type == 'text')
def back_choose_city(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_reply = types.KeyboardButton('Залишити анонімне повідомлення')
    item_rating = types.KeyboardButton('Рейтинг')
    item_link = types.KeyboardButton('Інформаційний лист')
    markup.add(item_reply, item_rating,  item_link)
    bot.send_message(message.chat.id, "З поверненням", reply_markup=markup)


bot.polling(none_stop=True)
