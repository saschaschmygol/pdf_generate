import sqlite3
import datetime
from pdf_settings_style import MONTH, MONTHS

def check_year(year):
    n_year = year.split(' ')
    current_date = datetime.datetime.now()
    cur_year = current_date.year

    if (int(n_year[1]) - int(cur_year)) >= 1:
        return False
    else:
        return True

def time_vac(date1, date2):
    vac_type, vac_subtype = date1[0], date1[1]
    n_weeks = 0

    if vac_type == "Грипп":
        n_weeks = date2[vac_type][4]

    elif vac_type == "Гепатит B":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][2]
        elif vac_subtype == 'V3':
            n_weeks = date2[vac_type][4]
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]

    elif vac_type == "Гепатит А":
            n_weeks = date2[vac_type][1]  # 26-52 недели (6-12 месяцев) после V1

    elif vac_type == "Дифтерия, столбняк":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-6 недель (30-45 дней) после V1
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 520 недель (10 лет)
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)

    elif vac_type == "Клещевой энцефалит":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-26 недель (1-6 месяцев) после V1
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 52 недели (1 год) после V1
        elif vac_subtype == 'RV1':
            n_weeks = date2[vac_type][4]  # 156 недель (3 года)
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 156 недель (3 года)

    elif vac_type == "Краснуха":
        n_weeks = date2[vac_type][4]  # 4 недели (1 месяц) после V

    elif vac_type == "Дизентерия Зонне":
        n_weeks = date2[vac_type][4]  # ежегодно

    elif vac_type == "НКВИ":
        n_weeks = date2[vac_type][4]  # ежегодно

    elif vac_type == "Корь":
         n_weeks = date2[vac_type][4]  # 26 недель (6 месяцев) после V

    elif vac_type == "Коклюш":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-6 недель (30-45 дней) после V
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 4-6 недель (30-45 дней) после V
        elif vac_subtype == 'V3':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)

    elif vac_type == "Ветряная оспа":
            n_weeks = date2[vac_type][1]  # 6 недель после V1

    elif vac_type == "Пневмококковая инфекция":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 8 недель после V1
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][4]  # 260 недель (5 лет) после V2
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 260 недель (5 лет) после V2


    return n_weeks

def sort_mounth(date):
    ''' Сортировка месяцев в date в порядке (январь -> декабрь)
     date['date'] = [['Сентябрь 2023', 'Дизентерия Зонне'], .....]'''
    if len(date['date']) > 1:
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
    else:
        pass

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
    cursor.execute(f'SELECT Сотрудник.Фамилия, Сотрудник.Имя, Сотрудник.Отчество, Вакцинация.Дата, Вакцинация.Название_Прививки, Вакцинация.Тип FROM Вакцинация, Сотрудник WHERE (Сотрудник.ID=Вакцинация.ID_Сотрудника={id})'
                   f'AND ((Вакцинация.Дата, Вакцинация.Название_Прививки) IN (SELECT MAX(Вакцинация.Дата), Вакцинация.Название_Прививки FROM Вакцинация GROUP BY Вакцинация.Название_Прививки ))')
    rows = cursor.fetchall() #Получение результатов в виде кортежа ([], [], [])
    print(rows)

    lst_vaccin = []
    for i in rows:
        lst_vaccin.append(i[4])
    print(lst_vaccin)

    cursor.execute(f"SELECT name, V1, V2, V3, RV1, RV FROM Прививка WHERE name IN ({", ".join(f"'{item}'" for item in lst_vaccin)})")
    n_rows = cursor.fetchall()
    # print(n_rows)

    conn.close()

    date2 ={}
    for i in n_rows:
        date2[i[0]] = list(i[1:6])
    # print(date2)  #{'':[0, 0, 1, 2, 3], ...}


    date = {'name': None, 'date':[[] for i in range(len(rows))]}
    date['name'] = rows[1][0] + ' ' + rows[1][1] + ' ' + rows[1][2] #формируем имя в строку

    for i, n in enumerate(rows):
        new_data = add_time(rows[i][3], time_vac([rows[i][4], rows[i][5]], date2), MONTH)
        if check_year(new_data):
            infectious_disease = rows[i][4]
            date['date'][i].append(new_data)
            date['date'][i].append(infectious_disease)
        else:
            pass
    print(date)

    date_p_sort = [i for i in date['date'] if i] # УДАЛЕНИЕ ПУСТЫХ СТРОК В DATE['date']
    print(f"sort {date_p_sort}")
    date['date'] = date_p_sort
    print(date)

    sort_mounth(date)
    print(date)

    return date

d = data_person(1)


