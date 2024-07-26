from pdf_settings_style import *
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch
from file_db import data_person

pdfmetrics.registerFont(TTFont('Times', 'timesnewromanpsmt.ttf'))

def format_date_table(s1, s2, date,TAB_PARAGRAPH_STYLE, KALEND_PO_EPIDEM_PAKAZ, NATION_KALENDAR, REGION_KALENDAR):
    ''' Создание списка данных для заполнения таблицы #->список [['', ''], ['', ''], [''..]] '''

    lst_info = [['1' for i in range(5)] for i in range(len(date['date']))]
    for i, n in enumerate(date['date']):
        lst_info[i][0] = n[0]
        lst_info[i][1] = n[1]
        lst_info[i][2] = REGION_KALENDAR[n[1]]
        lst_info[i][3] = NATION_KALENDAR[n[1]]
        lst_info[i][4] = KALEND_PO_EPIDEM_PAKAZ[n[1]]

    stroka_table_words = [[] for i in lst_info] # делаем стиль Paragraph
    for i, x in enumerate(lst_info):
        for n in x:
            a = Paragraph(n, TAB_PARAGRAPH_STYLE)
            stroka_table_words[i].append(a)

    lst_date = [s1, s2]                                # первые 2 строки таблицы

    for i in stroka_table_words:
        lst_date.append(i)

    return lst_date

def generate_pdf(date):
    doc = SimpleDocTemplate("example_table.pdf", pagesize=A4, topMargin=cm_to_points(1), leftMargin=cm_to_points(1))

    col_widths = [cm_to_points(1.9), cm_to_points(4), cm_to_points(4.5), cm_to_points(4.7),
                  cm_to_points(4.5)]  # ширина колонок

    list_words = [['Рекоммендуемый срок', 'Инфекционное заболевание', 'Основание', '', ''],
                  ['', '',
                   'Региональный календарь профилактических прививок по Свердловской области (утвержден Приказом МЗ СО от 11 августа 2022г. N 1881 - п)',
                   'Национальный календарь профилактических прививок (утвержден Приказом МЗ РФ от 6 декабря 2021 г. N 1122-н)',
                   'Календарь профилактических прививок по эпидемическим показаниям (утвержден Приказом МЗ РФ от 6 декабря 2021 г. N 1122-н)']]

    text_top = ['Уведомление о необходимости прохождения иммунизации', f'Уважаемый(-ая) {date['name']} !', f'Уведомляем вас, что в 2024 году ВЫ подлежите иммунизации против : {
    generate_str_vac(date)} ',
                'Предлагаем вам пройти иммунизацию согласно графику, прописанному в уведомлении, в срок не позднее 1 месяца с начала периода, предложенного в графике'
                ' по профилактике конкретного заболевания, и предоставить данные старшей медсестре отделения, для дальнейшего планирования последующих этапов иммунизации',
                'В случае отказа от прохождения иммунизации Работодатель оставляет за собой право отстранять своего сотрудника от работы в рамках действующего законодательства'
                ' без сохранения заработной платы']

    text_bot = ['Дата <<_____>>___________2024г.', 'Подпись направляемого на иммунизацию (с расшифровкой)_____________/___________',
                'Подпись сотрудника эпидемиологического отдела ___________/____________']

    stroka_table_words = [[] for i in list_words]
    for i, x in enumerate(list_words): # первые 2 строки таблицы
        for n in x:
            a = Paragraph(n, TAB_PARAGRAPH_STYLE)
            stroka_table_words[i].append(a)

    stroka_top = [Paragraph(i, CUSTOM_PARAGRAPH_STYLE) for i in text_top]
    stroka_bot = [Paragraph(i, CUSTOM_PARAGRAPH_STYLE) for i in text_bot] # перед и после таблицы

    lst_date = format_date_table(stroka_table_words[0], stroka_table_words[1], date, TAB_PARAGRAPH_STYLE, KALEND_PO_EPIDEM_PAKAZ, NATION_KALENDAR, REGION_KALENDAR)

    table = Table(lst_date, colWidths=col_widths) #создание таблицы и применение стиля
    table.setStyle(STYLE)

    # Добавляем отступы с помощью Spacer
    content_table = [Spacer(1, cm_to_points(0.5)), table, Spacer(1, cm_to_points(0.5))]
    content: list = stroka_top + content_table + stroka_bot

    # Добавляем таблицу в документ
    doc.build(content)

if __name__=='__main__':
    date = data_person(1)
    print(date)
    generate_pdf(date)

