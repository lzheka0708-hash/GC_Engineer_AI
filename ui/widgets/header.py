from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QLineEdit,
)
from PySide6.QtCore import Qt
class Header(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        self.title = QLabel("Главная")
        self.title.setObjectName("pageTitle")
        self.search = QLineEdit()
        self.search.setPlaceholderText("Поиск...")
        self.status = QLabel("🟢 Локальный ИИ")
        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.search)
        layout.addWidget(self.status)