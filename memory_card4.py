from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel)
from random import randint, shuffle

app = QApplication([])

btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignCenter)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=1) # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)

layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

class Question:
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Самый лучший язык программирования', 'Python', 'JavaScript', 'C++', 'Java'))
questions_list.append(Question('Кто из этих персонажей не дружит с Гарри Поттером?', 'Драко Малфой', 'Рон Уизли', 'Невилл Лонгботтом', 'Гермиона Грейнджер'))
questions_list.append(Question('Какая планета самая горячая?', 'Венера', 'Сатурн', 'Меркурий', 'Марс'))
questions_list.append(Question('Как назывался корабль капитана Джека Воробья в "Пиратах Карибского моря"?', 'Черная жемчужина', 'Мародер', 'Черный питон', 'Слизерин'))
questions_list.append(Question('Fe — это символ какого химического элемента?', 'Железо', 'Цинк', 'Водород', 'Фтор'))
questions_list.append(Question('Какая планета в нашей Солнечной системе самая большая?', 'Юпитер', 'Сатурн', 'Нептун', 'Земля'))
questions_list.append(Question('Какое животное не фигурирует в китайском зодиаке?', 'Колибри', 'Собака', 'Кролик', 'Дракон'))

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ
    show_question() # показываем панель вопросов

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print(f'Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов: {window.score}')
        print(f'Рейтинг: {window.score/window.total*100}%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print(f'Рейтинг: {window.score/window.total*100}%')

def next_question():
    ''' задает следующий вопрос или завершает викторину '''
    if questions_list:  # Проверяем, остались ли вопросы
        window.total += 1  # Увеличиваем счетчик общего количества вопросов
        print(f'Статистика\n-Всего вопросов: {window.total} \n-Правильных ответов: {window.score}')        
        # Получаем и удаляем случайный вопрос из списка
        cur_question = questions_list.pop(randint(0, len(questions_list) - 1))
        ask(cur_question)  # Задаем вопрос
    else:
        # Если вопросы закончились, завершаем викторину
        lb_Question.setText('Викторина завершена!')
        lb_Result.setText(f'Вы ответили правильно на {window.score} из {window.total} вопросов.')
        btn_OK.hide()  # Скрываем кнопку
        RadioGroupBox.hide()  # Скрываем варианты ответов
        AnsGroupBox.show()  # Показываем панель с результатами
        
# Обработчик нажатия кнопки
def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer()  # Проверка ответа
    else:
        next_question()  # Следующий вопрос

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит

window.score = 0
window.total = 0
next_question()
window.resize(500, 400)
window.show()
app.exec_()
