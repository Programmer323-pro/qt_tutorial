from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication([])
# Create a QWidget
widget = QWidget()
# Create a QVBoxLayout
layout = QVBoxLayout(widget)
# Create a QPushButton
button = QPushButton('Click me!')
# Set contents margins for the layout
layout.setContentsMargins(30, 30, 30, 30)
# Set spacing between widgets
layout.setSpacing(10)
# Add the button to the layout
layout.addWidget(button)
widget.show()
app.exec()