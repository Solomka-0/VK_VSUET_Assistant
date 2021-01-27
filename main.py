import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import random
import time
#Импорт дополнительных модулей
import rewriter
import controller
import answers
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
            print(self.list, file)
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

def write(user_id, message = None, file = None): # Отправляет сообщение или файл пользователю
    attachments = []
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

out = [] # Переменная для вывода
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
                    try:
                        if users.find_value('user_id', event.user_id) == False:
                            users.add({
                            'user_id':event.user_id,
                            'first_name':vk.method('users.get',{'user_id':event.user_id})[0]['first_name'],
                            'last_name':vk.method('users.get',{'user_id':event.user_id})[0]['last_name'],
                            'assistant_mode':True})
                    except:
                        print('Ошибка при выборе данных о пользователе')


                    request = event.text # Принимает сообщение от пользователя в виде текста
                    try:
                        input = rewriter.rewriter(request) # Разделяет строку на слова и находит ключевые слова
                                                           # Тип: массив; Первый элемент - массив со словами, Второй - массив с ключами

                        if users.find_value('user_id', event.user_id)['assistant_mode'] == True: # Смотрит в каком режиме нужно ответить пользователю
                            out = controller.main(event.user_id, input[0]) # Помогает пользователю, выводя для него каталог или определенные файлы
                        else:
                            out = controller.answer(event.user_id, input[0], input[1])

                        if isinstance(out, list):
                            for element in out: # Отправляет все сообщения или файлы (если их несколько) пользователю
                                if isinstance(element, str):
                                    write(event.user_id, element)
                                else:
                                    write(event.user_id, file = element)
                        else:
                            write(event.user_id, out)
                    except:
                        pass
    except:
        print('Longpoll: Превышено время ожидания. Повторная попытка')
        time.sleep(3)
