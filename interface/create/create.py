from pyqode.qt.QtCore import QRegExp
from pyqode.qt.QtGui import QRegExpValidator
from pyqode.qt.QtWidgets import QLabel
from pyqode.qt.QtWidgets import QLineEdit
from pyqode.qt.QtWidgets import QPushButton
from pyqode.qt.QtWidgets import QMessageBox
from pyqode.core.widgets import OutputWindow


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
            regexp = r'^([0-9]{2})$'
        else:
            regexp = r'^([a-zA-Z0-9]{2})$'
 
        entry.setValidator(QRegExpValidator(QRegExp(regexp)))
        return entry

    def show_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Loja não encontrada')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def create_term(self):
        term = OutputWindow()
        return term