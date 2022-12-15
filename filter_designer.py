#!/usr/bin/env python3
import sys
from PySide2.QtWidgets import (
    QApplication,
)

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
