import requests
import telebot
import random

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#ключ open weather api
api_telegram_token = '1687680321:AAHm7NH2ZsagoBAlcfNSV8U5Wwj0U9jhHK0' #токен telegram api

print("")
print("initialize") #сообщение в консоль

bot = telebot.TeleBot(api_telegram_token)

message1 = ['На улице холодно, одевайтесь теплее! Чтобы согреться, могу предложить Вам сходить в ресторан и выпить чашечку кофе! (здесь может быть ваша реклама ресторана)', 
	    'Мороз и солнце, день чудесный! Самое время выпить глинтвейн на уютном диване в самом лучшем кафе твоего города! (реклама кафе)', 
	    '"1.3"', '"1.4"','"1.5"']
message2 = ['"2.1"', '"2.2"', '"2.3"', '"2.4"','"2.5"']
message3 = ['"3.1"', '"3.2"', '"3.3"', '"3.4"','"3.5"']
message4 = ['"4.1"', '"4.2"', '"4.3"', '"4.4"','"4.5"']
message5 = ['"5.1"', '"5.2"', '"5.3"', '"5.4"','"5.5"']

random_message1 = random.choice(message1)
random_message2 = random.choice(message2)
random_message3 = random.choice(message3)
random_message4 = random.choice(message4)
random_message5 = random.choice(message5)

@bot.message_handler(commands=['start']) #старт
def welcome(message):
    bot.send_message(message.chat.id, f'Привет!  {message.from_user.first_name}'
                                      f' напиши название города и узнай погоду в нём.') #Сообщение при запуске

@bot.message_handler(content_types=['text']) #обработчик
def test(message):
    city_name = message.text

    try:
        params = {'APPID': api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)#параметры api open weather
        weather = result.json()#экспорт параметров

        if weather["main"]['temp'] < -10:   #при -10
            status = bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+random_message1))
        elif weather["main"]['temp'] < 0:   #при 0
            status = bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+random_message2))
        elif weather["main"]['temp'] < 10:  #при +10
            status = bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+random_message3))
        elif weather["main"]['temp'] < 30:  #при +30
            status = bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+random_message4))
        else:   #при +30+
            status = bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+random_message5))
	
       # bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
       #                 str(weather["main"]['temp']) + "°C" + "\n" +
       #                 "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
       #                 "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
       #                 "-------------------------------------------------------------------"
       #                 "\n" + status)

    except:
        bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Город " + city_name + " не найден") # сообщение в случае если город не найден
		
print("Started!")#сообщение в консоль
bot.polling(none_stop=True)
print("")
print("Stopped!")#сообщение в консоль
