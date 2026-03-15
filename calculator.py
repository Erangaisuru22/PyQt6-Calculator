import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit

class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(250,300)

        layout = QGridLayout()

        # Display
        self.display = QLineEdit()
        layout.addWidget(self.display,0,0,1,4)

        # Buttons
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('=',4,2),('+',4,3),
            ('C',5,0)  # Clear button
        ]

        for text,row,col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.click)
            layout.addWidget(button,row,col)

        self.setLayout(layout)

    def click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif text == "C":
            self.display.clear()  # Clears the input
        else:
            self.display.setText(self.display.text() + text)


app = QApplication(sys.argv)
window = Calculator()
window.show()
app.exec()
