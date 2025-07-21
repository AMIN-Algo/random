from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Рандомное число')
main_win.resize(400, 200)


button = QPushButton('сгенерировать')
text = QLabel('Нажми чтобы узнать победителя')
text_2 = QLabel('?')
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(text_2, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)

def show_win():
    nomber= randint(0, 99)
    text_2.setText(str(nomber))
    text.setText('Победитель:')

button.clicked.connect(show_win)

main_win.setStyleSheet('''background-color: red;
                       color: white;
                       font-size: 20px''')
button.setStyleSheet('''background-color: grey;
                     color: black''')
text.setStyleSheet('''color: black;''')
text_2.setStyleSheet('''color: yellow''')


main_win.show()
app.exec()