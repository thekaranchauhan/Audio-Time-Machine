import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class AudioTimeMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Time Machine")
        self.setGeometry(100, 100, 1000, 600)  # x, y, width, height
        
        label = QLabel("Welcome to Audio Time Machine!", self)
        label.setGeometry(50, 50, 300, 50)
        label.setWordWrap(True) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioTimeMachine()
    window.show()
    sys.exit(app.exec_())
