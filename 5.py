import sys
from PyQt5.QtWidgets import QApplication, QPushButton

def greet():
   print("Hello, PyQt!")

def farewell():
   print("Goodbye, PyQt!")

app = QApplication(sys.argv)
button = QPushButton("Click Me")
button.clicked.connect(greet)
button.clicked.connect(farewell)
button.show()
sys.exit(app.exec_())