from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedLayout
app = QApplication([])

# Create main window
main_window = QWidget()
main_window.setWindowTitle("QStackedLayout")

# Create widgets
widget1 = QLabel("Widget 1")
widget2 = QLabel("Widget 2")
widget3 = QLabel("Widget 3")

# Create stacked layout and add widgets to it
stacked_layout = QStackedLayout()
stacked_layout.addWidget(widget1)
stacked_layout.addWidget(widget2)
stacked_layout.addWidget(widget3)

# Create navigation buttons
next_button = QPushButton("Next")
prev_button = QPushButton("Previous")

# Connect buttons to switch between widgets
next_button.clicked.connect(lambda: stacked_layout.setCurrentIndex(stacked_layout.currentIndex() + 1))
prev_button.clicked.connect(lambda: stacked_layout.setCurrentIndex(stacked_layout.currentIndex() - 1))

# Create a vertical layout for the main window
main_layout = QVBoxLayout(main_window)
main_layout.addLayout(stacked_layout)
main_layout.addWidget(prev_button)
main_layout.addWidget(next_button)

# Set the main layout for the main window
main_window.setLayout(main_layout)
main_window.show()
app.exec()