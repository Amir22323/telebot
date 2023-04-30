import telebot

from weather import get_weather

token = "5864188381:AAEO_QPsiC33SLo22sFOx-jeoIf6GBO8PZ8"
weather_key = "7080b85d03b618cd74a84a0fa43249d3"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'Я ничего не умею :(')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'привет')
    elif message.text.lower() == "погода":
        city = "Пушкино"
        data = get_weather(weather_key, city)
        print(data)
        message_answer = "Место:{city} \r\nТемпература:{temp}".format(city=data['name'],
                                                    temp=data['main']['temp'])
        bot.send_message(message.chat.id, message_answer)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял')




bot.infinity_polling()