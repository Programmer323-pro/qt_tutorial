import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsLinearLayout, QGraphicsWidget, QMainWindow

def create_layout():
   # Create a QGraphicsLinearLayout with vertical orientation
   layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)

   # Create a QGraphicsWidget to hold the layout
   container_widget = QGraphicsWidget()

   # Add the layout to the container widget
   container_widget.setLayout(layout)

   return container_widget

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = QMainWindow()

   # Create a QGraphicsView and set the scene
   view = QGraphicsView()
   scene = QGraphicsScene()
   view.setScene(scene)

   # Add the layout to the scene
   layout_widget = create_layout()
   scene.addItem(layout_widget)

   # Set the background color of the window
   palette = window.palette()
   # Set your desired color
   palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 0))  
   window.setPalette(palette)

   # Adjust the window size
   window.setGeometry(100, 100, 400, 200)
   window.show()

   sys.exit(app.exec())