import datetime
import random
import time

import data
from data import answers
greeting_message = '''Тебе нужна помощь, да? Буду рад ответить на твои вопросы, но для начала выбери интересующий тебя раздел при помощи клавиатуры ⬇
"Общие вопросы" - Выбирай эту категорию, если ты студент или есть проблемы или вопросы, связанные с нашим ВУЗом.
"Абитуриенту" - Этот пункт расскажет о направлениях подготовки Воронежского государственного университета инженерных технологий. Очень полезный режим 😉
"По вопросам маркетинга" - Если у Вас есть предложение связанное с публикациями, то выбирайте этот пункт для более быстрого реагирования на него.'''

introductory_student = 'Есть вопрос или проблема? Я постараюсь разобраться. Даже если не смогу тебе помочь, то тебе обязательно ответит администратор, я его оповещу!'
introductory_entrant = '''Прекрасно! Интересуешься поступлением в этот универ? Специально для тебя есть каталог,
в котором можно найти ответы на большинство интересующих тебя вопросов.
Не нашел ответа? Переходи в раздел для студентов, там тебе точно ответят! ("/student_mode")'''
introductory_ad = 'Если у вас есть рекламное предложение или просьба о публикации - пишите сюда, вскоре это рассмотрит администрация.'
introductory_timetable = 'Расписание - это то что нас всех объединяет! Если ты впервые в этом разделе, то нажми кнопку "Смена персональной информации", чтобы настроить фильтры поиска расписания. Для того, чтобы просмотреть занятия выбери кнопку с нужным тебе днем недели.'

requests_time = {}

# Утренние приветствия
def morning_greeting(first_name):
    greeting_list = [f'Доброе утро, человек или {first_name}. ⏰🤗 ', 'Утречка :3\n ', 'Прекрасное утро, не правда ли? 🌞 ',
    'Доброе утро, соня :3\n', 'Лучше бы размялся, а не садился сразу за компьютер. 💪 ', 'Доброе утро, как поживаешь? 😉 ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Дневные приветствия
def afternoon_greeting(first_name, day_time):
    greeting_list = [f'Добрый день, человек или {first_name}. ', 'Аа.. Вот ты где!) ', 'Привет, как поживаешь? ',
    'Привет, как дела? 🙇🔨 ', 'Здарова, человечишка. 🤖 ', f'Хм.. Уже {day_time} часов. 😲 ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Вечерние приветствия
def evening_greeting(first_name):
    greeting_list = ['Доброго вечера. 🌙🌠 ', 'Привет. День подходит к концу.. ',
    'Привет. Отдыхаешь?\n ', 'Наслаждаюсь вечером.. Привет! ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Ночные приветствия
def night_greeting(first_name):
    greeting_list = ['Не спится, да? 🗿 ', 'Тебе следует лечь в кровать, человек. 🤖 ',
    'Дневная суета никак не покинет твоего тела? ', f'Доброй ночи, {first_name}. ', 'Привет. Сон очень важен, поэтому постарайся заснуть как можно скорее! '
    '1101000010010111110100001011010011010001100000001101000010110000110100001011001011010000101110001101000110001111001000001101000010110110110100001011010111010000101110111101000010110000110100011000111000101100001000001101000010111111110100001011111011010001100000101101000010111110110100001011110011010000101111101101000010111010001000001101000010111110110100001011000111010000101101011101000010110111110100011000110011010001100011111101000010111101\n'
    'Тебе следует лечь спать, человек.⏰ ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

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

def form_request(user_id, text, users, mode = 'student'):
    if mode == 'student':
        admins = data.student_adm.copy()
        output = {}
        output[user_id] = data.rand_el(data.notification)
        for id in admins:
            output[id] = f'{users.find_value("user_id", user_id)["first_name"]} задал(-а) вопрос: "' + text + '"'
    elif mode == 'ad':
        admins = data.marketing_adm.copy()
        output = {}
        output[user_id] = data.rand_el(data.notification)
        for id in admins:
            output[id] = f'{users.find_value("user_id", user_id)["first_name"]} предлагает: "' + text + '"'
    return output

def find_answer(words):
    keys = dict_to_list(answers).copy()
    answer = []
    for question in keys:
        if len(question - set(words)) == 0:
            answer.append(answers[question])
    if len(answer) != 0:
        return answer
    else:
        return None

def notify_admins(user_id, text, users, mode = 'student'): # Функция уведомления администраторов о поступившем вопросе
    global requests_time
    if mode == 'student':
        admins = data.student_adm.copy()
    elif mode == 'ad':
        admins = data.marketing_adm.copy()

    day_time = int(time.time() / 100)
    if in_stream(user_id) == False:
        requests_time[user_id] = day_time
        return form_request(user_id, text, users, mode)
    else:
        t_1 = requests_time[user_id]
        t_2 = day_time
        requests_time[user_id] = day_time
        if (t_2 - t_1) >= 20 or (t_2 - t_1) < 0:
            return form_request(user_id, text, users, mode)
