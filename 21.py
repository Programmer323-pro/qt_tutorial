import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView

class CustomGraphicsItem(QGraphicsRectItem):
   def __init__(self, width, height, color):
      super().__init__()
      self.setRect(0, 0, width, height)
      self.setBrush(QColor(color))

if __name__ == "__main__":
   app = QApplication(sys.argv)
   scene = QGraphicsScene()
   view = QGraphicsView(scene)

   # Create custom graphics items
   box1 = CustomGraphicsItem(100, 50, "lightblue")
   box2 = CustomGraphicsItem(80, 30, "lightgreen")

   # Position the items
   box1.setPos(10, 10)
   box2.setPos(10, 70)

   # Add items to the scene
   scene.addItem(box1)
   scene.addItem(box2)

   view.show()
   sys.exit(app.exec())
