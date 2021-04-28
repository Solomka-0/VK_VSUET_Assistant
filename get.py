from bs4 import BeautifulSoup
import requests

file_names = {'uits':'timetables/uits.xlsx', 'pma':'timetables/pma.xlsx', 'eht':'timetables/eht.xlsx', 'tf':'timetables/tf.xlsx', 'eiu':'timetables/eiu.xlsx'}

def get():
    url_name = 'https://vsuet.ru'
    url_path = '/student/schedule'
    try:
        page = requests.post(url_name + url_path)
        soup = BeautifulSoup(page.text, 'html.parser')
        uls = soup.find_all('ul')

        references = []
        for ul in uls:
            if ul.a['href'].find('.xlsx') != -1:
                references.append(ul.a['href'])

        for i in range(0, len(references)):
            references[i] = url_name + references[i]

        for file_name in file_names.keys():
            file = open(file_names[file_name], 'wb')
            for reference in references:
                if file_name in reference:
                    print(f'Загружен {file_names[file_name]}')
                    ufr = requests.get(reference)
                    file.write(ufr.content)
                    file.close()
                    break
        return True
    except:
        for file_name in file_names.keys():
            file = open(file_names[file_name], 'a')
            print(f'{file_names[file_name]} не был загружен')
            file.close()
        return False

if input("Загрузить расписание? (y/n): ") == 'y':
    get()
