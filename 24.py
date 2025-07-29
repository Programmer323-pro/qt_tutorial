import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
   def __init__(self):
      super().__init__()

      self.setWindowTitle('PyQt Label Widget')
      self.setGeometry(100, 100, 320, 210)

      label = QLabel('This is a QLabel widget')

      layout = QVBoxLayout()
      layout.addWidget(label)
      self.setLayout(layout)

      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())