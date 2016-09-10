from decouple import config
from pyqode.qt.QtWidgets import QWidget
from pyqode.qt.QtWidgets import QMainWindow
from pyqode.qt.QtWidgets import QHBoxLayout
from pyqode.qt.QtWidgets import QVBoxLayout
from .create import Create
from .data.search import Search


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


class Window(QWidget, Create, Search):
    def __init__(self, parent):
        super(Window, self).__init__(parent)
        self.lbs = (
            (1, 'Loja', 25, 455),
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

        for i in range(1, 15):
            hbox[i] = QHBoxLayout()
            vbox.addLayout(hbox[i], 0)

        hbox[1].addWidget(self.create_label('Codigo', width=45))
        self.info_labels['Codigo'] = self.create_entry()
        hbox[1].addWidget(self.info_labels['Codigo'])

        for lb in self.lbs:
            hbox[lb[0]].addWidget(self.create_label(lb[1], width=lb[2]))
            self.info_labels[lb[1]] = self.create_label(
                info=True, width=lb[3])
            hbox[lb[0]].addWidget(self.info_labels[lb[1]])

        self.btn_search = self.create_btn('Busca', width=570, func=self.search)
        hbox[7].addWidget(self.btn_search)

        hbox[8].addWidget(self.create_label('Ip1', width=15))
        hbox[8].addWidget(self.create_label(info=True, width=100))
        hbox[8].addWidget(self.create_entry(True))
        hbox[8].addWidget(self.create_btn('SSH', func=self.search))
        hbox[8].addWidget(self.create_btn('VNC', func=self.search))
        hbox[8].addWidget(self.create_btn('Box', func=self.search))

        hbox[10].addWidget(self.create_label('Ip2', width=15))
        hbox[10].addWidget(self.create_label(info=True, width=100))
        hbox[10].addWidget(self.create_entry(True))
        hbox[10].addWidget(self.create_btn('SSH', func=self.search))
        hbox[10].addWidget(self.create_btn('VNC', func=self.search))
        hbox[10].addWidget(self.create_btn('Box', func=self.search))

        hbox[12].addWidget(self.create_label('Roteador', width=45))
        hbox[12].addWidget(self.create_label(info=True, width=100))
        hbox[12].addWidget(self.create_btn('Box', func=self.search))
        
        hbox[14].addWidget(self.create_label('SonicWall', width=45))
        hbox[14].addWidget(self.create_label(info=True, width=100))
        hbox[14].addWidget(self.create_btn('Box', func=self.search))
        

    def search(self):
        info = self.search_store(self.info_labels['Codigo'].text())
        if info:
            self.set_data(info)
        
        else:
            self.show_msg()

    def set_data(self, info):
        self.info_labels['Loja'].setText(info.store)
        self.info_labels['Ip1'].setText(info.ip1)
        self.info_labels['Ip2'].setText(info.ip2)
        self.info_labels['Roteador'].setText(info.router)
        self.info_labels['SonicWall'].setText(info.sonicwall)
        self.info_labels['Ramal'].setText(info.ramal)
        self.info_labels['Telefone'].setText(info.phone)
        self.info_labels['Grife'].setText(info.label)
        self.info_labels['Tipo'].setText(info.local)
        self.info_labels['CEP'].setText(info.cep)
        self.info_labels['Designação'].setText(info.desigination)
        self.info_labels['CNPJ'].setText(info.cnpj)
        self.info_labels['Inscrição estadual'].setText(info.ie)
        self.info_labels['Supervisor'].setText(info.supervisor)
        self.info_labels['UF'].setText(info.uf)
        self.info_labels['Cidade'].setText(info.city)
        self.info_labels['Endereço'].setText(info.address)
