from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QLabel, QPushButton


def make_sentence():
    input_text = text.text()
    label.setText(input_text.capitalize() + ".")


app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentence Maker")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Make")
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

label = QLabel("")
layout.addWidget(label)

window.setLayout(layout)
window.show()
app.exec()