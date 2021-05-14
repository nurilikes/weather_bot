import requests
import telebot
import random
from telebot import types

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#���� open weather api
api_telegram_token = '1629247479:AAHFkYhoIOY1VyaOWm4Y0b70m1DHYEMo05Q' #����� telegram api

print("")
print("initialize") #��������� � �������

bot = telebot.TeleBot(api_telegram_token)

link1 = "https://ivi.ru"
link2 = "https://litres.ru"
link3 = "https://lamoda.ru"
link4 = "https://leroymerlin.ru"

message1 = "?������� �������, ����������� ����! � ����� �������� ����� ������ ���������� �����! \n" + link1
message2 = "?���� ��� ������� ������� ������, ����� ���������� ���� � ������ � �������� ����� ����� �� ������-��������! \n" + link2
message3 = "?���� �� ��� ������� ������� ������, ����� ����� ��� �������! � ������������� ������ ������������ �� ����� �������� �� ������ ����. \n" + link3
message4 = "?������ ����� ����� ������� ��������! ������, �������, �����, ������, ������, ������������� � ������ ������� ��������� ����� ������ � ��������, �������������� ����. \n"

random_message1 = random.choice(message1)
random_message2 = random.choice(message2)
random_message3 = random.choice(message3)
random_message4 = random.choice(message4)




@bot.message_handler(commands=['start']) #�����
def welcome(message):
    bot.send_message(message.chat.id, f'������!  {message.from_user.first_name}'
                                      f', ������ ��� �������� ������, � � ���� �����, ����� ������ � ���!'); #��������� ��� �������



@bot.message_handler(content_types=['text']) #����������
def test(message):
    markup = types.InlineKeyboardMarkup();
    ivi = types.InlineKeyboardButton(text='������� �� ivi.ru', url=link1);
    litres = types.InlineKeyboardButton(text='������� �� litres.ru', url=link2);
    lamoda = types.InlineKeyboardButton(text='������� �� lamoda.ru', url=link3);
    leroymerlin= types.InlineKeyboardButton(text='������� �� leroymerlin.ru', url=link4);


    city_name = message.text

    try:
        params = {'APPID': api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)#��������� api open weather
        weather = result.json()#������� ����������

        if weather["main"]['temp'] < -10:   #�� -���������� �� -10
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/ivi.jpeg', "������ � ������ " + str(weather["name"]) + " ����������� " +
                         str(weather["main"]['temp']) + "�C" + "\n" +
                         "���������: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "�� ����� ������ " + str(weather['weather'][0]["description"]+"\n"+message1))
        elif weather["main"]['temp'] < 0:   # - 10 - 0
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/litres.jpeg', "������ � ������ " + str(weather["name"]) + " ����������� " +
                         str(weather["main"]['temp']) + "�C" + "\n" +
                         "���������: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "�� ����� ������ " + str(weather['weather'][0]["description"]+"\n"+message2))
        elif weather["main"]['temp'] < 10:  #�� 0 �� +10
            status = bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/lamoda.jpeg', "������ � ������ " + str(weather["name"]) + " ����������� " +
                         str(weather["main"]['temp']) + "�C" + "\n" +
                         "���������: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "�� ����� ������ " + str(weather['weather'][0]["description"]+"\n"+message3))
        else: status = markup.add(leroymerlin)
        bot.send_message(message.chat.id, "??������ � ������ " + str(weather["name"])+ " ����������� " + str(weather["main"]['temp']) + "�C" + "\n" +"??���������: " + str(int(weather['main']['humidity'])) + "%" + "\n" + message4, "")
        bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/sad.jpeg', reply_markup=markup);




    except:
        bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "����� " + city_name + " �� ������"); # ��������� � ������ ���� ����� �� ������



print("Started!")#��������� � �������
bot.polling(none_stop=True, interval=0)
print("")
print("Stopped!")#��������� � �������
