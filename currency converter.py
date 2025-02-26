from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from{in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_= "ccOutputRslt").getText()
    rate = float(rate[:-4])

    return rate


def make_conversion():
    input_amount = float(text.text())
    input_currency = in_currency.currentText()
    output_currency = out_currency.currentText()
    rate = get_currency(input_currency, output_currency)
    conversion = round(input_amount * rate, 2)
    output.setText(f"{input_amount} {input_currency} is equal to {conversion} {output_currency}")


app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output = QLabel("")
layout.addWidget(output)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

text = QLineEdit()
layout3.addWidget(text)

in_currency = QComboBox()
in_currency.addItems(["USD", "EUR", "GPB"])
layout2.addWidget(in_currency)

out_currency = QComboBox()
out_currency.addItems(["USD", "EUR", "GPB"])
layout2.addWidget(out_currency)

btn = QPushButton("Convert")
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(make_conversion)

window.setLayout(layout)
window.show()
app.exec()