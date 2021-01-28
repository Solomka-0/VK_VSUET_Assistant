import datetime
import random
import data
import rewriter
from data import MAIN_ARCHIVE as archive

stream = {} # Список каталогов для пользователей. Ключ - user_id, значение - каталог доступный пользователю

def rand_el(array): # Возвращает рандомный элемент из массива
    return array[random.randint(0,len(array)-1)]

def dict_to_list(dictionary): # Переводит словарь в массив с ключами
    try:
        return list(dictionary.keys())
    except:
        return list(dictionary)

def list_out(user_id): # Получает массив с переменными типа .pdf, .folder (и др.) и выводит названия файлов
    global stream
    array = []
    array = dict_to_list(stream[user_id]).copy()
    list = ''
    if archive == stream[user_id]:
        list += f'{rand_el(data.first_decoration)}\n'
    number = 0
    for element in array:
        list += f'{rewriter.num_in_sm(number)} {element.name}\n'
        number += 1
    if archive != stream[user_id]:
        list += f'{rewriter.num_in_sm(number)} Вернуться к началу\n'
    return list

def add_to_stream(user_id): # Добавляет пользователя в список
    global stream
    stream[user_id] = archive.copy()

def delete_stream(user_id): # Пересоздает ветку(каталог) пользователя в списке
    stream.pop(user_id)

def re_creation_stream(user_id): # Пересоздает ветку(каталог) пользователя в списке
    stream[user_id] = archive.copy()

def update_stream(user_id, number): # Осуществляет переход пользователя по каталогу и возвращает значение, зависящее от типа файла
    global stream
    array = []
    array = dict_to_list(stream[user_id]).copy()
    try:
        if number == len(array) and archive != stream[user_id]: # Возвращает пользователя в начало при использовании нужной кнопки
            re_creation_stream(user_id)
            return None
        elif number > -1 and number < len(array): # Выбирает следующий файл/папку, если пользователь указал "правильный" номер
            stream[user_id] = stream[user_id][array[number]]
        else: # Если сообщение не соответствует требованию, то программа повторяет вопрос
            return -1
    except:
        pass
    if isinstance(array[number], data.Media) or isinstance(array[number], data.Pdf) or isinstance(array[number], data.Jpg) or (isinstance(array[number], data.Folder) and array[number].text != None): # Если дальше оказался файл, а не папка, то возвращает исполняемый файл
        return array[number]
    return None

def in_stream(user_id): # Проверяет есть ли id пользователья в stream. Возвращает bool
    global stream
    array = []
    array = dict_to_list(stream).copy()
    for element in array:
        if element == user_id:
            return True
    return False

def main(user_id, words = ['-1']): # Получает id клиента и текст сообщения в виде массива со словами
    global stream
    try:
        if in_stream(user_id) == False: # Если пользователя нет в списке 'актива', то он туда добавляется и выводится каталог,
                                        # если же есть, то, в зависимости от сообщения, переходит дальше по каталогу
            add_to_stream(user_id)
            return list_out(user_id)
        else:
            try:
                file = update_stream(user_id, int(words[0])) # Переходит дальше по каталогу, в зависимости от выбора пользователя
            except:
                return [rand_el(data.misund), list_out(user_id)] # Выводит рандомное сообщение и каталог
            if (bool(stream[user_id]) == False) or ((file != None) and isinstance(file, data.Folder) == False): # Переводит пользователя в начало каталога, если он попал в конец каталога
                re_creation_stream(user_id)
            if file != -1 and file != None:
                return [file, list_out(user_id)] # Выводит файл
            elif file == -1:
                return [rand_el(data.misund), list_out(user_id)] # Выводит рандомное сообщение и каталог
            return list_out(user_id)
    except:
        return 'Что-то пошло не так..'
