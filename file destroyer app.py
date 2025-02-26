from PyQt6.QtWidgets import QLabel, QApplication, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QVBoxLayout, QWidget,QLineEdit, QFileDialog
from pathlib import Path


def open_file():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")


def destroy_file():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            file.write(b'')
        path.unlink()


app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

label = QLabel("Select the files you want to destroy. It will be <font colour='red'>permanently</font> deleted.")

btn2 = QPushButton("Open files")
layout.addWidget(btn2)
btn2.clicked.connect(open_file)

btn1 = QPushButton("Destroy the files")
layout.addWidget(btn1)
btn1.clicked.connect(destroy_file)

window.show()
app.exec()