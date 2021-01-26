import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import random
import time
#Импорт дополнительных модулей
import rewriter
import controller
import data

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
# Основная программа
vk = vk_api.VkApi(token=data.token) #
longpoll = VkLongPoll(vk)           #     Авторизация в сообществе
upload = VkUpload(vk)               #
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text # Принимает сообщение от пользователя в виде текста
                    try:
                        input = rewriter.rewriter(request) # Разделяет строку на слова и находит ключевые слова
                                                           # Тип: массив; Первый элемент - массив со словами, Второй - массив с ключами
                        out = controller.main(event.user_id, input[0]) # Принимает ответ для клиента
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
