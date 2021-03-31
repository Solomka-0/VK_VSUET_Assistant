import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import datetime
#Импорт дополнительных модулей
import rewriter
import controller
from speech_controller import notify_admins
from speech_controller import random_greeting
from speech_controller import greeting_message, introductory_student, introductory_ad, introductory_entrant, introductory_timetable
from speech_controller import find_answer
import data
import json
from get import get as update_timetables
from timetable_controller import timetable_controller as t_controller
from timetable_controller import initialization
from ipgetter2 import ipgetter1 as ipgetter

class Storage(object): # Класс отвечает за сохранение листа в текстовом файле, его чтение и редактирование
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename + '.json') as file:
                self.list = json.load(file).copy()
                file.close()
        except:
            self.list = []
    def saving(self): # Перезаписывает(сохраняет) лист
        with open(self.filename + '.json', 'w') as file:
            json.dump(self.list, file)
            file.close()
    def find_value(self, key, value): # Находит элемент словаря в листе
        for element in self.list:
            if element[key] == value:
                return element
        return False
    def add(self, element): # Добавляет элемент в лист и перезаписывает(сохраняет) его
        self.list.append(element)
        self.saving()
    def withdraw(self, key, value): # Удаляет элемент из листа и перезаписывает(сохраняет) его
        self.list.remove(self.find_value(key, value))
        self.saving()

# Генерирует id, полагаясь на настоящее время (числа не повторяются и идут по возрастанию)
def id_generator():
    id = time.time() * 100000000
    id = int(id)
    return id

def get_group_id(): # Возвращает id сообщества
    return vk.method('groups.getById',{})[0]['id']

def get_ip():
    return ipgetter.myip()

def find_admins(): # Находит администраторов, возвращает список из id пользователей
    array = []
    array = vk.method('groups.getMembers',{'group_id':get_group_id(),'filter': 'managers'})['items'].copy()
    out = []
    for i in range(0, len(array)):
        out.append(array[i]['id'])
    return out

def get_next_line(text): # Находит первую линию в тексте, отделенную \n
    return text[0:text.find('\n')]

def generate_keyboard(user_id, text): # Переводит текст с цифрами (номерами) в кнопки
    keyboard = {"buttons":[], "inline":True} # Скелет для клавиатуры
    message = ''
    while text.find('\n') != -1 and len(text) > 3: # Пока длинна текста больше 3 и найден \n
        if message == '': # Добавляет текст сообщению во избежание ошибки
            message = '&#13;'

        string = get_next_line(text) # Получает следующую линию
        if len(keyboard["buttons"]) == 5: # Так как VK API может отправить только 5 инлайн-кнопок в сообщении (счет по высоте),
                                          # то условие отчитывает кажую партию кнопок и отправляет их
            keyboard = json.dumps(keyboard, separators=(',', ':'))
            vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator(), 'keyboard': keyboard})
            keyboard = {"buttons":[], "inline":True} # Сбрасывает клавиатуру

        if text[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: # Смотрит, есть ли в начале строки цифра
            if len(string) > 40: # Обрезает сообщение если оно слишком велико (максимум 40 символов)
                string = string[0:38] + '..'
            keyboard["buttons"].append([{"action":{ "type":"text", "label":string},"color":"secondary"}]) # Формирует клавиатуру
        else:
            message = message + string # Если в строке есть титул, то он высылается пользователю вместе с первым сообщением
        text = text[text.find('\n')+1:len(text)] # Переходит на следующую строку (линию)
    keyboard = json.dumps(keyboard, separators=(',', ':'))
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator(), 'keyboard': keyboard})

def find_keyboard(name): # Ищет и возвращает клавиатуру из файла "keyboards.json"
    try:
        with open("keyboards.json", encoding = "UTF-8") as file: # Открывает файл для чтения
            output = json.load(file).copy()
            output = output[name]
            file.close()
        output = json.dumps(output, separators=(',', ':'))
        return output
    except:
        print('Ошибка при чтении файла keyboards.json (см. find_keyboard)')
        return json.dumps({"buttons":[],"one_time":True}, separators=(',', ':'))

def update_keyboard(user_id, keyboard, message = 'Клавиатура обновлена'): # Обновляет клавиатуру на заданную
    try:
        print('\033[0m\033[37m ↑ Answer ↑\n\033[4m\033[36muser_id:\033[0m\033[33m', user_id, '\n\033[4m\033[36mmessage:\033[0m\033[33m', message, '\033[0m\033[37m')
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator(), 'keyboard': find_keyboard(keyboard)})
    except:
        print("Ошибка при попытке обновления клавиатуры! (см. update_keyboard)")

def send(user_id, message = None, file = None): # Отправляет сообщение или файл пользователю
    attachments = []
    print('\033[0m\033[37m ↑ Answer ↑\n\033[4m\033[36muser_id:\033[0m\033[33m', user_id, '\n\033[4m\033[36mmessage:\033[0m\033[33m', message, '\n\033[4m\033[36mtype_of_file:\033[0m\033[33m', type(file), '\033[0m\033[37m')
    if message != None:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator()})
    elif file != None:
        if isinstance(file, data.Media): # Кидает картинку на сервер, а затем пересылает ее пользователю вместе с текстом сообщения
            file_name = data.path + file.path
            upload_image = upload.photo_messages(photos=file_name)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            vk.method('messages.send', {'user_id': user_id, 'message': file.text, 'random_id': id_generator(), 'attachment': ','.join(attachments)})
        elif isinstance(file, data.Pdf): # Загружает документ на сервер, а потом пересылает его вмсесте с текстовым сообщением
            file_name = data.path + file.path
            upload_file = upload.document_message(doc=file_name, peer_id=user_id, title=file.file_name.replace(':', '').replace(' ', '_').replace('.', '').replace('!', '') + '.pdf')['doc']
            attachments.append('doc{}_{}'.format(upload_file['owner_id'], upload_file['id']))
            vk.method('messages.send', {'user_id': user_id, 'message': file.text, 'random_id': id_generator(), 'attachment': ','.join(attachments)})
        elif isinstance(file, data.Jpg): # Загружает картинку на сервер, а потом пересылает ее сообщением
            file_name = data.path + file.path
            upload_image = upload.photo_messages(photos=file_name)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            vk.method('messages.send', {'user_id': user_id, 'random_id': id_generator(), 'attachment': ','.join(attachments)})
        elif isinstance(file, data.Folder) and file.text != None:
            vk.method('messages.send', {'user_id': user_id, 'message': file.text, 'random_id': id_generator()})

def proc_str(user_id, string): # Смотрит на то как вывести строку (в виде кнопок, или же без них)
    if users.find_value('user_id', user_id)['keyboard_mode'] and users.find_value('user_id', user_id)['mode'] == 'entrant':
        try:
            generate_keyboard(user_id, string)
        except:
            print('Возможно произошла ошибка (proc_str)')
    else:
        send(user_id, string)

def write(user_id, output): # "Распределяет" вывод
    if isinstance(output, str): # Выполняет действия, предназначенные для строки
        proc_str(user_id, output)
    elif isinstance(output, list): # Выполняет действия с массивом (list)
        try:
            for element in output: # Отправляет все сообщения или файлы (если их несколько) пользователю
                if isinstance(element, str):
                    proc_str(user_id, element)
                elif isinstance(element, list):
                    write(user_id, element)
                elif isinstance(output, dict):
                    write(user_id, element)
                else:
                    send(user_id, file=element)
        except:
            print('Ошибка при обработке массива (функция write)')
    elif isinstance(output, dict): # Выполняет действия, если вывод является словарем (dict)
        ids = []
        ids = controller.dict_to_list(output).copy()
        for element in ids:
            write(element, output[element])
    elif isinstance(output, None):
        print("*Молчит*")
    else:
        send(user_id, output)
        print('Ошибка при выводе класса (функция write)')

def switch_mode(user_id, mode = None): # Переключает режим работы
    users.find_value('user_id', user_id)['mode'] = mode
    if mode == 'entrant':
        write(user_id, ['Включен режим для абитуриента!', controller.main(user_id)])
    elif mode == 'student':
        write(user_id, 'Ну, где там твой вопрос? 🧐')
    elif mode == 'ad':
        write(user_id, 'Мы ждем :)')
    elif mode == 'timetable':
        write(user_id, 'Жми на кнопку! c:')
    elif mode == 'tt_settings':
        write(user_id, 'Ты от куда?')
    users.saving()

output = [] # Переменная для вывода
users = Storage("users") # Переменная для долгосрочного хранения данных
admins = Storage("admins")
current_users = {}

def get_timetable(user_id, time):
    try:
        send(user_id, str(t_controller(users.find_value('user_id', user_id)['group'],
                users.find_value('user_id', user_id)['subgroup'],
                time,
                users.find_value('user_id', user_id)['faculty'])
            ))
    except:
        if users.find_value('user_id', user_id)['group'] == None or users.find_value('user_id', user_id)['faculty'] == None:
            update_keyboard(user_id, 'timetable', 'Недостаточно данных для получения рассписания. Ты можешь добавить информацию о себе, воспользовавшись особым разделом ("Смена персональной информации")')
        else:
            send(user_id, f'Не удалось получить расписание по заданным фильтрам:\nГруппа {users.find_value("user_id", user_id)["group"]}\nВременной промежуток {time}\nФакультет "{users.find_value("user_id", user_id)["faculty"]}"')

def command_block(user_id, words): # Обрабатывает команды
    global current_users

    if admins.find_value('user_id', user_id):
        if '/update_timetables' in words or ('обновить' in words and 'расписание' in words):
            if update_timetables():
                initialization()
                send(user_id, 'Файлы успешно обновлены!')
            else:
                initialization()
                send(user_id, 'Не удалось обновить файлы :с')
        if '/get_ip' in words or ('ip' in words):
            send(user_id, get_ip())

    if '/entrant_mode' in words or 'абитуриенту' in words: # Переключает режим на "для абитуриента"
        update_keyboard(user_id, 'entrant', introductory_entrant)
        switch_mode(user_id, mode = 'entrant')
        return True
    elif '/student_mode' in words or ('общие' in words and 'вопросы' in words): # Переключает режим на "для студента"
        update_keyboard(user_id, 'switch_mode', introductory_student)
        switch_mode(user_id, mode = 'student')
        return True
    elif '/ad_mode' in words or ('по' in words and 'маркетинга' in words): # Переключает режим на прием заявок от маркетологов
        update_keyboard(user_id, 'switch_mode', introductory_ad)
        switch_mode(user_id, mode = 'ad')
        return True
    elif '/timetable' in words or ('мое' in words and 'расписание' in words): # Переключает режим для выбора расписания
        update_keyboard(user_id, 'timetable', introductory_timetable)
        switch_mode(user_id, mode = 'timetable')
        return True
    elif '/keyboard' in words or ('отображение' in words and 'каталогов' in words): # Изменяет режим отображения клавиатуры
        users.find_value('user_id', user_id)['keyboard_mode'] = not users.find_value('user_id', user_id)['keyboard_mode']
        users.saving()
        write(user_id, 'Режим работы с клавиатурой изменен')
        return True
    elif '/tt_settings' in words or ('смена' in words and 'информации' in words): # Меняет режим для получения информации о пользователе
        update_keyboard(user_id, 'settings_step_0', 'Для начала следует определится с факультетом. Выбери один из вариантов на клавиатуре')
        switch_mode(user_id, 'tt_settings')
        current_users[user_id] = 'step_0'
        return True

    if users.find_value('user_id', user_id)['mode'] == 'timetable': # Возвращает расписание пользователю, исходя из указанного времени
        if 'понедельник' in words:
            get_timetable(user_id, 'понедельник')
        elif 'вторник' in words:
            get_timetable(user_id, 'вторник')
        elif 'среда' in words:
            get_timetable(user_id, 'среда')
        elif 'четверг' in words:
            get_timetable(user_id, 'четверг')
        elif 'пятница' in words:
            get_timetable(user_id, 'пятница')
        elif 'суббота' in words:
            get_timetable(user_id, 'суббота')
        elif 'расписание' in words and 'следующей' in words and 'недели' in words:
            get_timetable(user_id, 'след_неделя')
        elif 'расписание' in words and 'недели' in words:
            get_timetable(user_id, 'неделя')


    if '/modes' in words or ('вернуться' in words and 'к' in words and 'меню' in words) or ('Изменить' in words and 'режим' in words and 'работы' in words): # Возвращает клавиатуру для смены режима
        if admins.find_value('user_id', user_id):
            update_keyboard(user_id, 'adm_modes')
        else:
            update_keyboard(user_id, 'modes')
        return True
    return False


def display_admins(): # Выводит список администраторов с нужными параметрами
    print('\nАдминистрация:\n')
    for admin in admins.list:
        print(f'{admin["first_name"]} | id: "{admin["user_id"]}", modes: {admin["modes"]}\n')

def announce_admins(): # Обновляет список администрации
    if admins.list != find_admins():
        for admin_id in find_admins():
            if admins.find_value('user_id', admin_id) == False:
                admins.add({
                'user_id':admin_id,
                'first_name':vk.method('users.get',{'user_id':admin_id})[0]['first_name'],
                'last_name':vk.method('users.get',{'user_id':admin_id})[0]['last_name'],
                'modes':[]})
    for admin in admins.list: # Заносит администраторов во вспомогательные списки
        if 'ad' in admin["modes"]:
            data.marketing_adm.append(admin['user_id'])
        if 'student' in admin["modes"]:
            data.student_adm.append(admin['user_id'])

def change_settings_adm(): # Помогает в работе со списком администраторов
    if input('Изменить настройки администрации? (y/n): ') == 'y':
        print('Для выхода наберите "exit"')
        display_admins()
        print('Для справки:\nswitch_mode <id> <mode> - переключить режим администратору,\nadd_mode <id> <mode> - добавить режим,\nclear <id> - очистить режимы\n')
        print('Режимы работы: "student", "ad"\n')
        while True: # Слушает команды от пользователя
            command = input('Команда: ')
            if command == 'exit':
                break
            if 'switch_mode ' in command: # Меняет режим (режимы) на заданный
                command = command.replace('switch_mode ', '')
                try:
                    id = int(command[0:command.find(' ')])
                    mode = command[command.find(' ')+1:len(command)]
                except:
                    print('Ошибка распознания команды')
                    break
                if mode == 'student':
                    admins.find_value('user_id', id)['modes'].clear()
                    admins.find_value('user_id', id)['modes'].append('student')
                elif mode == 'ad':
                    admins.find_value('user_id', id)['modes'].clear()
                    admins.find_value('user_id', id)['modes'].append('ad')

            elif 'add_mode ' in command: # Добавляет режим в список
                command = command.replace('add_mode ', '')
                try:
                    id = int(command[0:command.find(' ')])
                    mode = command[command.find(' ')+1:len(command)]
                except:
                    print('Ошибка распознания команды\n')
                    break
                if mode == 'student':
                    new_set = set(admins.find_value('user_id', id)['modes'])
                    new_set.add('student')
                    admins.find_value('user_id', id)['modes'] = list(new_set).copy()
                elif mode == 'ad':
                    new_set = set(admins.find_value('user_id', id)['modes'])
                    new_set.add('ad')
                    admins.find_value('user_id', id)['modes'] = list(new_set).copy()

            elif 'clear ' in command: # Очищает список режимов
                command = command.replace('clear ', '')
                admins.find_value('user_id', id)['modes'].clear()
            else:
                print(f'Неизвестная команда: {command[0:len(command)]}')
                continue
            admins.saving()
            print('Изменения были сохранены!')
    print('\n-- Помощник запущен! --')

def distribution_controller(mode, input, user_id, request): # Параметры: mode - режим работы с пользователем,
                                                            # input - слова пользовательского запроса,
                                                            # user_id - id пользователя, request - текст сообщения от пользователя
    global users
    if mode == 'entrant': # Смотрит в каком режиме нужно ответить пользователю
        return controller.main(user_id, input) # Помогает пользователю, выводя для него каталог или определенные файлы
    elif mode == 'student' or mode == None:
        answer = find_answer(input) # Присваивает ответ на указаный вопрос, если он есть в каталоге
        if answer != None:
            return [answer, notify_admins(user_id, request, users, 'student')]
        else:
            return notify_admins(user_id, request, users, 'student')
    elif mode == 'ad':
        return notify_admins(user_id, request, users, 'ad')
    elif mode == 'tt_settings':
        return tt_settings(user_id, input, users)


def tt_settings(user_id, words, users): # Выбирает данные о пользователя для успешной работы другого(-их) режимов
    global current_users
    if current_users[user_id] == 'step_0': # Шаг 1 - Получение факультета пользвателя
        if 'уитс' in words:
            users.find_value('user_id', user_id)['faculty'] = 'uits'
        elif 'пма' in words:
            users.find_value('user_id', user_id)['faculty'] = 'pma'
        elif 'эхт' in words:
            users.find_value('user_id', user_id)['faculty'] = 'eht'
        elif 'технологий' in words and 'факультет' in words:
            users.find_value('user_id', user_id)['faculty'] = 'tf'
        elif 'эиу' in words or ('экономики' in words and 'управления' in words):
            users.find_value('user_id', user_id)['faculty'] = 'eui'
        else:
            return 'Увы, такого факультета нет в моем списке. Пожалуйста, используй кнопки'
        users.saving()
        update_keyboard(user_id, 'switch_mode', 'Отлично! Теперь укажи свою группу, например: "У-206"')
        current_users[user_id] = 'step_1'
        return None
    elif current_users[user_id] == 'step_1': # Шаг 2 - Получение группы студента
        users.find_value('user_id', user_id)['group'] = words[0]
        users.saving()
        current_users[user_id] = 'step_2'
        return 'Параметр был сохранен. Осталось только узнать твою подгруппу. Укажи "1"/"2" или, если у вас нет разделения, выбери любую из цифр'
    elif current_users[user_id] == 'step_2':  # Шаг 3 - Получение подгруппы и смена режима
        if int(words[0]) == 1 or int(words[0]) == 2:
            users.find_value('user_id', user_id)['subgroup'] = int(words[0])
            users.saving()
            current_users.pop(user_id)
            update_keyboard(user_id, 'timetable', 'Все, настройки завершены. Пользуйся на здоровье 😉')
            switch_mode(user_id, 'timetable')
            return None
        else:
            return 'Такой подгруппы не может быть! Ты снова что-то напутал, человечишка'


# Основная программа
vk = vk_api.VkApi(token=data.token) #
longpoll = VkLongPoll(vk)           #     Авторизация в сообществе
upload = VkUpload(vk)               #
announce_admins()
change_settings_adm()
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    now = datetime.datetime.now() # Определение текущего времени
                    user_id = event.user_id
                    request = rewriter.replace_smiles(event.text) # Принимает сообщение от пользователя в виде текста
                    try:
                        input = rewriter.rewriter(request) # Разделяет строку на слова
                        print('\n[', now.strftime("%d-%m %H:%M:%S"), ']\n\033[4m\033[32muser_id:\033[0m\033[33m', user_id, '\n\033[4m\033[32mrequest:\033[0m\033[33m', input, '\033[0m\033[37m')
                        if ('начать' in input or 'начало' in input) and users.find_value('user_id', user_id) == False: # Получает инфомацию о пользователе
                            users.add({
                            'user_id':user_id,
                            'first_name':vk.method('users.get',{'user_id':user_id})[0]['first_name'],
                            'last_name':vk.method('users.get',{'user_id':user_id})[0]['last_name'],
                            'mode':None,
                            'keyboard_mode':True,
                            'group':None,
                            'subgroup':1,
                            'faculty':None})
                            write(user_id, random_greeting(users.find_value('user_id', user_id)['first_name'])
                            + greeting_message)
                            update_keyboard(user_id, 'modes', 'Выбирай (клавиатура)')
                            break
                        elif users.find_value('user_id', user_id) == False:
                            users.add({
                            'user_id':user_id,
                            'first_name':vk.method('users.get',{'user_id':user_id})[0]['first_name'],
                            'last_name':vk.method('users.get',{'user_id':user_id})[0]['last_name'],
                            'mode':None,
                            'keyboard_mode':True,
                            'group':None,
                            'subgroup':1,
                            'faculty':None})
                            command_block(user_id, input)
                        elif ('начать' in input or 'начало' in input) and users.find_value('user_id', user_id):
                            write(user_id, random_greeting(users.find_value('user_id', user_id)['first_name'])
                            + greeting_message)
                            update_keyboard(user_id, 'modes', 'Выбирай (клавиатура)')
                            break
                        elif command_block(user_id, input):
                            break
                        output = distribution_controller(users.find_value('user_id', user_id)['mode'], input, user_id, request)
                        write(user_id, output)
                    except:
                        pass
    except:
        print('Longpoll: Превышено время ожидания. Повторная попытка')
        time.sleep(3)
