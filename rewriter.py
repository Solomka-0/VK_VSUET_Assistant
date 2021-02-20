# Алфавит (Все допустимые символы(остальные удаляются))
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ь','э','ю','я','ы',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9', ' ', "'", '/', '-', '+', '*', '^']

# Удаляет пробелы из массива со словами
numeral = {0: '0⃣', 1: '1⃣' , 2: '2⃣', 3: '3⃣' , 4: '4⃣' , 5: '5⃣' , 6: '6⃣' , 7: '7⃣' , 8: '8⃣' , 9: '9⃣'}

def num_in_sm(number):
    global numeral
    out = ''
    while (number//10 != 0):
        out = numeral[number%10] + out
        number = number//10
    out = numeral[number%10] + out
    return out

def replace_smiles(string):
    string = string.replace(' 0⃣', '0')
    string = string.replace(' 1⃣', '1')
    string = string.replace(' 2⃣', '2')
    string = string.replace(' 3⃣', '3')
    string = string.replace(' 4⃣', '4')
    string = string.replace(' 5⃣', '5')
    string = string.replace(' 6⃣', '6')
    string = string.replace(' 7⃣', '7')
    string = string.replace(' 8⃣', '8')
    string = string.replace(' 9⃣', '9')
    string = string.replace('0⃣', '0')
    string = string.replace('1⃣', '1')
    string = string.replace('2⃣', '2')
    string = string.replace('3⃣', '3')
    string = string.replace('4⃣', '4')
    string = string.replace('5⃣', '5')
    string = string.replace('6⃣', '6')
    string = string.replace('7⃣', '7')
    string = string.replace('8⃣', '8')
    string = string.replace('9⃣', '9')
    return string


def del_spaces(array_of_words):
    i = 0
    while i < len(array_of_words):
        if array_of_words[i] == '':
            array_of_words.pop(i)
            i -= 1
        i += 1
    return array_of_words
# Находит ключевые слова в массиве. Возвращает массив из номеров ключевых слов
def words_in_ids(array_of_words):
    global words_list
    array_of_words = del_spaces(array_of_words)
    id_list = []
    for i in range(0, len(array_of_words)):
        if array_of_words[i] in words_list:
            id_list.append(words_list[array_of_words[i]])
        if i < len(array_of_words) - 1:
            if (array_of_words[i] + ' ' + array_of_words[i + 1]) in words_list:
                x = array_of_words[i] + ' ' + array_of_words[i + 1]
                id_list.append(words_list[x])
        if i < len(array_of_words) - 2:
            if (array_of_words[i] + ' ' + array_of_words[i + 1] + ' ' + array_of_words[i + 2]) in words_list:
                x = array_of_words[i] + ' ' + array_of_words[i + 1] + ' ' + array_of_words[i + 2]
                id_list.append(words_list[x])
    return id_list
# Переводит строку в массив со словами
def text_in_words(string):
    string = remove_characters(string)
    k = []
    while string.find(' ') > -1:
        pos = string.find(' ')
        k.append(string[0:pos])
        string = string[pos+1:len(string)]
    k.append(string)
    return k
# Проверяет символ на его наличие в заданном алфавите
def in_array(char):
    global alphabet
    bool = False
    for i in range(0, len(alphabet)):
        if char == alphabet[i]:
            bool = True
    return bool
# Удаляет символы из строки
def remove_characters(string):
    n = len(string)
    i = 0
    while i in range(0, n):
        if in_array(string[i]) == False:
            string = string.replace(string[i], ' ')
            n -= 1
        i += 1
    return string
# Главная функция, изменяет строку
def rewriter(text):
    text = text.lower()
    words = [] #Массив со словами
    key_list = [] #Массив с заданными id для ключевых слов
    words = text_in_words(remove_characters(text)) # Перевод текста в слова с удалением запятых
    words = del_spaces(words) # Удаление пустых элементов в массиве
    if words != []:
        return words
    else:
        return ['invalidvalue']
