import datetime
import random
import time

import data
from data import answers
greeting_message = '''Буду рад ответить на ваши вопросы, но для начала выберите интересующие вас разделы при помощи клавиатуры ⬇

🗓"Мое расписание"🗓- Данный пункт выведет актуальный список предметов на любой день!

❓"Общие вопросы" ❓ - Выбирайте эту категорию, если есть проблемы или вопросы.

📢"Абитуриенту" 📢 - Этот пункт расскажет о направлениях подготовки Воронежского государственного университета инженерных технологий. Очень полезный режим 😉

📊 "По вопросам маркетинга" 📊 - Если у Вас есть предложение связанное с публикациями, то выбирайте этот пункт для более быстрого реагирования на него.'''

introductory_student = 'Есть вопрос или проблема? Я постараюсь разобраться. Даже если не смогу вам помочь, то на вопрос обязательно ответит администратор, я его оповещу!'
introductory_entrant = '''Прекрасно! Интересуетесь поступлением в этот универ? Специально для вас есть каталог,
в котором можно найти ответы на большинство интересующих абитуриента вопросов.
Не нашли информации? Переходите в раздел с вопросами, там вам точно ответят!'''
introductory_ad = 'Если у Вас есть рекламное предложение или просьба о публикации - пишите сюда, вскоре это рассмотрит администрация.'
introductory_timetable = 'Расписание - это то что нас всех объединяет! Если вы впервые в этом разделе, то нажмите кнопку "Смена персональной информации", чтобы настроить фильтры поиска расписания. Для того, чтобы просмотреть занятия выберите кнопку с нужным вам днем недели.'

requests_time = {}

# Утренние приветствия
def morning_greeting(first_name):
    greeting_list = [f'Доброе утро, {first_name}. ⏰🤗 ', 'Утречка :3\n', f'Прекрасное утро, {first_name}. 🌞\nВам нужна помощь? ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Дневные приветствия
def afternoon_greeting(first_name, day_time):
    greeting_list = [f'Добрый день, {first_name}. ', f'Здравствуйте, {first_name}. 🙇🔨 ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Вечерние приветствия
def evening_greeting(first_name):
    greeting_list = [f'Доброго вечера, {first_name}. 🌙🌠 ', 'Привет. День подходит к концу.. ',
    f'Привет, {first_name}. Отдыхаете?\n ', 'Наслаждаюсь вечером.. Привет! ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

# Ночные приветствия
def night_greeting(first_name):
    greeting_list = [f'Вам следует лечь спать, {first_name}. ⏰ ', f'Доброй ночи, {first_name}.', 'Привет. Сон очень важен, поэтому постарайся заснуть как можно скорее! ']
    return greeting_list[random.randint(0, len(greeting_list)-1)]

def random_greeting(first_name):
    day_time = int(datetime.datetime.now().hour)
    if day_time>=5 and day_time<=10:
        return morning_greeting(first_name)
    elif day_time>=11 and day_time<=15:
        return afternoon_greeting(first_name, day_time)
    elif day_time>=16 and day_time<=22:
        return evening_greeting(first_name)
    elif day_time<=4:
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
        output[user_id] = data.rand_el(data.notification_student)
        for id in admins:
            output[id] = f'{users.find_value("user_id", user_id)["first_name"]} (id{user_id}) задал(-а) вопрос: "' + text + '"'
    elif mode == 'ad':
        admins = data.marketing_adm.copy()
        output = {}
        output[user_id] = data.rand_el(data.notification_ad)
        for id in admins:
            output[id] = f'{users.find_value("user_id", user_id)["first_name"]} (id{user_id}) предлагает: "' + text + '"'
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
