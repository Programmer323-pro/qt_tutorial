import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QFormLayout
class MainWindow(QWidget):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.setWindowTitle('Sign Up Form')

      layout = QFormLayout()
      self.setLayout(layout)

      layout.addRow('Enter the name:', QLineEdit(self))
      layout.addRow('Enter the Email:', QLineEdit(self))
      layout.addRow('Enter the Pincode:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
      layout.addRow('Enter the Mobile Number:', QLineEdit(self))
      layout.addRow(QPushButton('Sign Up Form'))

      # show the window
      self.show()
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec())