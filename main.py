import sys
from pyqode.qt.QtWidgets import QMainWindow, QApplication
from interface import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec_())