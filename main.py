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
from speech_controller import greeting_massage
import data
import json

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

def update_keyboard(user_id, keyboard, message = 'Updated'): # Обновляет клавиатуру
    try:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator(), 'keyboard': find_keyboard(keyboard)})
    except:
        print("Ошибка при попытке обновления клавиатуры! (см. update_keyboard)")

def send(user_id, message = None, file = None): # Отправляет сообщение или файл пользователю
    attachments = []
    if message != None:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': id_generator()})
    elif file != None:
        print(type(file))
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
    if users.find_value('user_id', user_id)['keyboard_mode'] == False or string.find('0') == -1:
        send(user_id, string)
    else:
        try:
            generate_keyboard(user_id, string)
        except:
            print('Не удалось создать клавиатуру!')

def write(user_id, output): # "Распределяет" вывод
    print('Ответ:', type(output))
    if isinstance(output, str): # Выполняет действия, предназначенные для строке (list)
        if users.find_value('user_id', user_id)['keyboard_mode'] and output.find('0') != -1:
            try:
                generate_keyboard(user_id, output) # Генерирует сообщение-клавиатуру
            except:
                print('Ошибка при генерации клавиатуры (функция write)')
        else:
            send(user_id, output)
    elif isinstance(output, list): # Выполняет действия с массивом (list)
        try:
            for element in output: # Отправляет все сообщения или файлы (если их несколько) пользователю
                if isinstance(element, str):
                    proc_str(user_id, element)
                else:
                    send(user_id, file = element)
        except:
            print('Ошибка при обработке массива (функция write)')
    elif isinstance(output, dict): # Выполняет действия, если вывод является словарем (dict)
        ids = []
        ids = controller.dict_to_list(output).copy()
        for element in ids:
            write(element, output[element])
    else:
        send(user_id, output)
        print('Ошибка при выводе класса (функция write)')

def switch_mode(user_id, mode = 'assistant_mode'): # Переключает режим работы
    users.find_value('user_id', user_id)[mode] = not users.find_value('user_id', user_id)[mode]
    users.saving()
    if users.find_value('user_id', user_id)[mode] == True:
        if mode == 'assistant_mode':
            write(user_id, ['Включен режим для абитуриента!', controller.main(user_id)])
        elif mode == 'keyboard_mode':
            write(user_id, 'Клавиатура подключена!')
    else:
        if mode == 'assistant_mode':
            controller.delete_stream(user_id)
            write(user_id, 'Режим для абитуриента выключен!')
        elif mode == 'keyboard_mode':
            write(user_id, 'Клавиатура отключена!')

output = [] # Переменная для вывода
users = Storage("users") # Переменная для долгосрочного хранения данных
# Основная программа
vk = vk_api.VkApi(token=data.token) #
longpoll = VkLongPoll(vk)           #     Авторизация в сообществе
upload = VkUpload(vk)               #
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    now = datetime.datetime.now() # Определение текущего времени
                    data.admins = find_admins()
                    user_id = event.user_id
                    if users.find_value('user_id', user_id) == False: # Получает инфомацию о пользователе
                        users.add({
                        'user_id':user_id,
                        'first_name':vk.method('users.get',{'user_id':user_id})[0]['first_name'],
                        'last_name':vk.method('users.get',{'user_id':user_id})[0]['last_name'],
                        'assistant_mode':False,
                        'keyboard_mode':True})
                        write(user_id, random_greeting(users.find_value('user_id', user_id)['first_name'])
                        + greeting_massage)
                        break

                    request = event.text # Принимает сообщение от пользователя в виде текста
                    try:
                        input = rewriter.rewriter(request) # Разделяет строку на слова
                        # Вывод в консоль
                        print('\n[', now.strftime("%d-%m %H:%M:%S"), ']\n\033[4m\033[32muser_id:\033[0m\033[33m', user_id, '\n\033[4m\033[32mrequest:\033[0m\033[33m', input, '\033[0m\033[37m')
                        if '/assistant' in input:
                            switch_mode(user_id)
                            break
                        elif '/keyboard' in input:
                            switch_mode(user_id, 'keyboard_mode')

                        if '/menu' in input:
                            update_keyboard(user_id, "main")
                        elif '/hide' in input:
                            update_keyboard(user_id, "remote")
                        if users.find_value('user_id', user_id)['assistant_mode'] == True: # Смотрит в каком режиме нужно ответить пользователю
                            output = controller.main(user_id, input) # Помогает пользователю, выводя для него каталог или определенные файлы
                        elif not (user_id in data.admins):
                            output = notify_admins(user_id, event.text, users, find_admins())
                        else:
                            output = 'Администратору не могут приходить вопросы от администратора!'

                        write(user_id, output)
                    except:
                        pass
    except:
        print('Longpoll: Превышено время ожидания. Повторная попытка')
        time.sleep(3)
