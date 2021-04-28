import requests
import telebot
import random

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#ключ open weather api
api_telegram_token = '1687680321:AAHm7NH2ZsagoBAlcfNSV8U5Wwj0U9jhHK0' #токен telegram api

print("")
print("initialize") #сообщение в консоль

bot = telebot.TeleBot(api_telegram_token)

message1 = ['Сегодня холодно, оставайтесь дома! А чтобы скрасить вечер можете посмотреть фильм!']
message2 = ['Если нет желания сегодня гулять, можно устроиться дома в кресле и почитать любую книгу из онлайн-каталога!']
message3 = ['Если вы еще сменили верхнюю одежду, самое время это сделать! С ассортиментом можете ознакомиться на сайте магазина по ссылке ниже.']
message4 = ['Дачный сезон можно считать открытым! Семена, рассада, лейки, лопаты, грабли, газонокосилки и прочий садовый инвентарь можно купить в магазине, представленном ниже.']

random_message1 = random.choice(message1)
random_message2 = random.choice(message2)
random_message3 = random.choice(message3)
random_message4 = random.choice(message4)

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
