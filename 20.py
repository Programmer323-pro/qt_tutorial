import sys
from PyQt5.QtCore import QSizeF, Qt
from PyQt5.QtWidgets import (QApplication, QGraphicsAnchorLayout,
QGraphicsProxyWidget, QGraphicsScene, QGraphicsView, QGraphicsWidget,
QPushButton, QSizePolicy)
def createItem(minimum, preferred, maximum, name):
   wid = QGraphicsProxyWidget()

   wid.setWidget(QPushButton(name))
   wid.setMinimumSize(minimum)
   wid.setPreferredSize(preferred)
   wid.setMaximumSize(maximum)
   wid.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

   return wid
if __name__ == '__main__':

   app = QApplication(sys.argv)

   scene = QGraphicsScene()
   scene.setSceneRect(0, 0, 800, 480)

   minSize = QSizeF(30, 100)
   prefSize = QSizeF(210, 100)
   maxSize = QSizeF(300, 100)

   a = createItem(minSize, prefSize, maxSize, "BOX 1")
   b = createItem(minSize, prefSize, maxSize, "BOX 2")
   c = createItem(minSize, prefSize, maxSize, "BOX 3")
   d = createItem(minSize, prefSize, maxSize, "BOX 4")
   e = createItem(minSize, prefSize, maxSize, "BOX 5")
   f = createItem(QSizeF(30, 50), QSizeF(150, 50), maxSize, "BOX 6")
   g = createItem(QSizeF(30, 50), QSizeF(30, 100), maxSize, "BOX 7")

   lay = QGraphicsAnchorLayout()
   lay.setSpacing(0)

   wid2 = QGraphicsWidget(None, Qt.Window)
   wid2.setPos(20, 20)
   wid2.setLayout(lay)

   # Vertical
   lay.addAnchor(a, Qt.AnchorTop, lay, Qt.AnchorTop)
   lay.addAnchor(b, Qt.AnchorTop, lay, Qt.AnchorTop)

   lay.addAnchor(c, Qt.AnchorTop, a, Qt.AnchorBottom)
   lay.addAnchor(c, Qt.AnchorTop, b, Qt.AnchorBottom)
   lay.addAnchor(c, Qt.AnchorBottom, d, Qt.AnchorTop)
   lay.addAnchor(c, Qt.AnchorBottom, e, Qt.AnchorTop)

   lay.addAnchor(d, Qt.AnchorBottom, lay, Qt.AnchorBottom)
   lay.addAnchor(e, Qt.AnchorBottom, lay, Qt.AnchorBottom)

   lay.addAnchor(c, Qt.AnchorTop, f, Qt.AnchorTop)
   lay.addAnchor(c, Qt.AnchorVerticalCenter, f, Qt.AnchorBottom)
   lay.addAnchor(f, Qt.AnchorBottom, g, Qt.AnchorTop)
   lay.addAnchor(c, Qt.AnchorBottom, g, Qt.AnchorBottom)

   # Horizontal
   lay.addAnchor(lay, Qt.AnchorLeft, a, Qt.AnchorLeft)
   lay.addAnchor(lay, Qt.AnchorLeft, d, Qt.AnchorLeft)
   lay.addAnchor(a, Qt.AnchorRight, b, Qt.AnchorLeft)

   lay.addAnchor(a, Qt.AnchorRight, c, Qt.AnchorLeft)
   lay.addAnchor(c, Qt.AnchorRight, e, Qt.AnchorLeft)

   lay.addAnchor(b, Qt.AnchorRight, lay, Qt.AnchorRight)
   lay.addAnchor(e, Qt.AnchorRight, lay, Qt.AnchorRight)
   lay.addAnchor(d, Qt.AnchorRight, e, Qt.AnchorLeft)

   lay.addAnchor(lay, Qt.AnchorLeft, f, Qt.AnchorLeft)
   lay.addAnchor(lay, Qt.AnchorLeft, g, Qt.AnchorLeft)
   lay.addAnchor(f, Qt.AnchorRight, g, Qt.AnchorRight)

   scene.addItem(wid2)
   scene.setBackgroundBrush(Qt.lightGray)

   view = QGraphicsView(scene)
   view.show()
   sys.exit(app.exec_())