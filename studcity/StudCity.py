import telebot
from telebot import types

bot = telebot.TeleBot(Your Token)


@bot.message_handler(commands=['start'])
def start_menu(message):
    bot1="[Бот зв'язку СР СМ](your url)"
    bot2="[Бот зв'язку СР НАУ](your url)"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_reply = types.KeyboardButton('Залишити анонімне повідомлення')
    item_rating = types.KeyboardButton('Оплата гуртожитку')
    item_link = types.KeyboardButton('Інформаційний лист')
    markup.add(item_reply, item_rating, item_link)
    bot.send_message(message.chat.id, "Ви звернулися за анонімною допомогою\n до Студентської Ради. 🔵⚪️ \n\nФакт корупції, неправомірних дій — допоможемо вирішити.\n\n"+bot1+"\n"+bot2, reply_markup=markup, parse_mode = 'Markdown')


@bot.message_handler(func=lambda mess: mess.text == 'Залишити анонімне повідомлення')
def not_anonymous(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_reply = types.KeyboardButton('Написати свій відгук')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_reply, item_back)
    bot.send_message(message.chat.id,
                     text='Для написання анонімного повідомлення натисність "Написати свій відгук".',
                     reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Написати свій відгук', content_types=["text"])
def anonymous_question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_back = types.KeyboardButton('На головну')
    markup.add(item_back)

    chatid = -1001439324326

    if message.text == "Написати свій відгук":
        markup2 = telebot.types.ReplyKeyboardRemove()
        send = bot.send_message(message.chat.id, "Увага❗️\n\nЩоб ми були в змозі вирішити вашу проблему — опишіть її повністю.\n\nТак як ми не будемо знати, хто звернувся, та не зможемо зв'язатися з вами\nнам потрібна повна інформація.", reply_markup=markup2)
        bot.register_next_step_handler(send, anonymous_question)
    else:
        bot.send_message(message.chat.id, 'Дякую за відгук, натисніть "На головну" для подальшого вибору',
                         reply_markup=markup)
        if message.text == "На головну":
            send = message.text
            bot.register_next_step_handler(send, question)
        else:
            bot.send_message(chat_id=chatid, text=message.text)



@bot.message_handler(func=lambda mess: mess.text == "Оплата гуртожитку")
def payment(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_privat = types.KeyboardButton('Приватбанк')
    item_monobank = types.KeyboardButton('Монобанк')
    item_map_bank = types.KeyboardButton('Банки поряд')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_privat, item_monobank, item_map_bank, item_back)
    bot.send_message(message.chat.id, text='Тут я можу допомогти вам оплатити гуртожиток через інтернет, або показати найближчий банк поряд.', reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Приватбанк')
def payment(message):
    bot.send_message(message.chat.id, text='Інструкція по оплаті гуртожитку')
    bot.send_photo(message.chat.id,
                   photo='your url',
                   parse_mode='HTTP')
    bot.send_photo(message.chat.id,
                   photo='your url',
                   parse_mode='HTTP')


@bot.message_handler(func=lambda mess: mess.text == 'Монобанк')
def payment(message):
    bot.send_message(message.chat.id, text='Інструкція по оплаті гуртожитку')
    bot.send_photo(message.chat.id,
                   photo='your url',
                   parse_mode='HTTP')
    bot.send_photo(message.chat.id,
                   photo='your url',
                   parse_mode='HTTP')


@bot.message_handler(func=lambda mess: mess.text == 'Банки поряд')
def payment(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_privat = types.KeyboardButton('Відділ Приватбанку')
    item_alfa = types.KeyboardButton('Відділ Альфабанку')
    item_pumb = types.KeyboardButton('Відділ Пумб')
    item_ukrgaz = types.KeyboardButton('Відділ Укргазбанк')
    item_back = types.KeyboardButton('Назад')
    item_exit = types.KeyboardButton('На головну')
    markup.add(item_privat, item_alfa, item_pumb, item_ukrgaz, item_back, item_exit)
    bot.send_message(message.chat.id, text='Виберіть зручний для вас банк', reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Назад')
def payment(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_privat = types.KeyboardButton('Приватбанк')
    item_monobank = types.KeyboardButton('Монобанк')
    item_map_bank = types.KeyboardButton('Банки поряд')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_privat, item_monobank, item_map_bank, item_back)
    bot.send_message(message.chat.id, text='Тут я можу допомогти вам оплатити гуртожиток через інтернет, або показати найближчий банк поряд.', reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Відділ Приватбанку')
def payment(message):
    bot.send_location(message.chat.id, latitude=50.438826, longitude=30.439630)


@bot.message_handler(func=lambda mess: mess.text == 'Відділ Альфабанку')
def payment(message):
    bot.send_location(message.chat.id, latitude=50.441167, longitude=30.432694)


@bot.message_handler(func=lambda mess: mess.text == 'Відділ Пумб')
def payment(message):
    bot.send_location(message.chat.id, latitude=50.441268, longitude=30.432736)


@bot.message_handler(func=lambda mess: mess.text == 'Відділ Укргазбанк')
def payment(message):
    bot.send_location(message.chat.id, latitude=50.440877, longitude=30.431011)


@bot.message_handler(func=lambda mess: mess.text == 'Інформаційний лист')
def link(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на канал НАУ",
                                            url="your url")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привіт, нажми на кнопку для перегляду корисної інформації", reply_markup=keyboard)


@bot.message_handler(func=lambda mess: mess.text == 'На головну' and mess.content_type == 'text')
def back_choose_city(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_questions = types.KeyboardButton('Написати СР СМ НАУ')
    item_reply = types.KeyboardButton('Залишити анонімне повідомлення')
    item_map = types.KeyboardButton('Завантажити карту НАУ')
    item_rating = types.KeyboardButton('Оплата гуртожитку')
    item_donat_description = types.KeyboardButton('Опис Студкошту')
    item_donat = types.KeyboardButton('Студкошт')
    item_link = types.KeyboardButton('Інформаційний лист')
    markup.add(item_reply, item_rating, item_link)
    bot.send_message(message.chat.id, "З поверненням", reply_markup=markup)


bot.polling(none_stop=True)
