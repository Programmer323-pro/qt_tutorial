from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.spinBox = QSpinBox(self)
      self.spinBox.valueChanged.connect(self.on_spinbox_valueChanged)

   @pyqtSlot(int)
   def on_spinbox_valueChanged(self, value):
      print("Integer value changed:", value)

if __name__ == "__main__":
   app = QApplication([])
   window = MainWindow()
   window.show()
   app.exec_()