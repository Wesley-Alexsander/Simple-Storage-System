import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow
                               , QComboBox ) # import ComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # Dando nome para janela
        self.setWindowTitle('ComboBox - Lista de itens drop down')

        # instanciando ComboBox
        self.itens_list = QComboBox()

        # 01° Forma de adicionar separadamente os itens na comboBox
        self.itens_list.addItem('Carro')
        self.itens_list.addItem('Moto')
        self.itens_list.addItem('Barco')
        self.itens_list.addItem('Avião')

        # 02° Forma de adicionar todos itens na comboBox de uma unica vez.
        self.itens_list.addItems(['Submarino', 'Foguete'])

        # # Tornar o ComboBox Editavel
	    # self.itens_list.setMaxCount(10) # Limite de 10 elementos

        # # Tornar o ComboBox Editavel
        # self.itens_list.setEditable(True)       

        # Centralizando na janela (Central Widget)
        self.setCentralWidget(self.itens_list)

        # ========== Pegando (Texto / Indice) ========== #
       
        # Pegando o indice dos itens
        self.itens_list.currentIndexChanged.connect(self.get_index)

        # Pegando o texto dos itens
        # self.itens_list.currentTextChanged.connect(self.get_text)
        print(self.itens_list.currentText())
        #
        

    # ================== Funções executadas pelo ComboBox ================== #

    def get_index(self):
        print(f'O indice é:')
        print(self.itens_list.currentText())

                
# ======= Exec App ======= #

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
