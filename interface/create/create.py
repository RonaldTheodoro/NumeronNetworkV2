import os
import sys
from pyqode.qt.QtCore import QRegExp
from pyqode.qt.QtGui import QRegExpValidator
from pyqode.qt.QtWidgets import QLabel
from pyqode.qt.QtWidgets import QLineEdit
from pyqode.qt.QtWidgets import QPushButton
from pyqode.qt.QtWidgets import QMessageBox
from pyqode.core.widgets import OutputWindow


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snippets')

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

    def start_ping(self, term, ip=None):
        term.stop_process()
        if ip is not None:
            term.start_process(
                sys.executable, 
                [os.path.join(BASE_DIR, 'ping_test.py'), '-ip', ip]
            )
        else:
            term.start_process(
                sys.executable, [os.path.join(BASE_DIR, 'ping_test.py')])