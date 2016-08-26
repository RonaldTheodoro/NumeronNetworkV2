from decouple import config
from pyqode.qt.QtWidgets import QWidget
from pyqode.qt.QtWidgets import QMainWindow
from pyqode.qt.QtWidgets import QHBoxLayout
from pyqode.qt.QtWidgets import QVBoxLayout
from pyqode.qt.QtWidgets import QPushButton
from .create import Create
from .data.search import search_store


class MainWindow(QMainWindow):
    APPVERSION = config('APPVERSION')
    APPCODENAME = config('APPCODENAME')

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Numeron Network')
        self.setFixedSize(600, 700)
        self.window = Window(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.window)
        self.setCentralWidget(_widget)


class Window(QWidget, Create):
    def __init__(self, parent):
        super(Window, self).__init__(parent)
        self.lbs = (
            (1, 'Codigo', 45, 20),
            (1, 'Loja', 25, 465),
            (2, 'Ip1', 15, 100),
            (2, 'Ip2', 15, 100),
            (2, 'Roteador', 45, 100),
            (2, 'SonicWall', 45, 100),
            (3, 'Ramal', 35, 30),
            (3, 'Telefone', 50, 85),
            (3, 'Grife', 30, 100),
            (3, 'Tipo', 25, 60),
            (3, 'CEP', 25, 70),
            (4, 'Designação', 80, 90),
            (4, 'CNPJ', 50, 110),
            (4, 'Inscrição estadual', 105, 105),
            (5, 'Supervisor', 60, 200),
            (5, 'UF', 20, 20),
            (5, 'Cidade', 40, 200),
            (6, 'Endereço', 60, 500)
        )
        self.info_labels = {}
        self.init_ui()
        self.show()

    def init_ui(self):
        hbox = {}
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        for i in range(1, 8):
            hbox[i] = QHBoxLayout()
            vbox.addLayout(hbox[i], 0)

        for lb in self.lbs:
            hbox[lb[0]].addWidget(self.create_label(lb[1], width=lb[2]))
            self.info_labels[lb[1].lower()] = self.create_label(
                info=True, width=lb[3])
            hbox[lb[0]].addWidget(self.info_labels[lb[1].lower()])

        self.btn_search = QPushButton('Busca')
        self.btn_search.clicked.connect(self.search)
        hbox[7].addWidget(self.btn_search)

    def search(self):
        info = search_store('99')
        