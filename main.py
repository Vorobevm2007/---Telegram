import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import time

bot = telebot.TeleBot('6905629509:AAHNqx1RX6KmapmHjiFXQZTsLWA8Az2_Q4Q')

@bot.message_handler(commands=['start'])
def messag(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width=2)
    SchoolSchedule = types.KeyboardButton('Расписание уроков')
    TheMainMenu = types.KeyboardButton('Основное меню')
    markup.add(SchoolSchedule,TheMainMenu)
    bot.send_message(message.chat.id,'Здравствуйте!\nКлавиатура создана...\nС помощью неё, можно со мно взаимодействовать.\nНажми на кнопку <b><u>"Основное меню",</u></b>\n<i>А дальше сам(а) разберёшься...</i>',reply_markup=markup,parse_mode="html")

@bot.callback_query_handler(func=lambda call:True)
def massage(call):
    if call.message:
        match(call.data):
            case 'MenuForStudents':
                markup = types.InlineKeyboardMarkup(row_width=1)
                UntilTheSummer = types.InlineKeyboardButton('Сколько до конца?📆',callback_data='UntilTheSummer')
                SchoolAnnouncements = types.InlineKeyboardButton('Общешкольные объявления📝',callback_data='SchoolAnnouncements')
                UntilTheEndOfTheLesson = types.InlineKeyboardButton('Сколько до конца урока?🧾',callback_data='UntilTheEndOfTheLesson')
                CallSchedule = types.InlineKeyboardButton('Расписание звонков📃', callback_data='CallSchedule')
                ElectronicMagazine = types.InlineKeyboardButton('Электронный журнал📕',callback_data='ElectronicMagazine')
                SchoolWebsite = types.InlineKeyboardButton('Школьный сайт👩‍💻', callback_data='SchoolWebsite')
                ProninWebsite = types.InlineKeyboardButton('Сайт Пронина А.В.🧑‍💻',callback_data='ProninWebsite')
                Course = types.InlineKeyboardButton('Курс доллара💵', callback_data='Course')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(UntilTheSummer, SchoolAnnouncements, UntilTheEndOfTheLesson, CallSchedule,ElectronicMagazine, SchoolWebsite, ProninWebsite, Course, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Меню учеников',reply_markup=markup)
            case 'MenuForTeacher':
                markup = types.InlineKeyboardMarkup(row_width=1)
                UntilTheSummer = types.InlineKeyboardButton('Сколько до конца?📆', callback_data='UntilTheSummer')
                SchoolAnnouncements = types.InlineKeyboardButton('Общешкольные объявления📝',callback_data='SchoolAnnouncements')
                UntilTheEndOfTheLesson = types.InlineKeyboardButton('Сколько до конца урока?🧾',callback_data='UntilTheEndOfTheLesson')  # ---
                CallSchedule = types.InlineKeyboardButton('Расписание звонков📃', callback_data='CallSchedule')
                ElectronicMagazine = types.InlineKeyboardButton('Электронный журнал📕',callback_data='ElectronicMagazine')
                SchoolWebsite = types.InlineKeyboardButton('Школьный сайт👩‍💻', callback_data='SchoolWebsite')
                Course = types.InlineKeyboardButton('Курс доллара💵', callback_data='Course')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(UntilTheSummer, SchoolAnnouncements, UntilTheEndOfTheLesson, CallSchedule,ElectronicMagazine, SchoolWebsite, Course, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Меню учителей',reply_markup=markup)
            case 'UntilTheSummer':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Exit)
                BASE_URL_BeforeTheSummerHolidays = 'https://www.calc.ru/dney-do-leta.html?hl=ru_RU&amp;ysclid=lf89kzpn8x84005675'
                response = requests.get(BASE_URL_BeforeTheSummerHolidays)
                soup = BeautifulSoup(response.text, 'lxml')
                data = soup.find('div', class_='text')
                namber = data.find('div').text
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=f'До конца учёбы:\n{namber}', reply_markup=markup)
            case 'SchoolAnnouncements':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Site = types.InlineKeyboardButton('Страничка в ВК', url='https://m.vk.com/mbouabramovskaya')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Site, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Страничка в ВК Абрамовской СШ', reply_markup=markup)
            case 'UntilTheEndOfTheLesson':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Pon = types.InlineKeyboardButton('Понедельник', callback_data='Pon')
                Vtor = types.InlineKeyboardButton("Вторник-пятница", callback_data='Vtor')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Pon, Vtor, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Какой сегодня день?',reply_markup=markup)
            case 'Pon':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Exit = types.InlineKeyboardButton('Назад', callback_data='UntilTheEndOfTheLesson')
                markup.add(Exit)
                hour = time.localtime().tm_hour
                min = time.localtime().tm_min
                resultInMin = hour * 60 + min
                prizent = ''
                if resultInMin < 550:
                    prizent = f'Уроки не начались.'
                elif resultInMin > 550 and resultInMin < 590:
                    res = resultInMin - 590
                    prizent = f'1 урок закончится через:{res}минут'
                elif resultInMin > 600 and resultInMin < 640:
                    res = resultInMin - 640
                    prizent = f'2 урок закончится через:{res}минут'
                elif resultInMin > 655 and resultInMin < 695:
                    res = resultInMin - 695
                    prizent = f'3 урок закончится через:{res}минут'
                elif resultInMin > 710 and resultInMin < 750:
                    res = resultInMin - 750
                    prizent = f'4 урок закончится через:{res}минут'
                elif resultInMin > 765 and resultInMin < 805:
                    res = resultInMin - 805
                    prizent = f'5 урок закончится через:{res}минут'
                elif resultInMin > 815 and resultInMin < 855:
                    res = resultInMin - 855
                    prizent = f'6 урок закончится через:{res}минут'
                elif resultInMin > 860 and resultInMin < 900:
                    res = resultInMin - 900
                    prizent = f'7 урок закончится через:{res}минут'
                elif resultInMin > 900:
                    prizent = f'Уроки закончились.'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=prizent,reply_markup=markup)
            case 'Vtor':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Exit = types.InlineKeyboardButton('Назад', callback_data='UntilTheEndOfTheLesson')
                markup.add(Exit)
                hour = time.localtime().tm_hour
                min = time.localtime().tm_min
                resultInMin = hour * 60 + min
                prizent = ''
                if resultInMin < 510:
                    prizent = f'Уроки не начались.'
                elif resultInMin > 510 and resultInMin < 550:
                    res = resultInMin - 550
                    prizent = f'1 урок закончится через:{res}минут'
                elif resultInMin > 560 and resultInMin < 600:
                    res = resultInMin - 600
                    prizent = f'2 урок закончится через:{res}минут'
                elif resultInMin > 615 and resultInMin < 655:
                    res = resultInMin - 655
                    prizent = f'3 урок закончится через:{res}минут'
                elif resultInMin > 670 and resultInMin < 710:
                    res = resultInMin - 710
                    prizent = f'4 урок закончится через:{res}минут'
                elif resultInMin > 725 and resultInMin < 765:
                    res = resultInMin - 765
                    prizent = f'5 урок закончится через:{res}минут'
                elif resultInMin > 775 and resultInMin < 815:
                    res = resultInMin - 815
                    prizent = f'6 урок закончится через:{res}минут'
                elif resultInMin > 825 and resultInMin < 865:
                    res = resultInMin - 865
                    prizent = f'7 урок закончится через:{res}минут'
                elif resultInMin > 865:
                    prizent = f'Уроки закончились.'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=prizent,reply_markup=markup)
            case 'CallSchedule':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Exit)
                result = 'Расписание звонков\nПонедельник:\n1 урок 9:30-9:50\n2 урок 10:00-10:40\n3 урок 10:55-11:35\n4 урок 11:50-12:30\n5 урок 12:45-13:25\n6 урок 13:35-14:15\n7 урок 14:20-15:00\n\nВторник-пятница:\n1 урок 8:30-9:10\n2 урок 9:20-10:00\n3 урок 10:15-10:55\n4 урок 11:10-11:50\n5 урок 12:05-12:45\n6 урок 12:55-13:35\n7 урок 13:45-14:25'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=result,reply_markup=markup)
            case 'ElectronicMagazine':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Site = types.InlineKeyboardButton('edu.gounn.ru',url='https://edu.gounn.ru/authorize?return_uri=%2Fjournal-app%2Fu.112')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Site, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Эл.жур.',reply_markup=markup)
            case 'SchoolWebsite':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Site = types.InlineKeyboardButton('Школьн...', url='https://abramovosc.edusite.ru/')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Site, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Сайт школы:',reply_markup=markup)
            case 'ProninWebsite':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Site = types.InlineKeyboardButton('Сайт Пронина...', url='https://proninavfizika.edu-sites.ru/')
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Site, Exit)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Сайт Пронина А.В.:',reply_markup=markup)
            case 'Course':
                markup = types.InlineKeyboardMarkup(row_width=2)
                Exit = types.InlineKeyboardButton('Назад', callback_data='Menu')
                markup.add(Exit)
                BASE_URL_ = 'https://www.sberometer.ru/?_%7D_&amp&ysclid=lsng8glkpc780067336'
                response = requests.get(BASE_URL_)
                soup = BeautifulSoup(response.text, 'lxml')
                data = soup.find('span', class_='oracleCurrentCurs')
                namber = data.find("span").text
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text=f'Курс доллара:{namber}\nИнформация с сайта:https://www.sberometer.ru/?_%7D_&amp&ysclid=lsng8glkpc780067336',reply_markup=markup)
            case 'Menu':
                markup = types.InlineKeyboardMarkup(row_width=2)
                MenuForStudents = types.InlineKeyboardButton('Меню учеников👨‍🎓', callback_data='MenuForStudents')
                MenufForTeachers = types.InlineKeyboardButton('Меню учителей👨‍🏫', callback_data='MenuForTeacher')
                markup.add(MenuForStudents, MenufForTeachers)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Основное меню',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    match(message.text):
        case "Расписание уроков":
            photo1 = open('images/Понидельник-вторник.jpg', 'rb')
            photo2 = open('images/Среда-четверг.jpg', 'rb')
            photo3 = open('images/Пятница.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1)
            bot.send_photo(message.chat.id, photo2)
            bot.send_photo(message.chat.id, photo3)
        case "Основное меню":
            markup = types.InlineKeyboardMarkup(row_width=2)
            MenuForStudents = types.InlineKeyboardButton('Меню учеников👨‍🎓', callback_data='MenuForStudents')
            MenufForTeachers = types.InlineKeyboardButton('Меню учителей👨‍🏫', callback_data='MenuForTeacher')
            markup.add(MenuForStudents, MenufForTeachers)
            bot.send_message(message.from_user.id, 'Основное меню', reply_markup=markup)
        case _:
            bot.send_message(message.from_user.id, 'Для меня этого не существует.\n<b>Не напрягайте меня.</b>',parse_mode="html")

if __name__ == '__main__':
    bot.polling(none_stop=True)