#create a memory card application
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QRadioButton, QLabel
from random import shuffle #to shuffle the answer option
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('The national language of Brazil', 'Portuguese', 'Italian', 'Spanish', 'Brazilian'))
question_list.append(Question('When is the idependence day of indonesia?', '17 august 1945', '30 august 1945', '1 july 1945', '27 november 1945'))
question_list.append(Question('Who is considered the Father of the Renaissance and painted the famous Mona Lisa?', 'Leonardo da Vinci', 'Raphael', 'Michelangelo', 'Donatello' ))
question_list.append(Question('Which Italian city is often regarded as the birthplace of the Renaissance?', 'Rome', 'Milan', 'Venice', 'Florence'))
question_list.append(Question('Who sculpted the iconic statue David, which is considered a masterpiece of Renaissance sculpture?', 'Michelangelo', 'Leonardo da Vinci', 'Donatello', 'Raphael' ))
question_list.append(Question('Which Renaissance artist is known for his frescoes in the Sistine Chapel, including The Creation of Adam?', 'Michelangelo', 'Leonardo da Vinci', 'Raphael', 'Donatello' ))
question_list.append(Question('Who painted The Last Supper, a famous mural depicting the final meal of Jesus with his disciples?', 'Leonardo da Vinci', 'Michelangelo', 'Donatello', 'Raphael' ))
question_list.append(Question('Which Renaissance artist is known for his Madonnas and The School of Athens fresco in the Vatican?,' 'Raphael', 'Michelangelo', 'Donatello', 'Leonardo da Vinci', 'venice' ))
question_list.append(Question('Which Renaissance artist is known for his The Adoration of the Magi and The Baptism of Christ?', 'Leonardo da Vinci', 'Raphael', 'Donatello', 'Michelangelo' ))
question_list.append(Question('Which Renaissance artist is famous for his bronze statue of David and Gattamelata?', 'Donatello', 'Michelangelo', 'Raphael', 'Leonardo da Vinci' ))

app = QApplication([]) #set the memory card
window = QWidget()
window.setWindowTitle("Memory Card")
window.setGeometry(300, 200, 400, 400) #coordinate

question_label = QLabel("question")
option1 = QRadioButton('option1')
option2 = QRadioButton('option2')
option3 = QRadioButton('option3')
option4 = QRadioButton('option4')

optionGroup = QButtonGroup()
optionGroup.addButton(option1) #add button to the answer
optionGroup.addButton(option2)
optionGroup.addButton(option3)
optionGroup.addButton(option4)

hbox1 = QHBoxLayout()
hbox1.addWidget(option1) 
hbox1.addWidget(option3) 

hbox2 = QHBoxLayout()
hbox2.addWidget(option2)
hbox2.addWidget(option4)

layoutvbox = QVBoxLayout()
layoutvbox.addLayout(hbox1)
layoutvbox.addLayout(hbox2)

question_groupbox = QGroupBox('Answer options')
question_groupbox.setLayout(layoutvbox)
answer_groupbox = QGroupBox('Test result')
result_label = QLabel('Are you correct or not?')
correct_label2 = QLabel('The answer will be here!')
layoutvbox_result = QVBoxLayout()
layoutvbox_result.addWidget(result_label)
layoutvbox_result.addWidget(correct_label2)
answer_groupbox.setLayout(layoutvbox_result)


# layout = QVBoxLayout()
# layout.addWidget(answer_groupbox)

button = QPushButton('Answer')
layout = QVBoxLayout()
layout.addWidget(question_label)
layout.addWidget(question_groupbox)
layout.addWidget(answer_groupbox)
answer_groupbox.hide()
layout.addWidget(button)
window.setLayout(layout)

def show_result():
    question_groupbox.hide()
    answer_groupbox.show()
    button.setText('Next question') #showing the result after tap next quest

def show_question(): 
    question_groupbox.show()
    answer_groupbox.hide()
    button.setText('Answer')
    optionGroup.setExclusive(False) #for resetting the options
    option1.setChecked(False)
    option2.setChecked(False)
    option3.setChecked(False)
    option4.setChecked(False)
    optionGroup.setExclusive(True)

answers = [option1, option2, option3, option4]

def ask(q: Question):
    shuffle(answers) #shuffeling the answer
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question)
    correct_label2.setText(q.right_answer)
    show_question()

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    window.total += 1 #for questions
    print('Statistic\n-Total question:', window.total, '\n-Right answer', window.score)
    q = question_list[window.cur_question]
    ask(q)

def show_correct(res):
    result_label.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct')
        window.score += 1 #for adding right answer
        print('Statistic\n-Total question:', window.total, '\n-Right answer:', window.score)
        print('Rating:', (window.score/window.total*100), '%')
    else:
        show_correct('Incorrect') 
        print('Rating', (window.score/window.total*100), '%')

def answering():
    if button.text() == 'Answer':
        check_answer()
    else:
        next_question()
        
window.cur_question = -1

button.clicked.connect(answering)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()