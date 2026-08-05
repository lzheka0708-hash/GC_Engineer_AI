from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from ui.pages.chat_page import ChatPage
from ui.pages.diagnostics_page import DiagnosticsPage
from ui.pages.documents_page import DocumentsPage
from ui.pages.home_page import HomePage
from ui.pages.settings_page import SettingsPage
from ui.widgets.sidebar import Sidebar


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GC Engineer AI")
        self.resize(1400, 900)
        self._build_ui()
    def _build_ui(self):
        self.sidebar = Sidebar()
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        self.stack = QStackedWidget()
        self.home_page = HomePage()
        self.chat_page = ChatPage()
        self.diagnostics_page = DiagnosticsPage()
        self.documents_page = DocumentsPage()
        self.settings_page = SettingsPage()
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.chat_page)
        self.stack.addWidget(self.diagnostics_page)
        self.stack.addWidget(self.documents_page)
        self.stack.addWidget(self.settings_page)
        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)
        self.sidebar.chat_clicked.connect(self.show_chat)
        self.sidebar.diagnostics_clicked.connect(self.show_diagnostics)
        self.sidebar.documents_clicked.connect(self.show_documents)
        self.sidebar.settings_clicked.connect(self.show_settings)
        self.sidebar.set_active_button(self.sidebar.chat_btn)
    def show_chat(self):
        self.stack.setCurrentWidget(self.chat_page)
        self.sidebar.set_active_button(self.sidebar.chat_btn)
    def show_diagnostics(self):
        self.stack.setCurrentWidget(self.diagnostics_page)
        self.sidebar.set_active_button(self.sidebar.diagnostics_btn)
    def show_documents(self):
        self.stack.setCurrentWidget(self.documents_page)
        self.sidebar.set_active_button(self.sidebar.docs_btn)
    def show_settings(self):
        self.stack.setCurrentWidget(self.settings_page)
        self.sidebar.set_active_button(self.sidebar.settings_btn)   