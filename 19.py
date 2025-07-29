import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsGridLayout, QGraphicsProxyWidget, QPushButton, QGraphicsWidget
def main():
   app = QApplication(sys.argv)

   # Create a QGraphicsScene
   scene = QGraphicsScene()

   # Create a QGraphicsView and set the scene
   view = QGraphicsView(scene)

   # Create a QGraphicsGridLayout
   layout = QGraphicsGridLayout()

   # Create buttons and add them to the layout
   b1 = QPushButton("Box 1")
   b2 = QPushButton("Box 2")
   b3 = QPushButton("Box 3")
   b4 = QPushButton("Box 4")

   proxy_button1 = QGraphicsProxyWidget()
   proxy_button1.setWidget(b1)
   layout.addItem(proxy_button1, 0, 0)

   proxy_button2 = QGraphicsProxyWidget()
   proxy_button2.setWidget(b2)
   layout.addItem(proxy_button2, 0, 1)

   proxy_button3 = QGraphicsProxyWidget()
   proxy_button3.setWidget(b3)
   layout.addItem(proxy_button3, 1, 0)

   proxy_button4 = QGraphicsProxyWidget()
   proxy_button4.setWidget(b4)
   layout.addItem(proxy_button4, 1, 1)

   # Create a QGraphicsWidget to hold the layout
   widget = QGraphicsWidget()
   widget.setLayout(layout)

   # Add the widget to the scene
   scene.addItem(widget)

   # Show the view
   view.show()

   # Execute the application
   sys.exit(app.exec())

if __name__ == "__main__":
   main()