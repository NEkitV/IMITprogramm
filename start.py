# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfgen import canvas


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("interface.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    institutes = form.lineEdit.text()
    directionIs = form.lineEdit_2.text()
    educationalFormIs = form.lineEdit_3.text()
    fioIs = form.lineEdit_4.text()
    сhairmanGEKIs = form.lineEdit_5.text()
    memberGEK1Is = form.lineEdit_6.text()
    memberGEK2Is = form.lineEdit_7.text()
    memberGEK3Is = form.lineEdit_8.text()
    memberGEK4Is = form.lineEdit_9.text()
    memberGEK5Is = form.lineEdit_10.text()
    directorIs = form.lineEdit_13.text()
    consultantIs = form.lineEdit_14.text()

    question1Is = form.plainTextEdit.toPlainText()
    question2Is = form.plainTextEdit_2.toPlainText()
    question3Is = form.plainTextEdit_3.toPlainText()

    yesIs = form.plainTextEdit_4.toPlainText()
    noIs = form.plainTextEdit_5.toPlainText()
    abstainIs = form.plainTextEdit_6.toPlainText()


    ChGEK = form.comboBox.currentText()
    diploma = form.comboBox_5.currentText()


    # Загрузка кастомного шрифта

    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))

    pdf = canvas.Canvas("FilePDF.pdf", pagesize=letter)
    # Установка кастомного шрифта

    pdf.setFont("TimesNewRomanBold", 12)

    # заголовок файла
    pdf.setTitle('TheTitle')
    # фотка игу
    image = 'icon.jpg'
    pdf.drawInlineImage(image, 270, 720)

    # жирный текст

    pdf.drawString(240, 705, 'МИНОБРНАУКИ РОССИИ')
    pdf.drawString(125, 690, 'федеральное государственное бюджетное образовательное учреждение ')
    pdf.drawString(260, 675, 'высшего образования ')
    pdf.drawString(200, 660, '«Иркутский государственный университет»')
    pdf.drawString(260, 645, '(ФГБОУ ВО «ИГУ»)')

    pdf.line(130, 550, 500, 550)
    # обычный текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    # вставка института

    #
    #
    pdf.drawCentredString(300, 552, institutes)
    #
    #

    pdf.drawString(260, 539, 'институт (факультет)')

    pdf.line(110, 490, 520, 490)

    #
    #
    pdf.drawCentredString(300, 492, directionIs)
    #
    #
    pdf.drawString(140, 479, 'направление подготовки (специальность), направленность (профиль)')

    pdf.drawString(140, 440, 'форма обучения')
    pdf.line(225, 437, 520, 437)

    #
    #
    pdf.drawCentredString(350, 440, educationalFormIs)
    #
    #

    pdf.drawString(270, 427, '(очная, очно-заочная, заочная)')

    # жирный текст
    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))
    pdf.setFont("TimesNewRomanBold", 16)

    pdf.drawString(225, 333, 'КНИГА ПРОТОКОЛОВ')
    pdf.drawString(120, 310, 'заседаний государственной экзаменационной комиссии')
    pdf.drawString(138, 295, 'по защите выпускных квалификационных работ')
    pdf.drawString(200, 278, 'и присвоению квалификации')

    # Второй лист
    pdf.showPage()
    # жирный 16 текст
    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))
    pdf.setFont("TimesNewRomanBold", 16)

    # текст
    pdf.drawString(200, 740, 'Протокол №')
    pdf.line(295, 738, 400, 738)

    # жирный 12 текст
    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))
    pdf.setFont("TimesNewRomanBold", 12)

    pdf.drawString(150, 728, 'заседания государственной экзаменационной комиссии')
    pdf.drawString(170, 715, 'по защите выпускных квалификационных работ ')
    pdf.drawString(220, 702, 'и присвоению квалификации ')

    # обычный текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(210, 689, '«______»  _______________ 20____ г. ')
    pdf.drawString(60, 666, 'по рассмотрению выпускной квалификационной работы обучающегося ______________________')
    pdf.drawString(60, 651, '____________________________________________________________________________________')

    # обычный текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    #
    #
    pdf.drawCentredString(300, 651, fioIs)
    #
    #
    # обычный текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(260, 638, '(Фамилия Имя Отчество )')

    # обычный текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(60, 623, 'на тему: ____________________________________________________________________________')
    pdf.drawString(60, 605, '____________________________________________________________________________________')
    pdf.drawString(60, 590, '____________________________________________________________________________________')

    # жирный 12 текст
    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))
    pdf.setFont("TimesNewRomanBold", 12)
    pdf.drawString(50, 577, 'Присутствовали:')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(50, 563, 'Председатель ')
    pdf.drawString(50, 550,
                   'ГЭК                           ____________________________________________________________________')
    #
    #
    pdf.drawCentredString(120, 525, ChGEK)
    #
    #

    #
    #
    pdf.drawCentredString(330, 551, сhairmanGEKIs)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(240, 539, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(50, 525, 'Члены ГЭК:')
    pdf.drawString(50, 505, '1:')
    pdf.drawString(43, 504, '______________________________________________________________________________________')

    #
    #
    pdf.drawCentredString(300, 504, memberGEK1Is)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 493, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 480, '2:')
    pdf.drawString(43, 479, '______________________________________________________________________________________')

    #
    #
    pdf.drawCentredString(300, 479, memberGEK2Is)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 469, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 455, '3:')
    pdf.drawString(43, 454, '______________________________________________________________________________________')

    #
    #
    pdf.drawCentredString(300, 454, memberGEK3Is)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 443, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 430, '4:')
    pdf.drawString(43, 429, '______________________________________________________________________________________')

    #
    #
    pdf.drawCentredString(300, 429, memberGEK4Is)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 418, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 405, '5:')
    pdf.drawString(43, 404, '______________________________________________________________________________________')

    #
    #
    pdf.drawCentredString(300, 405, memberGEK5Is)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 393, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 380, '6:')
    pdf.drawString(43, 379, '______________________________________________________________________________________')

    pdf.drawString(50, 350, 'Руководитель ')
    pdf.drawString(50, 340, '                              ______________________________________________________________________')

    #
    #
    pdf.drawCentredString(320, 340, directorIs)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 327, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(50, 317, 'Консультант ')
    pdf.drawString(50, 313, '                              ______________________________________________________________________')

    #
    #
    pdf.drawCentredString(320, 313, consultantIs)
    #
    #

    # обычный текст 10
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)
    pdf.drawString(210, 300, 'Ф.И.О., ученая степень, ученое звание, должность')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(78, 288, 'Состав и секретарь государственной экзаменационной комиссии утвержден приказом от ')
    pdf.drawString(78, 275, '______________________ № ____________.')
    pdf.drawString(78, 260, 'В государственную экзаменационную комиссию представлены следующие материалы:')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(70, 240, '1.')

    # italic текст 12
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 12)
    pdf.drawString(84, 240, 'Выпускная квалификационная работа ')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(70, 225, '2.')

    # italic текст 12
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 12)
    pdf.drawString(84, 225, 'Отзыв руководителя')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(70, 210, '3.')

    # italic текст 12
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 12)



    pdf.drawString(84, 210, 'Рецензия (на ВКР магистра, специалиста в обязательном порядке)')



    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)
    pdf.drawString(70, 195, '4.')

    # italic текст 12
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 12)
    pdf.drawString(84, 195, 'Справка о результатах проверки на степень оригинальности ')

    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    #
    #
    pdf.drawCentredString(320, 154, question1Is)
    #
    #

    #
    #
    pdf.drawCentredString(320, 109, question2Is)
    #
    #

    #
    #
    pdf.drawCentredString(320, 79, question3Is)
    #
    #

    pdf.drawString(70, 180, '5. ______________________________________________________________________')
    pdf.drawString(70, 165, 'После сообщения о выполненной работе обучающемуся были заданы следующие вопросы: ')
    pdf.drawString(70, 154, '1. ___________________________________________________________________________________')
    pdf.drawString(70, 139, '_____________________________________________________________________________________')
    pdf.drawString(70, 124, '_____________________________________________________________________________________')
    pdf.drawString(70, 109, '2. ___________________________________________________________________________________')
    pdf.drawString(70, 94, '_____________________________________________________________________________________')
    pdf.drawString(70, 79, '3. ___________________________________________________________________________________')
    pdf.drawString(70, 68, '_____________________________________________________________________________________')
    pdf.drawString(70, 55, '_____________________________________________________________________________________')
    pdf.drawString(70, 43, 'Характеристика ответов')


    # ТРЕТЬЯ СТРАНИЦА
    pdf.showPage()
    # обычный текст 12
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    #
    #
    #
    #

    if (form.comboBox_2.currentText() == ("5-Дан полный, развернутый ответ на поставленный вопрос, показана\n"
            "совокупность осознанных знаний об объекте, проявляющаяся в свободном\n"
            "оперировании понятиями, умении выделить существенные и\n"
            "несущественные его признаки, причинно-следственные связи. Знание об\n"
            "объекте демонстрируется на фоне понимания его в системе данной науки и\n"
            "междисциплинарных связей")):
        pdf.drawString(85, 738, 'Дан полный, развернутый ответ на вопрос, показана совокупность осознанных знаний об объекте,')
        pdf.drawString(75, 720, 'умение выделять существенные признаки и причинно-следственные связи.')
    elif (form.comboBox_2.currentText() == ("4- Дан полный, развернутый ответ на поставленный вопрос, доказательно\n"
            "раскрыты основные положения темы; B ответе прослеживается четкая\n"
            "структура, логическая последовательность, отражающая сущность\n"
            "раскрываемых понятий, теорий, явлений.")):
        pdf.drawString(85, 738, 'Дан полный, развернутый ответ на поставленный вопрос, четкая структура, логическая,')
        pdf.drawString(75, 720, 'логическая последовательность и основные положения темы представлены в полном ответе.')
    elif (form.comboBox_2.currentText() == (
            "3-Дан полный, но недостаточно последовательный ответ на поставленный\n"
            "вопрос, но при этом показано умение выделить существенные и\n"
            "несущественные признаки и причинно-следственные связи. Ответ логичен\n"
            "и изложен в терминах науки. Могут быть допущены 1-2 ошибки в\n"
            "определении основных понятий\n")):
        pdf.drawString(90, 738, 'Частично последовательный ответ, некоторые ошибки в определении понятий, но в целом ')
        pdf.drawString(75, 720, 'выделяются существенные признаки и причинно-следственные связи. ')
    elif (form.comboBox_2.currentText() == (
            "2-Дан неполный ответ, представляющий собой разрозненные знания по теме\n"
            "вопроса с существенными ошибками в определениях. Присутствуют\n"
            "фрагментарность, нелогичность изложения. Студент не осознает связь\n"
            "данного понятия, теории, явления с другими объектами дисциплины\n"
            "(модуля). Отсутствуют выводы, конкретизация и доказательность\n"
            "изложения. Речь неграмотная.")):
        pdf.drawString(90, 738, 'Неполный и нелогичный ответ с ошибками в определениях, отсутствием связи с другими')
        pdf.drawString(75, 720, 'объектами дисциплины, выводами и доказательностью. Речь неграмотная.')




    if (form.comboBox_3.currentText() == ("5-Дан полный, развернутый ответ на поставленный вопрос, показана\n"
            "совокупность осознанных знаний об объекте, проявляющаяся в свободном\n"
            "оперировании понятиями, умении выделить существенные и\n"
            "несущественные его признаки, причинно-следственные связи. Знание об\n"
            "объекте демонстрируется на фоне понимания его в системе данной науки и\n"
            "междисциплинарных связей")):
        pdf.drawString(85, 693, 'Дан полный, развернутый ответ на вопрос, показана совокупность осознанных знаний об объекте,')
        pdf.drawString(75, 678, 'умение выделять существенные признаки и причинно-следственные связи.')
    elif (form.comboBox_3.currentText() == ("4- Дан полный, развернутый ответ на поставленный вопрос, доказательно\n"
            "раскрыты основные положения темы; B ответе прослеживается четкая\n"
            "структура, логическая последовательность, отражающая сущность\n"
            "раскрываемых понятий, теорий, явлений.")):
        pdf.drawString(85, 693, 'Дан полный, развернутый ответ на поставленный вопрос, четкая структура, логическая,')
        pdf.drawString(75, 678, 'логическая последовательность и основные положения темы представлены в полном ответе.')
    elif (form.comboBox_3.currentText() == (
            "3-Дан полный, но недостаточно последовательный ответ на поставленный\n"
            "вопрос, но при этом показано умение выделить существенные и\n"
            "несущественные признаки и причинно-следственные связи. Ответ логичен\n"
            "и изложен в терминах науки. Могут быть допущены 1-2 ошибки в\n"
            "определении основных понятий\n")):
        pdf.drawString(90, 693, 'Частично последовательный ответ, некоторые ошибки в определении понятий, но в целом ')
        pdf.drawString(75, 678, 'выделяются существенные признаки и причинно-следственные связи. ')
    elif (form.comboBox_3.currentText() == (
            "2-Дан неполный ответ, представляющий собой разрозненные знания по теме\n"
            "вопроса с существенными ошибками в определениях. Присутствуют\n"
            "фрагментарность, нелогичность изложения. Студент не осознает связь\n"
            "данного понятия, теории, явления с другими объектами дисциплины\n"
            "(модуля). Отсутствуют выводы, конкретизация и доказательность\n"
            "изложения. Речь неграмотная.")):
        pdf.drawString(90, 693, 'Неполный и нелогичный ответ с ошибками в определениях, отсутствием связи с другими')
        pdf.drawString(75, 678, 'объектами дисциплины, выводами и доказательностью. Речь неграмотная.')


    if (form.comboBox_4.currentText() == ("5-Дан полный, развернутый ответ на поставленный вопрос, показана\n"
        "совокупность осознанных знаний об объекте, проявляющаяся в свободном\n"
        "оперировании понятиями, умении выделить существенные и\n"
        "несущественные его признаки, причинно-следственные связи. Знание об\n"
        "объекте демонстрируется на фоне понимания его в системе данной науки и\n"
        "междисциплинарных связей")):
        pdf.drawString(85, 663, 'Дан полный, развернутый ответ на вопрос, показана совокупность осознанных знаний об объекте,')
        pdf.drawString(75, 648, 'умение выделять существенные признаки и причинно-следственные связи.')
    elif (form.comboBox_4.currentText() == ("4- Дан полный, развернутый ответ на поставленный вопрос, доказательно\n"
            "раскрыты основные положения темы; B ответе прослеживается четкая\n"
            "структура, логическая последовательность, отражающая сущность\n"
            "раскрываемых понятий, теорий, явлений.")):
        pdf.drawString(85, 663, 'Дан полный, развернутый ответ на поставленный вопрос, четкая структура, логическая,')
        pdf.drawString(75, 648, 'логическая последовательность и основные положения темы представлены в полном ответе.')
    elif (form.comboBox_4.currentText() == (
            "3-Дан полный, но недостаточно последовательный ответ на поставленный\n"
            "вопрос, но при этом показано умение выделить существенные и\n"
            "несущественные признаки и причинно-следственные связи. Ответ логичен\n"
            "и изложен в терминах науки. Могут быть допущены 1-2 ошибки в\n"
            "определении основных понятий\n")):
        pdf.drawString(90, 663, 'Частично последовательный ответ, некоторые ошибки в определении понятий, но в целом ')
        pdf.drawString(75, 648, 'выделяются существенные признаки и причинно-следственные связи. ')
    elif (form.comboBox_4.currentText() == (
            "2-Дан неполный ответ, представляющий собой разрозненные знания по теме\n"
            "вопроса с существенными ошибками в определениях. Присутствуют\n"
            "фрагментарность, нелогичность изложения. Студент не осознает связь\n"
            "данного понятия, теории, явления с другими объектами дисциплины\n"
            "(модуля). Отсутствуют выводы, конкретизация и доказательность\n"
            "изложения. Речь неграмотная.")):
        pdf.drawString(90, 663, 'Неполный и нелогичный ответ с ошибками в определениях, отсутствием связи с другими')
        pdf.drawString(75, 648, 'объектами дисциплины, выводами и доказательностью. Речь неграмотная.')

    pdf.drawString(70, 738, '1. ___________________________________________________________________________________')
    pdf.drawString(70, 720, '_____________________________________________________________________________________')
    pdf.drawString(70, 693, '2. ___________________________________________________________________________________')
    pdf.drawString(70, 678, '_____________________________________________________________________________________')
    pdf.drawString(70, 663, '3. ___________________________________________________________________________________')
    pdf.drawString(70, 648, '_____________________________________________________________________________________')
    pdf.drawString(70, 633, '_____________________________________________________________________________________')
    pdf.drawString(70, 621,
                   'Мнения председателя и членов государственной экзаменационной комиссии о выявленном в ходе ')
    pdf.drawString(70, 606, 'государственного аттестационного испытания уровне подготовленности обучающегося к ')
    pdf.drawString(70, 591, 'решению профессиональных задач ')
    pdf.drawString(70, 576, '_____________________________________________________________________________________')
    pdf.drawString(70, 561, '_____________________________________________________________________________________')
    pdf.drawString(70, 546, 'о выявленных недостатках в теоретической и практической подготовке ')
    pdf.drawString(70, 531, 'обучающегося_______________________________________________________________________')
    pdf.drawString(70, 516, '____________________________________________________________________________________')
    pdf.drawString(70, 501, '____________________________________________________________________________________')
    pdf.drawString(70, 486, '____________________________________________________________________________________')
    pdf.drawString(70, 450, 'Признать, что обучающийся защитил выпускную квалификационную работу с оценкой  ')
    pdf.drawString(70, 435, '___________________________________________________________________________ ')
    pdf.drawString(70, 435, '___________________________________________________________________________ ')

    # italic текст 10
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 12)

    pdf.drawString(270, 425, '(оценка прописью)')

    # жирный 12 текст
    font_path = "timesNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanBold", font_path))
    pdf.setFont("TimesNewRomanBold", 12)

    pdf.drawString(70, 400, 'РЕШЕНИЕ ГЭК: ')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(70, 385, 'На основании результатов прохождения государственной итоговой аттестации:')
    pdf.drawString(70, 360, '–  Государственный экзамен сдан с оценкой_______________________________________________')

    # italic текст 10
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 10)

    pdf.drawString(370, 348, '(оценка прописью)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(70, 333, '(протокол заседания ГЭК по приему государственного экзамена от _____________ № _______);')
    pdf.drawString(70, 318, '– Выпускная квалификационная работа защищена с оценкой ________________________________ ')

    # italic текст 10
    font_path = "timesNewRomanItalic.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRomanItalic", font_path))
    pdf.setFont("TimesNewRomanItalic", 10)

    pdf.drawString(420, 308, '(оценка прописью)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(70, 280, 'Присвоить ___________________________________________________________________________')

    # обычный 10 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(250, 270, '(Фамилия Имя Отчество студента (в д.п.)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(70, 255, 'квалификацию_______________________________________________________________________,')

    # обычный 10 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(260, 245, '(бакалавр/ специалист/ магистр)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    #
    #
    pdf.drawCentredString(300, 216, diploma)
    #
    #

    pdf.drawString(70, 215, 'Выдать диплом _______________________________________________________________________')

    # обычный 10 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(120, 205,
                   '(бакалавра/бакалавра с отличием; специалиста/специалиста с отличием; магистра/магистра с отличием')
    pdf.drawString(270, 195, '- выбрать нужное)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    #
    #
    pdf.drawCentredString(99, 155, yesIs)
    #
    #

    #
    #
    pdf.drawCentredString(188, 155, noIs)
    #
    #

    #
    #
    pdf.drawCentredString(327, 155, abstainIs)
    #
    #

    pdf.drawString(70, 155, 'За ______, против _________, воздержались __________.')
    pdf.drawString(70, 130, 'Председатель ГЭК ________________ __________________')

    # обычный 10 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(180, 120, '   (подпись)                        (И.О. Фамилия)')

    # обычный 12 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 12)

    pdf.drawString(70, 100, 'Секретарь ГЭК ______________   ______________________')

    # обычный 10 текст
    font_path = "timesNewRoman.ttf"
    pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
    pdf.setFont("TimesNewRoman", 10)

    pdf.drawString(180, 90, '   (подпись)                        (И.О. Фамилия)')

    pdf.save()


form.pushButton.clicked.connect(on_click)

app.exec()