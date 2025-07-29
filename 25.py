import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
   def __init__(self):
      super().__init__()

      self.setWindowTitle('PyQt Label Widget')
      self.setGeometry(100, 100, 320, 210)

      label = QLabel()
      pixmap = QPixmap('"C:\\Users\\User\\Desktop\\Windows_logo_-_2021.svg.png"')
      label.setPixmap(pixmap)

      layout = QVBoxLayout()
      layout.addWidget(label)
      self.setLayout(layout)

      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())