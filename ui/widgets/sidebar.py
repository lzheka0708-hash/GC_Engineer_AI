from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
class Sidebar(QWidget):
    def __init__(self):
       super().__init__()
       layout = QVBoxLayout(self)
       self.chat_btn = QPushButton("💬 Чат")
       self.diagnostics_btn = QPushButton("🔧 Диагностика")
       self.docs_btn = QPushButton("📄 Документы")
       self.settings_btn = QPushButton("⚙ Настройки")
       layout.addWidget(self.chat_btn)
       layout.addWidget(self.diagnostics_btn)
       layout.addWidget(self.docs_btn)
       layout.addStretch()
       layout.addWidget(self.settings_btn)
 