import sys
from PySide6.QtWidgets import QApplication
from ui.windows.main_window import Mainwindow
def main():
    app = QApplication(sys.argv)
    with open("ui/styles/main.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()    