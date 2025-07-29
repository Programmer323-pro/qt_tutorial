from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
class TwoColumnLayout(QWidget):
   def __init__(self):
      super().__init__()

      # Create a QGridLayout instance
      layout = QGridLayout()
      # Add widgets to the layout
      for i in range(10):
         layout.addWidget(QPushButton(f'Box {i+1}'), i // 2, i % 2)
      # Set the layout on the application's window
      self.setLayout(layout)

app = QApplication([])
window = TwoColumnLayout()
window.setWindowTitle('PyQt')
window.show()
app.exec()