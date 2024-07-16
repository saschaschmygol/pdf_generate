from reportlab.platypus import TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
def cm_to_points(cm: float):
    return cm * 28.3464567  # 1 cm = 28.3464567 points

STYLE = TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Цвет текста для заголовка
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Выравнивание текста по центру
    ('FONTNAME', (0, 0), (-1, 0), 'Times'),  # Шрифт для заголовка
    ('FONTSIZE', (0, 0), (-1, 0), 14),  # Размер шрифта для заголовка
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Отступ снизу для заголовка
    ('BACKGROUND', (0, 0), (-1, -1), colors.white),  # Заливка фона для данных
    ('FONTNAME', (0, 1), (-1, -1), 'Times'),  # Шрифт для данных
    ('FONTSIZE', (0, 1), (-1, -1), 12),  # Размер шрифта для данных
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Сетка таблицы
    ('SPAN', (2, 0), (4, 0)),  # Объединение ячеек Header 2 и Header 3
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
])

CUSTOM_PARAGRAPH_STYLE = ParagraphStyle(
    'CustomStyle',
    fontName='Times',
    fontSize=12,
    leading=14,  # Межстрочный интервал
    textColor=colors.black,
    alignment=4,  # Центрирование текста (0 - влево, 1 - центр, 2 - вправо, 4 - в ширину)
    spaceAfter=0,  # Отступ после абзаца
    firstLineIndent=20,  # Отступ первой строки (красная строка)
    leftIndent=cm_to_points(0),  # Отступ слева
    rightIndent=cm_to_points(0)  # Отступ справа
)