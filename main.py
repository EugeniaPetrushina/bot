import telebot
from telebot import types
bot = telebot.TeleBot('5205850102:AAF93gC5k5FoDVQOmZU3BFdN4GkE7rMtZTc')

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "👋 Главное меню" or ms_text == "Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)
    elif ms_text == "/dog" or ms_text == "Прислать собаку":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Красивую")
        btn2 = types.KeyboardButton("Смешную")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id,  text="Какую собаку?", reply_markup=markup)
    elif ms_text == "Красивую":
        img = open('собака4.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif ms_text == "Смешную":
        img = open('собака1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif ms_text == "Прислать анекдот":
        bot.send_message(chat_id, text="еще не готово...")
    elif ms_text == "WEB-камера":
        bot.send_message(chat_id, text="еще не готово...")
    elif ms_text == "Управление":
        bot.send_message(chat_id, text="еще не готово...")
    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, text="Автор: Петрушина Евгения")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/evgptr")
        key1.add(btn1)
        img = open('кот1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
    else:
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: "
                                   + ms_text)
bot.polling(none_stop=True, interval=0)


