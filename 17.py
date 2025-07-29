import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton, QStackedLayout 


class MyWindow(QMainWindow):
   def __init__(self):
      super().__init__()

      # Create the main window
      self.setWindowTitle("Page Switcher")
      self.setGeometry(200, 200, 600, 500)

      # Create the stacked layout
      self.stackedLayout = QStackedLayout()

      # Create Page 1
      self.page1Widget = QWidget()
      page1Layout = QVBoxLayout()
      page1Button = QPushButton("Go to Page 2")
      page1Button.clicked.connect(self.switch_to_page2)
      page1Layout.addWidget(page1Button)
      self.page1Widget.setLayout(page1Layout)

      # Create Page 2
      self.page2Widget = QWidget()
      page2Layout = QVBoxLayout()
      page2Button = QPushButton("Go to Page 1")
      page2Button.clicked.connect(self.switch_to_page1)
      page2Layout.addWidget(page2Button)
      self.page2Widget.setLayout(page2Layout)

      # Add pages to the stacked layout
      self.stackedLayout.addWidget(self.page1Widget)
      self.stackedLayout.addWidget(self.page2Widget)

      # Set the initial page
      self.stackedLayout.setCurrentIndex(0)

      # Set the central widget
      centralWidget = QWidget()
      centralWidget.setLayout(self.stackedLayout)
      self.setCentralWidget(centralWidget)

   def switch_to_page1(self):
      self.stackedLayout.setCurrentIndex(0)

   def switch_to_page2(self):
      self.stackedLayout.setCurrentIndex(1)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = MyWindow()
   window.show()
   sys.exit(app.exec())