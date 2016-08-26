from pyqode.qt.QtWidgets import QLabel
from pyqode.qt.QtWidgets import QPushButton


class Create:
    
    def create_label(self, text='', info=False, width=30):
        label = QLabel(text)
        label.setFixedWidth(width)
        label.setFixedHeight(20)

        if info:
            label.setStyleSheet('background-color: white; border: 1px solid;')
        return label

    def create_btn(self, text, func=None):
        btn = QPushButton(text)
        btn.clicked.connect(func)
        return btn