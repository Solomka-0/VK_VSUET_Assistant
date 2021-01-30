import datetime
import random
import time

import data

greeting_massage = '''\nТебя приветствует онлайн-помощник ВГУИТ. Я отвечу на вопросы абитуриента и помогу с ответом на другие. Если ты интерисуешься поступлением в наш университет, то есть специальный каталог, который тебе поможет. Для работы с ним поменяй режим работы командой "/assistant".
В любом случае, тебе может пригодиться меню, для его вызова есть команда "/menu", ну и "/hide" для того чтобы его спрятать. Думаю, ты разберешься!'''
requests_time = {}

# Утренние приветствия
def morning_greeting(first_name):
    greating_list = [f'Доброе утро, человек или {first_name}. ⏰🤗', 'Утречка :3\n', 'Прекрасное утро, не правда ли? 🌞',
    'Доброе утро, соня :3\n', 'Лучше бы размялся, а не садился сразу за компьютер. 💪', 'Доброе утро, как поживаешь? 😉']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Дневные приветствия
def afternoon_greeting(first_name, day_time):
    greating_list = [f'Добрый день, человек или {first_name}.', 'Добрый день, браток.', 'Привет, как поживаешь? 🎧',
    'Привет, как дела? 🙇🔨', 'Здарова, человечишка. 🤖', f'Хм.. Уже {day_time} часов. 😲']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Вечерние приветствия
def evening_greeting(first_name):
    greating_list = ['Доброго вечера. 🌙🌠', 'Привет. День подходит к концу..',
    'Тьма спустилась в этот мир.', 'Привет. Отдыхаешь? Здорово. C: \n', 'Ум-м.. Уже темнеет!..']
    return greating_list[random.randint(0, len(greating_list)-1)]

# Ночные приветствия
def night_greeting(first_name):
    greating_list = ['Не спится, да? 🗿', 'Тебе следует лечь в кровать, человек. 🤖',
    'Дневная суета никак не покинет твоего тела, человек?', f'Доброй ночи, {first_name}.', 'Привет. Тебе нужен сон.'
    '1101000010010111110100001011010011010001100000001101000010110000110100001011001011010000101110001101000110001111001000001101000010110110110100001011010111010000101110111101000010110000110100011000111000101100001000001101000010111111110100001011111011010001100000101101000010111110110100001011110011010000101111101101000010111010001000001101000010111110110100001011000111010000101101011101000010110111110100011000110011010001100011111101000010111101'
    'Тебе следует лечь спать, человек.⏰']
    return greating_list[random.randint(0, len(greating_list)-1)]

def random_greeting(first_name):
    day_time = int(datetime.datetime.now().hour)
    if day_time>=5 and day_time<=10:
        return morning_greeting(first_name)
    elif day_time>=11 and day_time<=15:
        return afternoon_greeting(first_name, day_time)
    elif day_time>=16 and day_time<=22:
        return evening_greeting(first_name)
    elif day_time>=23 and day_time<=4:
        return night_greeting(first_name)

def dict_to_list(dictionary): # Переводит словарь в массив с ключами
    try:
        return list(dictionary.keys())
    except:
        return list(dictionary)

def in_stream(user_id): # Проверяет есть ли id пользователья в requests_time. Возвращает bool
    global requests_time
    array = []
    array = dict_to_list(requests_time).copy()
    for element in array:
        if element == user_id:
            return True
    return False

def form_request(user_id, text, users, admins):
    output = {}
    output[user_id] = data.rand_el(data.notification)
    for id in admins:
        output[id] = f'{users.find_value("user_id", user_id)["first_name"]} задал(-а) вопрос: "' + text + '"'
    return output

def notify_admins(user_id, text, users, admins):
    global requests_time

    day_time = int(time.time() / 100)
    if in_stream(user_id) == False:
        requests_time[user_id] = day_time
        return form_request(user_id, text, users, admins)
    else:
        t_1 = requests_time[user_id]
        t_2 = day_time
        print(t_1, t_2)
        requests_time[user_id] = day_time
        if (t_2 - t_1) >= 20 or (t_2 - t_1) < 0:
            return form_request(user_id, text, users, admins)
