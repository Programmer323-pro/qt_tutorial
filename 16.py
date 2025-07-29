import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
class MainWindow(QWidget):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.setWindowTitle('PyQt QVBoxLayout')
      # create a layout
      layout = QVBoxLayout()
      self.setLayout(layout)
      # add a spacer
      layout.addStretch()
      # create buttons and add them to the layout
      title = ['A', 'B', 'C', 'D', 'E']
      buttons = [QPushButton(t) for t in title]
      for button in buttons:
         layout.addWidget(button)
      # add a spacer
      layout.addStretch()
      # show the window
      self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())