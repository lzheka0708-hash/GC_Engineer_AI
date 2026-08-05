from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
class Sidebar(QWidget):
    chat_clicked = Signal()
    diagnostics_clicked = Signal()
    documents_clicked = Signal()
    settings_clicked = Signal()
    def __init__(self):
       super().__init__()
       layout = QVBoxLayout(self)
       title = QLabel("GC Engineer\nAI")
       title.setAlignment(Qt.AlignCenter)
       layout.addWidget(title)
       layout.addSpacing(20)
       self.chat_btn = QPushButton("💬 Чат")
       self.chat_btn.setObjectName("menuButton")
       self.chat_btn.clicked.connect(
           self.chat_clicked.emit
       )
       self.diagnostics_btn = QPushButton("🔧 Диагностика")
       self.diagnostics_btn.setObjectName("menuButton")
       self.diagnostics_btn.clicked.connect(
           self.diagnostics_clicked.emit
       )
       self.docs_btn = QPushButton("📄 Документы")
       self.docs_btn.setObjectName("menuButton")
       self.docs_btn.clicked.connect(
           self.documents_clicked.emit
       )
       self.settings_btn = QPushButton("⚙ Настройки")
       self.settings_btn.setObjectName("menuButton")
       self.settings_btn.clicked.connect(
           self.settings_clicked.emit
       )
       layout.addWidget(self.chat_btn)
       layout.addWidget(self.diagnostics_btn)
       layout.addWidget(self.docs_btn)
       layout.addStretch()
       layout.addWidget(self.settings_btn)
       self.setFixedWidth(220)
    def set_active_button(self, button):
         buttons = [
             self.chat_btn,
             self.diagnostics_btn,
             self.docs_btn,
             self.settings_btn,
         ]
         for btn in buttons:
             btn.setProperty("active", False)
             btn.style().unpolish(btn)
             btn.style().polish(btn)
         button.setProperty("active", True)
         button.style().unpolish(button)
         button.style().polish(button)