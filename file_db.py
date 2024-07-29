import sqlite3
import datetime
from pdf_settings_style import MONTH, MONTHS

def age_calculate(date_of_birth): # 2002-01-23
    bir_date = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
    cur_date = datetime.datetime.now()

    age = cur_date.year - bir_date.year

    if (cur_date.month, cur_date.day) < (bir_date.month, bir_date.day):
        age -= 1
    return age
def check_year(date):
    ''' date 2023-03-21 '''
    lst_data: list = date.split('-')  # выделяем год месяц день
    year = int(lst_data[0])
    month = int(lst_data[1])
    day = int(lst_data[2])
    custom_date = datetime.datetime(year, month, day)

    current_date = datetime.datetime.now()

    if (custom_date - current_date).days > 365:
        return False
    else:
        return True

def time_vac(date1, date2, age):
    vac_type, vac_subtype = date1[0], date1[1]
    next_vac_subtype = ''
    n_weeks = 0

    if vac_type == "Грипп":
        n_weeks = date2[vac_type][4]
        next_vac_subtype = 'RV'

    elif vac_type == "Гепатит B":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]
            next_vac_subtype = 'V2'
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][2]
            next_vac_subtype = 'V3'
        elif vac_subtype == 'V3':
            n_weeks = date2[vac_type][4]
            next_vac_subtype = 'RV'
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]
            next_vac_subtype = 'RV'

    elif vac_type == "Гепатит А":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 26-52 недели (6-12 месяцев) после V1
            next_vac_subtype = 'V2'
        if vac_subtype == 'V2':
            n_weeks = 0

    elif vac_type == "Дифтерия, столбняк":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-6 недель (30-45 дней) после V1
            next_vac_subtype = 'V2'
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 520 недель (10 лет)
            next_vac_subtype = 'RV1'
        elif vac_subtype == 'RV1':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
            next_vac_subtype = 'RV'
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
            next_vac_subtype = 'RV'

    elif vac_type == "Клещевой энцефалит":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-26 недель (1-6 месяцев) после V1
            next_vac_subtype = 'V2'
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 52 недели (1 год) после V1
            next_vac_subtype = 'RV1'
        elif vac_subtype == 'RV1':
            n_weeks = date2[vac_type][4]  # 156 недель (3 года)
            next_vac_subtype = 'RV'
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 156 недель (3 года)
            next_vac_subtype = 'RV'

    elif vac_type == "Краснуха":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][4]  # 4 недели (1 месяц) после V
            next_vac_subtype = 'RV'
        if vac_subtype == 'RV':
            n_weeks = 0

    elif vac_type == "Дизентерия Зонне":
        n_weeks = date2[vac_type][4]  # ежегодно
        next_vac_subtype = 'RV'

    elif vac_type == "НКВИ":
        n_weeks = date2[vac_type][4]  # ежегодно
        next_vac_subtype = 'RV'

    elif vac_type == "Корь":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][4]  # 26 недель (6 месяцев) после V
            next_vac_subtype = 'RV'
        if vac_subtype == 'RV':
            n_weeks = 0

    elif vac_type == "Коклюш":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 4-6 недель (30-45 дней) после V
            next_vac_subtype = 'V2'
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][3]  # 4-6 недель (30-45 дней) после V
            next_vac_subtype = 'V3'
        elif vac_subtype == 'V3':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
            next_vac_subtype = 'RV'
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 520 недель (10 лет)
            next_vac_subtype = 'RV'

    elif vac_type == "Ветряная оспа":
        if vac_type == 'V1':
            n_weeks = date2[vac_type][1]  # 6 недель после V1
            next_vac_subtype = 'V2'
        if vac_type == 'V2':
            n_weeks = 0

    elif vac_type == "Пневмококковая инфекция":
        if vac_subtype == 'V1':
            n_weeks = date2[vac_type][1]  # 8 недель после V1
            next_vac_subtype = 'V2'
        elif vac_subtype == 'V2':
            n_weeks = date2[vac_type][4]  # 260 недель (5 лет) после V2
            next_vac_subtype = 'V2'
        elif vac_subtype == 'RV':
            n_weeks = date2[vac_type][4]  # 260 недель (5 лет) после V2
            next_vac_subtype = 'RV'

    return n_weeks, next_vac_subtype

def sort_mounth(date):
    ''' Сортировка месяцев в date в порядке (январь -> декабрь)
     date['date'] = [['2023-06-10', 'Дизентерия Зонне'], .....]'''
    sorted_date = sorted(date, key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'))
    return sorted_date

def add_time(current_date, weeks_to_add): # дата в формате 2024-02-21, кол-во недель
    ''' Прибавление (weeks_to_add) недель к дате '''

    lst_data: list = current_date.split('-') # выделяем год месяц день
    year = int(lst_data[0])
    month = int(lst_data[1])
    day = int(lst_data[2])

    custom_date = datetime.datetime(year, month, day)
    new_date = (custom_date + datetime.timedelta(weeks=weeks_to_add)).strftime("%Y-%m-%d") # '2023-09-21'

    # str_data = new_date.split('-')
    # new_date = MONTH[str_data[1]] + ' ' + str_data[0]                                   # 'март 2023'

    return new_date

def data_person(id):
    conn = sqlite3.connect('1.db')

    #получение списка прививок по сфере работы
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Сфера_Работы WHERE name = (SELECT Должность.Сфера_Работы FROM Должность WHERE ID=(SELECT Сотрудник.Должность_Сотрудника FROM Сотрудник WHERE Сотрудник.ID={id}))")
    rows = cursor.fetchall()
    lst_vac_work = []
    for i in rows[0][2:]:
        if i != None:
            lst_vac_work.append(i)
        else:
            pass
    print(lst_vac_work)

    cursor = conn.cursor()
    cursor.execute(f"SELECT S.Имя, S.Фамилия, S.Отчество,  S.Пол, S.Дата_Рождения, W.Дата, W.Название_Прививки, W.Тип FROM Вакцинация as W, Сотрудник as S "
                   f"INNER JOIN (SELECT Вакцинация.ID_Сотрудника, MAX(Вакцинация.Дата) as Дата, Вакцинация.Название_Прививки "
                   f"FROM Вакцинация GROUP BY Вакцинация.ID_Сотрудника, Вакцинация.Название_Прививки HAVING Вакцинация.ID_Сотрудника = {id}) "
                   f"as D ON (W.Дата = D.Дата) AND (W.ID_Сотрудника = D.ID_Сотрудника= S.ID);")
    rows = cursor.fetchall() #Получение результатов в виде кортежа ([], [], [])
    lst_vac = rows
    print(lst_vac)

    date_of_birth = rows[0][4] #рассчет полных лет
    age = age_calculate(date_of_birth)
    print(age)

    date = {'name': None, 'date':[]}
    date['name'] = lst_vac[0][0] + ' ' + lst_vac[0][1] + ' ' + lst_vac[0][2] #формируем имя в строку

    if lst_vac[0][3] == 'М':
        if 'Краснуха' in lst_vac_work:
            lst_vac_work.remove('Краснуха')

    lst_vac_priv = []
    for i in lst_vac:
        lst_vac_priv.append(i[6])
    print(lst_vac_priv) #текущие прививки которые ставились раньше

    new_lst_vac = list(set(lst_vac_work) & set(lst_vac_priv)) # удаление нестандартных прививок, не отн к списку прививок в сфере раб. (за свой счет и т.д.)
    print(f"new_lst_vac {new_lst_vac}")

    if lst_vac[0][3] == 'Ж':
        if ('Краснуха' in lst_vac_work) and (('Краснуха' not in new_lst_vac) and age > 25):
            lst_vac_work.remove('Краснуха') # удаляем краснуху из общего списка если >25 и не был привит

    lst_vac_n = [i for  i in lst_vac if i[6] in new_lst_vac]
    print(lst_vac_n)                                          #оставляем только стандартные прививки для дальнейшего планирования
    new_lst_vac_work = list(set(lst_vac_work) - set(lst_vac_priv)) #список прививок для которых нужно начать схему вакцинации
    print(f"new_lst_vac_work {new_lst_vac_work}")


    cursor.execute(f"SELECT name, V1, V2, V3, RV1, RV FROM Прививка WHERE name IN ({", ".join(f"'{item}'" for item in lst_vac_work)})")
    rows = cursor.fetchall()
    conn.close()
    date2 ={}
    for i in rows:
        date2[i[0]] = list(i[1:6])
    #print(date2)  #{'Грипп':[0, 0, 1, 2, 3], ...}

    for i, n in enumerate(lst_vac_n):
        tp: str = n[7] # 'RV'
        disea = n[6]  # 'Грипп'
        dat = n[5] # 2023-02-02
        #print(tp, disea, dat)
        while True:
            lst = []
            week_add, n_tp = time_vac([disea, tp], date2, age) # 4, RV
            new_data = add_time(dat, week_add) # '2023-09-21'
            if week_add == 0:
                break
            if check_year(new_data):
                lst.append(new_data)
                lst.append(disea)
                #print(1)
                date['date'].append(lst) # ['2004-', '']
                dat = new_data
                tp = n_tp
            else:
                break

    for i, n in enumerate(new_lst_vac_work): #если прежде не велась вакцинация
        tp: str = 'V1' # 'RV'
        disea = n  # 'Грипп'
        dat = add_time(datetime.datetime.now().strftime("%Y-%m-%d"), 1)

        lst = []
        lst.append(dat)
        lst.append(disea)
        date['date'].append(lst) # первый раз
        #print(f"Nachalo {tp, disea, dat}")
        while True:
            ls = []
            week_add, n_tp = time_vac([disea, tp], date2, age) # return (4, RV)
            #print(f"------- {week_add, n_tp}")
            new_data = add_time(dat, week_add) # '2023-09-21'
            #print(f"New data{disea, new_data}")
            if week_add == 0:
                break
            if check_year(new_data):
                ls.append(new_data)
                ls.append(disea)
                #print(2)
                date['date'].append(ls) # ['2004-', '']
                dat = new_data
                tp = n_tp
            else:
                break


    # for i, n in enumerate(rows):
    #     new_data = add_time(rows[i][3], time_vac([rows[i][4], rows[i][5]], date2), MONTH)
    #     if check_year(new_data):
    #         infectious_disease = rows[i][4]
    #         date['date'][i].append(new_data)
    #         date['date'][i].append(infectious_disease)
    #     else:
    #         pass
    # print(date)
    #
    # date_p_sort = [i for i in date['date'] if i] # УДАЛЕНИЕ ПУСТЫХ СТРОК В DATE['date']
    # print(f"sort {date_p_sort}")
    # date['date'] = date_p_sort
    # print(date)
    #
    sort_date = sort_mounth(date['date'])
    date['date'] = sort_date[:]
    print(f"\n\n date{date}")

    return date

d = data_person(4)


