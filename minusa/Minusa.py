import telebot
from telebot import types

bot = telebot.TeleBot('Your token')


@bot.message_handler(commands=['start'])
def start_menu(message):
    studrada = '[Студрада НАУ](your url)'
    studcity = '[Студрада Студмістечка](your url)'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_transport = types.KeyboardButton('Транспорт')
    item_settlement = types.KeyboardButton('Поселення')
    item_inf = types.KeyboardButton('Корисна інформація')
    item_life = types.KeyboardButton('Життя в НАУ')
    item_map = types.KeyboardButton('Карта НАУ')
    markup.add(item_transport, item_settlement, item_inf, item_life, item_map)
    bot.send_message(message.chat.id, text="🔵⚪️\nПривіт, мінус.\nЦей бот допоможе вам зорієнтуватися у всесвіті НАУ! ✈️\nПоселення, навчання та все що завгодно — все це тут.\n\nБот від Студентської Ради.\nВід студентів для студентів.\n\n🎓Переходьте на канали, де є всі новини НАУ, та де вам завжди допоможуть: \n\n"+studrada+'\n'+studcity, reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Життя в НАУ')
def life(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_nuzhno = types.KeyboardButton('Розваги і потреби')
    item_each = types.KeyboardButton('Їжа')
    item_health = types.KeyboardButton("Здоров'я")
    item_inside = types.KeyboardButton('Інсайд НАУ')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_nuzhno, item_each, item_health,item_inside, item_back)
    bot.send_message(message.chat.id, text='✈️Життя в НАУ✈️', reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Розваги і потреби')
def life(message):
    bot.send_message(message.chat.id, text='Найближче відділення Нової пошти, біля гуртожитків №120 (вул. Ніжинська, 16)\n\n'
                                           '*ЦКМ* - Центр Культури та Мистецтв - це приміщення, де найчастіше проходять заходи Національного авіаційного університету, а іноді і концерти відомих людей!\n'
                                           'Адреса: проспект Любомира Гузара, 1\n\n'
                                           '*HAU HUB* - (Настільні ігри, заходи і т.д.) - це проект Наукового товариства студентів, аспірантів, докторантів та молодих вчених НАУ.\n'
                                           'Це частина університету, а отже заходи тут безкоштовні, а користуватися простором можуть студенти і викладачі НАУ та інших дружніх університетів.\n'
                                           'Адреса: 4 гуртожиток, Гарматна 53, вхід під муралом\n\n'
                                           '*Narikela RED* - Гарне місце, куди можна сходити на Кальян, з недорогими цінами.\n'
                                           'Адреса: вулиця Миколи Голего, 7в', parse_mode='Markdown')

@bot.message_handler(func=lambda mess: mess.text == 'Інсайд НАУ')
def life(message):
    markup1 = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Стаття',
                                             url='your url')
    markup1.add(btn_my_site)
    bot.send_message(message.chat.id, text='НАУ: легенда - історія, та як тут все працює', reply_markup=markup1)


@bot.message_handler(func=lambda mess: mess.text == 'Їжа')
def life(message):
    map = "[на карті НАУ.](your url)"
    bot.send_message(message.chat.id, text='Всі ці місця можна знайти '+map+'\n\n'
                                                                           '🍽 *Бістро НАУ*\n'
                                                                           '📋 По-студентські та смачно.  Дешево та сердито.\n'
                                                                           '💰 30-70 грн\n\n'
                                                                           '🍕 *Домінос*\n'
                                                                           '📋"Лакшері " їжа для студента.\n'
                                                                           '💰 120-210 грн (велика піца)\n\n'
                                                                           '🥘 *Пузата Хата*\n'
                                                                           '📋 Домашня їжа — борщик, котлетка по київськи.\n'
                                                                           '💰 80-130 грн ( Перше та Друге)\n\n'
                                                                           '🍕 *Піца в 8 корпусі*\n'
                                                                           '📋 Легендарна піца НАУ\n'
                                                                           '💰 18-25 грн\n\n'
                                                                           '*Happy Cake* (територія 4 корпусу)\n'
                                                                           '📋 Перекус, випічка. Саме то між парами.\n'
                                                                           '💰 30-70 грн\n\n'
                                                                           '*Тераса Клубу Forsage (біля 3 гуртожитку)*\n'
                                                                           '📋 Комплексні обіди, кальяни безкоштовно за студентський\n'
                                                                           '💰 50-100 грн', parse_mode='Markdown')

@bot.message_handler(func=lambda mess: mess.text == "Здоров'я")
def life(message):
    bot.send_message(message.chat.id, text='Рекомендуємо звернутися до поліклініки за адресою: Гарматна 36 та оформити договір з сімейним лікарем.\n\n'
                                           'Проте, на території НАУ, також знаходиться МЕДИЧНИЙ ЦЕНТР (АМЦ), вразі якщо ви почуваєте себе погано, у вас підвищена температура, ви можете звернутись до свого терапевта.')


@bot.message_handler(func=lambda mess: mess.text == 'Транспорт')
def transport(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='До НАУ', callback_data=1),
               telebot.types.InlineKeyboardButton(text='Від НАУ', callback_data=2))
    bot.send_message(message.chat.id, text="Виберіть напрям", reply_markup=markup)


@bot.message_handler(func=lambda mess: mess.text == 'Поселення')
def sattlement(message):
    markup1 = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Натисніть для перегдяду алгоритму',
                                             url='your url')
    btn_inf = types.InlineKeyboardButton(text='Про поселення на наступний рік', callback_data=3)
    btn_my_inf = types.InlineKeyboardButton(text='Після поселення',
                                             url='your urll')
    markup1.add(btn_my_site)
    markup1.add(btn_inf)
    markup1.add(btn_my_inf)
    bot.send_message(message.chat.id, "Після прибуття до Києва, у вказану дату заселення, вам необхідно поселитися згідно алгоритму: ", reply_markup=markup1)


@bot.message_handler(func=lambda mess: mess.text == 'Корисна інформація')
def inf(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_first_day = types.KeyboardButton('Перші дні навчання')
    item_kontrakt = types.KeyboardButton('Контрактникам')
    item_obshchaga = types.KeyboardButton('Для мешканців гуртожитку')
    item_dekanat = types.KeyboardButton('Відділи, деканати, кабінети')
    item_back = types.KeyboardButton('На головну')
    markup.add(item_first_day, item_dekanat, item_kontrakt, item_obshchaga, item_back)
    bot.send_message(message.chat.id, text='Виберіть необхідний вам пункт', reply_markup=markup)

@bot.message_handler(func=lambda mess: mess.text == 'Перші дні навчання')
def inf(message):
    text = '[Посиланням.](your url)'
    text2 = '[посиланням.](your url)'
    bot.send_message(message.chat.id, text='Ознайомитися з картою НАУ, розташування корпусів навчання та гуртожитків, можна за '+text+
                                           '\n\nВхід до 5, 2 та 3 корпусів, здійснюється через 4 корпус!\n\n'
                                           'Кожна аудиторія має свій номер, виду 1.234, де:\n'
                                           'де "1", це номер корпусу;\n'
                                           'де "2", це поверх корпусу;\n'
                                           'де "34", це номер аудиторії;\n\n'
                                           'Перелік необхідних робочих телефонів Кафедр, деканатів, мед центру, приймальної комісії і т.д, можна дізнатися за '+text2, parse_mode="Markdown")


@bot.message_handler(func=lambda mess: mess.text == 'Відділи, деканати, кабінети')
def inf(message):
    bot.send_message(message.chat.id, text='✈️*Відділи:*\n\n''*Відділ розрахунків по стипендіях*\n'
                                           'Начальник – Болінчук Надія Павлівна\n'
                                           'кабінет 1.243, тел. +38 (044) 46666666\n\n'
                                           '*Відділ обліку касових та розрахункових операцій*\n'
                                           'Начальник – Ковальчук Оксана Геннадіївна\n'
                                           'кабінет 1.247, тел. +38 (044) 406666666\n\n'
                                           '*Бухгалтерія СМ (студмістечка)*\n'
                                           'Заступник головного бухгалтера – Муляр Галина Миколаївна\n'
                                           'гуртожиток № 3, кабінет 14, тел. +38 (044) 406666665\n\n'
                                           '*Відділ організаційної роботи зі студентами*\n'
                                           'Заступник головного бухгалтера – Хмелюк Алла Анатоліївна\n'
                                           'кабінет 8.001, тел. +38 (044)6666666', parse_mode='Markdown')
    bot.send_message(message.chat.id, text='✈️*Деканати факультетів:*\n\n'
                                           '*ФККПІ* - Дирекція: ауд. 5.206, тел.: +38 (044) 40666666666;\n'
                                           '*ФАЕТ* - Дирекція: ауд. 5.410, тел.: +38 (044) 40866666;\n'
                                           '*ФЛСК* - Дирекція: ауд. 8.807, тел.: +38 (044) 40666666;\n'
                                           '*ФЕБІТ* - Дирекція: ауд. 5.202, тел.: +38 (044) 4066666;\n'
                                           '*АКФ* - Дирекція: ауд. 1.350, тел.: +38 (044) 406666666;\n'
                                           '*ФЕБА* - Дирекція: ауд. 2.210 , тел.: +38 (044) 406666666;\n'
                                           '*ФТМЛ* - Дирекція: ауд. 2.206, тел.: +38 (044) 406666666;\n'
                                           '*ФМВ* - Дирекція: ауд. 7.206, тел.: +38 (044) 406666666;\n'
                                           '*ФАБД* - Дирекція: ауд. 3.220, тел.: +38 (044) 46466666;\n'
                                           '*ЮФ* - Дирекція: ауд. , тел.: +38 (044) 466666;\n'
                                           '*КВП* - Дирекція: ауд. , тел.: +38 (044) 6666666;', parse_mode='Markdown')


@bot.message_handler(func=lambda mess: mess.text == 'Контрактникам')
def inf(message):
    bot.send_message(message.chat.id, text='За квитанціями *Оплати навчання* та термінами їх сплати, звертатися до Відділу організаційної роботи зі студентами.', parse_mode='Markdown')
    bot.send_message(message.chat.id, text='*Відділ організаційної роботи зі студентами:*\n'
                                           'Заступник головного бухгалтера – Хмелюк Алла Анатоліївна\n'
                                           'кабінет 8.001, тел. +38 (044) 6666666', parse_mode='Markdown')

@bot.message_handler(func=lambda mess: mess.text == 'Для мешканців гуртожитку')
def inf(message):
    markup1 = types.InlineKeyboardMarkup()
    btn_my_inf = types.InlineKeyboardButton(text='Стаття',
                                            url='your url')
    markup1.add(btn_my_inf)
    bot.send_message(message.chat.id, text='Як облаштувати кімнату та як влаштоване життя гуртожитку', reply_markup=markup1)


@bot.message_handler(func=lambda mess: mess.text == 'Карта НАУ')
def map(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти до карти НАУ",
                                            url="https://www.google.com/maps/d/edit?mid=1VDlRakwBo9f5-rBqx6bm4tMvt8bbu3pr&usp=sharing")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Для перегляду карти, натисність кнопку",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Зачекайте, ваш запит оброблюється')
    if call.data == '1':
        bot.send_message(call.message.chat.id, "Від ЖД вокзалу: зі станції Вокзальна - трамвай №1, 3 - до станції Національний авіаційний університет.")
    elif call.data == '2':
        bot.send_message(call.message.chat.id,text='*До найближчого метро:*\n\n'
                                                   '*1 та 3* трамваї (До станції "Політехнічний інститут")\n'
                                                   '*1 та 3* трамваї (До станції "Вокзальна")\n\n'
                                                   '*До центру:*\n\n'
                                                   '- Майдан Незалежності - 1 та 3 трамваї (До станції Метро "Політехнічний інститут") — Станція Хрещатик\n'
                                                   '- ТРЦ "Гулівер", стадіон "Олімпійський" - Маршрутка №411, Автобус № 69\n\n'
                                                   '*Для оформлення документів:*\n\n'
                                                   "ЦНАП - Маршрутка *№401*\n"
                                                   "Солом'янський РВК (воєнкомат) - Маршрутка *№401*", parse_mode="Markdown")
    elif call.data == '3':
        bot.send_message(call.message.chat.id,
                         text='Квитанцію на оплату гуртожитку, а також інформацію, що до термінів сплати, можна взяти в *Бухгалтерію*.\n\n'
                              'Поселення в гуртожиток на наступний рік, відбувається таким чином:\n\n'
                              '\tЗа першим списком: \n\n'
                              '\t\t1. Студенти, які мають високі середні бали(наприклад 2020 рік, для ФККПІ, для поселення на другий курс, за першими списками, >4.6 бала))\n'
                              '\t\t2. Студенти, які мають певні пільги.\n'
                              '\t\t3.Студенти, які є членами СРГ(Студентської дари гуртожитків).\n\n'
                              '\tЗа другим списком:\n'
                              '\t\t1.Студенти, які мають мають гарний середній бал, але не пройшли по першим спискам.\n\n'
                              'Як потрапити до СРГ (Студради гуртожитку) :\n'
                              "Напишіть в бот СР СМ / зверніться до представника СРГ, вони нададуть повну інформацію щодо обов'язків та умов вступу.",
                         parse_mode='Markdown')
        markup3 = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Натисніть на кнопку',
                                                 url='your url')
        markup3.add(btn_my_site)
        bot.send_message(call.message.chat.id, "Бот СР СМ", reply_markup=markup3)

@bot.message_handler(func=lambda mess: mess.text == 'На головну')
def back(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_transport = types.KeyboardButton('Транспорт')
    item_settlement = types.KeyboardButton('Поселення')
    item_inf = types.KeyboardButton('Корисна інформація')
    item_life = types.KeyboardButton('Життя в НАУ')
    item_map = types.KeyboardButton('Карта НАУ')
    markup.add(item_transport, item_settlement, item_inf, item_life, item_map)
    bot.send_message(message.chat.id, 'З поверненням', reply_markup=markup)


bot.polling(none_stop=True)
