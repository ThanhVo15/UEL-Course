import sys
from PyQt6.QtWidgets import QApplication
from Test.MainWindowEx import MainWindowEx

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindowEx()
    main_window.show()
    sys.exit(app.exec())
