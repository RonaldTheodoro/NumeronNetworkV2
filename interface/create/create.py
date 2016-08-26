from pyqode.qt.QtCore import QRegExp
from pyqode.qt.QtGui import QRegExpValidator
from pyqode.qt.QtWidgets import QLabel
from pyqode.qt.QtWidgets import QLineEdit
from pyqode.qt.QtWidgets import QPushButton


class Create:
    
    def create_label(self, text='', info=False, width=30):
        label = QLabel(text)
        label.setFixedWidth(width)
        label.setFixedHeight(20)

        if info:
            label.setStyleSheet('background-color: white; border: 1px solid;')
        return label

    def create_btn(self, text, width=100, func=None):
        btn = QPushButton(text)
        btn.setFixedWidth(width)
        btn.clicked.connect(func)
        return btn

    def create_entry(self, term=False):
        entry = QLineEdit()
        entry.setFixedWidth(30)

        if term:
            regexp = '^([0-9]{2})$'
        else:
            regexp = '^([a-zA-Z0-9]{2})$'

        validator = QRegExpValidator(QRegExp(regexp))
        entry.setValidator(validator)
        return entry