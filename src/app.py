import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QGridLayout, QApplication, QMainWindow, QPushButton, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle("The Machine GUI")
        # Set the window size
        self.setFixedSize(QSize(400,300))

        # Set Grid layout
        self.layout = QGridLayout()

        # State Variables
        self.is_launching = False

        # Widgets
        self.status = self.create_status_label()
        self.launch_toggle = self.create_launch_button()

        # Add status label to layout
        self.layout.addWidget(self.status, 0, 0)
        # Add launch button to layout
        self.layout.addWidget(self.launch_toggle, 1, 0)
        
        widget = QWidget()
        widget.setLayout(self.layout)
        # Set central widget of the Window to be the button.
        self.setCentralWidget(widget)
    
    def create_launch_button(self):
        # Create a button to initiate launch sequence
        launch_toggle = QPushButton("Initiate Launch")
        launch_toggle.setStyleSheet('background-color: #D3D3D3;')
        launch_toggle.setCheckable(True)
        launch_toggle.clicked.connect(self.initiate_launch)
        launch_toggle.setChecked(self.is_launching)
        return launch_toggle
    
    def create_status_label(self):
        # Create status label
        label = QLabel("Idle")
        label.setAlignment(Qt.AlignmentFlag(4))
        return label
    
    def initiate_launch(self, check):
        self.is_launching = check
        # If the launch has already been started
        # and the user is cancelling the launched
        if not self.is_launching:
            # Cancel the launch
            print("Launch cancelled.")
            self.status.setText("Launch Cancelled.")
            self.launch_toggle.setText("Initiate Launch")
            self.launch_toggle.setStyleSheet('background-color: #D3D3D3;')
        # Otherwise, launch the rocket!
        else:
            # Launch the rocket
            print("Launching!")
            self.status.setText("Launching!")
            self.launch_toggle.setText("Cancel")
            self.launch_toggle.setStyleSheet('background-color: #D22B2B;')


# Create a QApplication instance
# and pass in command line arguments
app = QApplication(sys.argv)

# Create a Qt widget (the window)
window = MainWindow()
# Display the window
window.show()

# Start the event loop.
app.exec()
