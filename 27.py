#!/bin/python


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

class MainWindow(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('PyQt QLineEdit Widget')
      self.setGeometry(100, 100, 320, 210)

      password = QLineEdit(echoMode=QLineEdit.EchoMode.Password)

      layout = QVBoxLayout()
      layout.addWidget(password)
      self.setLayout(layout)
      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())