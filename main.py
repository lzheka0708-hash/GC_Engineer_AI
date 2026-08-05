import sys
from PySide6.QtWidgets import QApplication
from ui.windows.main_window import Mainwindow
def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()    