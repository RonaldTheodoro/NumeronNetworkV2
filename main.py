import sys
from pyqode.qt.QtWidgets import QMainWindow, QApplication
from interface import MainWindow


def main():
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
            
    