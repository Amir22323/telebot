import telebot

token = "5864188381:AAEO_QPsiC33SLo22sFOx-jeoIf6GBO8PZ8"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Чем помочь?')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'привет')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "как дела":
        bot.send_message(message.chat.id, 'норм')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "расскажи анекдот":
        bot.send_message(message.chat.id, 'ок')


bot.infinity_polling()