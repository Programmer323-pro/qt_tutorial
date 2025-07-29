import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
class ExampleWidget(QWidget):
   def __init__(self):
      super().__init__()
      self.initUI()
   def initUI(self):
      # Create widgets
      b1 = QPushButton('A', self)
      b2 = QPushButton('B', self)
      b3 = QPushButton('C', self)

      # Create horizontal layout
      h_box = QHBoxLayout()
      h_box.addWidget(b1)
      h_box.addWidget(b2)
      h_box.addWidget(b3)

      # Set spacing between widgets
      h_box.setSpacing(70)

      # Set content margins
      h_box.setContentsMargins(50, 50, 50, 50)

      # Set the layout for the main window
      self.setLayout(h_box)

      self.setGeometry(300, 300, 300, 150)
      self.setWindowTitle('QHBoxLayout Margin')
      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = ExampleWidget()
   sys.exit(app.exec())