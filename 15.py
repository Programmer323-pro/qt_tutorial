import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor
class Color(QWidget):
   def __init__(self, color):
      super().__init__()
      self.setAutoFillBackground(True)
      # default palette for current style
      palette = self.palette()
      # Modify the color
      palette.setColor(self.backgroundRole(), QColor(color))
      self.setPalette(palette)

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      # Setting window title
      self.setWindowTitle("My App")

      layout = QVBoxLayout()
      layout.addWidget(Color('orange'))
      layout.addWidget(Color('blue'))
      layout.addWidget(Color('green'))

      widget = QWidget()
      widget.setLayout(layout)
      self.setCentralWidget(widget)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())