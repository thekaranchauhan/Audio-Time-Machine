import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog

class AudioTimeMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Time Machine")
        self.setGeometry(100, 100, 1000, 600)

        # Label to display welcome message
        label = QLabel("Welcome to Audio Time Machine!", self)
        label.setGeometry(50, 50, 300, 50)
        label.setWordWrap(True)

        # Button to load audio file
        self.load_button = QPushButton("Load Audio File", self)
        self.load_button.move(50, 100)
        self.load_button.clicked.connect(self.load_audio_file)

        # Label to display selected file path
        self.file_label = QLabel("No file selected", self)
        self.file_label.move(50, 150)
        self.file_label.setFixedWidth(700)  # Wide enough for long paths

        # Variable to store the selected file path
        self.audio_file_path = None

    def load_audio_file(self):
        # Open file dialog to select audio file
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Audio File",
            "",  # Default directory (current dir)
            "Audio Files (*.mp3 *.wav *.ogg *.flac)"  # Supported formats
        )
        
        if file_path:
            # Update the label and store the path
            self.audio_file_path = file_path
            self.file_label.setText(f"Selected: {file_path}")
        else:
            self.file_label.setText("No file selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioTimeMachine()
    window.show()
    sys.exit(app.exec_())