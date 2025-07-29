import sys
from PyQt5.QtCore import QDialog,QPushButton,QObject
from PyQt5.QtGui import QGuiApplication

def window():
   app = QGuiApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   QObject.connect(b2,("clicked()"),b2_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print ("Button 1 clicked")

def b2_clicked():
   print ("Button 2 clicked")

if __name__ == '__main__':
   window()