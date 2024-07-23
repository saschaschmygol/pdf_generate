import sqlite3
import datetime
from pdf_settings_style import MONTH, MONTHS

def sort_mounth(date):
    ''' Сортировка месяцев в date в порядке (январь -> декабрь)
     date['date'] = [['Сентябрь 2023', 'Дизентерия Зонне'], .....]'''

    i = 0
    while True:
        cur_mon = date['date'][i][0].split(' ')
        next_mon = date['date'][i + 1][0].split(' ') # ['Сентябрь', '2023']

        if MONTHS.index(cur_mon[0]) > MONTHS.index(next_mon[0]):
            date['date'][i], date['date'][i + 1] = date['date'][i + 1], date['date'][i]
            i = 0
        else:
            i += 1
        if i == len(date['date']) - 1:
            break

def add_time(current_date, weeks_to_add, MONTH): # дата в формате 21-02-2024, кол-во недель
    ''' Прибавление (weeks_to_add) недель к дате '''

    lst_data: list = current_date.split('-') # выделяем год месяц день
    year = int(lst_data[2])
    month = int(lst_data[1])
    day = int(lst_data[0])

    custom_date = datetime.datetime(year, month, day)
    new_date = (custom_date + datetime.timedelta(weeks=weeks_to_add)).strftime("%Y-%m") # '2023-09'

    str_data = new_date.split('-')
    new_date = MONTH[str_data[1]] + ' ' + str_data[0]                                   # 'март 2023'

    return new_date

def data_person(id):
    conn = sqlite3.connect('example.db')

    cursor = conn.cursor() #Создание курсора

    # Выполнение запроса
    cursor.execute(f'SELECT Сотрудник.Фамилия, Сотрудник.Имя, Сотрудник.Отчество, Вакцинация.Дата, Вакцинация.Название_Прививки, Вакцинация.Тип FROM Вакцинация, Сотрудник WHERE Сотрудник.ID=Вакцинация.ID_Сотрудника={id}')

    rows = cursor.fetchall() #Получение результатов в виде кортежа ([], [], [])

    conn.close()

    date = {'name': None, 'date':[[] for i in range(len(rows))]}
    date['name'] = rows[1][0] + ' ' + rows[1][1] + ' ' + rows[1][2] #формируем имя в строку

    for i, n in enumerate(rows):
        new_data = add_time(rows[i][3], 30, MONTH)
        infectious_disease = rows[i][4]
        date['date'][i].append(new_data)
        date['date'][i].append(infectious_disease)

    sort_mounth(date)

    return date

# d = data_person(1)
# for n in d['date']:
#     print(n)

