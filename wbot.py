import requests
import telebot
import random
from telebot import types

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#ключ open weather api
api_telegram_token = '1629247479:AAHFkYhoIOY1VyaOWm4Y0b70m1DHYEMo05Q' #токен telegram api

print("")
print("initialize") #сообщение в консоль

link1 = "https://ivi.ru"
link2 = "https://litres.ru"
link3 = "https://lamoda.ru"
link4 = "https://leroymerlin.ru"

message1 = "Сегодня холодно, оставайтесь дома! А чтобы скрасить вечер можете посмотреть фильм! \n" + link1
message2 = "Если нет желания сегодня гулять, можно устроиться дома в кресле и почитать любую книгу из онлайн-каталога! \n" + link2
message3 = "Если вы еще сменили верхнюю одежду, самое время это сделать! С ассортиментом можете ознакомиться на сайте магазина по ссылке ниже. \n" + link3
message4 = "Дачный сезон можно считать открытым! Семена, рассада, лейки, лопаты, грабли, газонокосилки и прочий садовый инвентарь можно купить в магазине, представленном ниже. \n"

random_message1 = random.choice(message1)
random_message2 = random.choice(message2)
random_message3 = random.choice(message3)
random_message4 = random.choice(message4)


@bot.message_handler(commands=['start']) #старт
def welcome(message):
    bot.send_message(message.chat.id, f'Привет!  {message.from_user.first_name}'
                                      f', напиши мне название города, а я тебе скажу, какая погода в нем!'); #Сообщение при запуске



@bot.message_handler(content_types=['text']) #обработчик
def test(message):
    markup = types.InlineKeyboardMarkup();
    ivi = types.InlineKeyboardButton(text='Перейти на ivi.ru', url=link1);
    litres = types.InlineKeyboardButton(text='Перейти на litres.ru', url=link2);
    lamoda = types.InlineKeyboardButton(text='Перейти на lamoda.ru', url=link3);
    leroymerlin= types.InlineKeyboardButton(text='Перейти на leroymerlin.ru', url=link4);


    city_name = message.text

    try:
        params = {'APPID': api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)#параметры api open weather
        weather = result.json()#экспорт параметров

        if weather["main"]['temp'] < -10:   #от -бесконечно до -10
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/ivi.jpeg', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+message1))
        elif weather["main"]['temp'] < 0:   # - 10 - 0
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/litres.jpeg', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+message2))
        elif weather["main"]['temp'] < 10:  #от 0 до +10
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/lamoda.jpeg', "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]+"\n"+message3))
        else: status = markup.add(leroymerlin)
        bot.send_message(message.chat.id, "??Сейчас в городе " + str(weather["name"])+ " температура " + str(weather["main"]['temp']) + "°C" + "\n" +"??Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" + message4, "")
        bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/sad.jpeg', reply_markup=markup);




    except:
        bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Город " + city_name + " не найден"); # сообщение в случае если город не найден



print("Started!")#сообщение в консоль
bot.polling(none_stop=True, interval=0)
print("")
print("Stopped!")#сообщение в консоль
