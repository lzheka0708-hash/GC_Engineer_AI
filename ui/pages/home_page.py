from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("Добро пожаловать в GC Engineer AI")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)