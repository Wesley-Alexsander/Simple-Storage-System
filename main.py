from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys
from functionality import ConsultaExterna
import dbc

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Simple Storage Service")

        # Configurando menu Ativo
        self.icon_only_widget.hide()
        self.paginas.setCurrentWidget(self.pg_home)
        
        # Configurando botões menu
        self.btn_home_02.setChecked(True)

        # Conexao banco 
        self.database = dbc.DataBase()

        # Instanciando Classe Fornecedor
        self.Fornecedor = dbc.Fornecedor()

        # Instanciando Classe Produto
        self.Produto = dbc.Produto()

        # Instanciando Classe AtualizarEstoque
        self.AtualizarEstoque = dbc.AtualizarEstoque()

        # Instanciando Classe AtualizarEstoque
        self.Pesquisar_Produtos = dbc.PesquisarProdutos()
        
        
        

        ########################################################################################
        # Paginas do sistema

        # Menu retraido (Icon_only_widget)
        self.btn_home_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_cadastro_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_cadastro))
        self.btn_estoque_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_manuseio_01.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_manuseio))

        # Menu aberto (Full_menu_widget)
        self.btn_home_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_home))
        self.btn_cadastro_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_cadastro))
        self.btn_estoque_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_estoque))
        self.btn_manuseio_02.clicked.connect(lambda: self.paginas.setCurrentWidget(self.pg_manuseio))
        ########################################################################################


        ########################################################################################
        # CADASTRO DE FORNECEDORES:

        # Lista de tipos de produtos
        self.cb_tipo.addItems(
            [
            ''   
            , 'Camisetas'
            , 'Motelom'
            , 'Calças'
            , 'Camisas Sociais'
            , 'Sueters'
            , 'Calças Sociais'
            , 'Blazers'
            ] 
        )
        # Bloqueando item em banco (Não será possivel selecionar item em branco, após escolher um tipo)
        self.cb_tipo.model().item(0).setEnabled(False)
        # Preenchimento automatioco
        self.txt_cnpj.editingFinished.connect(self.consulta_cnpj)

        # registrar clientes
        self.btn_cadastrar_fornecedor.clicked.connect(self.registrar_empresa)

        # limpar campos
        self.btn_limpar_fornecedor.clicked.connect(self.limpar_campos)
        ########################################################################################


                



        ########################################################################################
        # ENTRADA DE PRODUTOS:
        self.txt_sku_entrada.setPlaceholderText('Insira o Sku')
        self.txt_tipo_entrada.setPlaceholderText('Tipo do Produto')
        self.txt_nome_entrada.setPlaceholderText('Insira o nome Produto')
        self.cb_tamanho_entrada.setPlaceholderText('Tamanhos')
        

        self.cb_tamanho_entrada.addItems(
                [
                ''
                , 'PP'
                , 'P'
                , 'M'
                , 'G'
                , 'GG'
                , 'EXG'
                , 'EXGG'
                , '-------------------------------'
                , '36'
                , '38'
                , '40'
                , '42'
                , '44'
                , '46'
                , '48'
                , '50'
                , '52'
                ]   
            )
        # Bloqueando item em banco (Não será possivel selecionar item em branco, após escolher um tipo)
        self.cb_tamanho_entrada.model().item(0).setEnabled(False)
        self.cb_tamanho_entrada.model().item(8).setEnabled(False)

        # Depois de digitar o sku e pressionar ENTER, irá preencher os campos
        self.txt_sku_entrada.editingFinished.connect(self.preencher_entrada)
        
        # Botão cadastrar
        self.btn_cadastrar_entrada.clicked.connect(self.entrada_produtos)

        # Botão limpar
        self.btn_limpar_entrada.clicked.connect(self.limpar_campos)


        ########################################################################################




       ########################################################################################
        # SAIDA DE PRODUTOS:
        self.txt_sku_entrada.setPlaceholderText('Insira o Sku')
        self.txt_tipo_entrada.setPlaceholderText('Tipo do Produto')
        self.txt_nome_entrada.setPlaceholderText('Insira o nome Produto')
        self.cb_tamanho_2.setPlaceholderText('Tamanhos')
        

        self.cb_tamanho_2.addItems(
                [
                ''
                , 'PP'
                , 'P'
                , 'M'
                , 'G'
                , 'GG'
                , 'EXG'
                , 'EXGG'
                , '-------------------------------'
                , '36'
                , '38'
                , '40'
                , '42'
                , '44'
                , '46'
                , '48'
                , '50'
                , '52'
                ]   
            )
        # Bloqueando item em banco (Não será possivel selecionar item em branco, após escolher um tipo)
        self.cb_tamanho_2.model().item(0).setEnabled(False)
        self.cb_tamanho_2.model().item(8).setEnabled(False)

        # Depois de digitar o sku e pressionar ENTER, irá preencher os campos
        self.txt_sku_saida.editingFinished.connect(self.preencher_saida)
        
        # Botão cadastrar 
        self.btn_cadastrar_saida.clicked.connect(self.saida_produtos) 

        # Botão limpar
        self.btn_limpar_saida.clicked.connect(self.limpar_campos)


        ########################################################################################

        
        ########################################################################################
        # CADASTRO DE PRODUTOS:

        # Cadastro de Produtos
        self.btn_cadastrar_produto.clicked.connect(self.cadastro_prod)

        # limpar campos
        self.btn_limpar_produto.clicked.connect(self.limpar_campos)
        ########################################################################################




        



    # Criando consulta de api CNPJ
    def consulta_cnpj(self):
        # Criando conexão
        api = ConsultaExterna()
        request = api.pesquisar_cnpj(self.txt_cnpj.text())

        # Recuperando dados
        self.txt_nome.setText(request[0])
        self.txt_logradouro.setText(request[1])
        self.txt_numero.setText(request[2])
        self.txt_complemento.setText(request[3])
        self.txt_bairro.setText(request[4])
        self.txt_municipio.setText(request[5])
        self.txt_uf.setText(request[6])
        self.txt_cep.setText(request[7])
        self.txt_telefone.setText(request[8])
        self.txt_email.setText(request[9])

    def registrar_empresa(self):
        self.Fornecedor.cadastrar_fornecedor(
             self.txt_nome.text()
            , self.txt_logradouro.text()
            , self.txt_numero.text()
            , self.txt_complemento.text()
            , self.txt_bairro.text()
            , self.txt_municipio.text()
            , self.txt_uf.text()
            , self.txt_cep.text()
            , self.txt_telefone.text()
            , self.txt_email.text()
        )
        self.limpar_campos()
        
    
    def cadastro_prod(self):
        self.Produto.cadastrar_produto(
            self.txt_sku_produto.text()
            , self.txt_cnpj_fornecedor_02.text()
            , self.cb_tipo.currentText()
            , self.txt_produto.text()
            , self.spin_custo.value()
            , self.spin_preco.value()
        )
        self.limpar_campos()



    
    
    def preencher_entrada(self):
        tupla = self.Pesquisar_Produtos.pesquisa_sku(self.txt_sku_entrada.text())
        self.txt_tipo_entrada.setText(tupla[2])
        self.txt_nome_entrada.setText(tupla[3])


    def preencher_saida(self):
        tupla = self.Pesquisar_Produtos.pesquisa_sku(self.txt_sku_saida.text())
        self.txt_tipo_saida.setText(tupla[2])
        self.txt_nome_saida.setText(tupla[3])    

    def entrada_produtos(self):
        self.AtualizarEstoque.registrar_entrada(
            self.txt_sku_entrada.text()
            , self.txt_nome_entrada.text()
            , self.txt_tipo_entrada.text()
            , self.cb_tamanho_entrada.currentText()
            , self.spin_quantidade.value()
        )
        self.limpar_campos()

    def saida_produtos(self):
        self.AtualizarEstoque.registrar_saida(
            self.txt_sku_saida.text()
            , self.txt_nome_saida.text()
            , self.txt_tipo_saida.text()
            , self.cb_tamanho_2.currentText()
            , self.spin_quantidade_saida.value()
        ) 
        self.limpar_campos()


    # def combo_text(self, t):
    #     return t
    
    def limpar_campos(self):
        self.txt_cnpj.setText('')
        self.txt_nome.setText('')
        self.txt_logradouro.setText('')
        self.txt_numero.setText('')
        self.txt_complemento.setText('')
        self.txt_bairro.setText('')
        self.txt_municipio.setText('')
        self.txt_uf.setText('')
        self.txt_cep.setText('')
        self.txt_telefone.setText('')
        self.txt_email.setText('')
        self.txt_sku_produto.setText('')
        self.txt_cnpj_fornecedor_02.setText('')
        self.txt_produto.setText('')
        self.spin_custo.setValue(0.00)
        self.spin_preco.setValue(0.00)
        self.cb_tipo.setCurrentIndex(0)
        self.txt_sku_entrada.setText('')
        self.txt_nome_entrada.setText('')
        self.txt_tipo_entrada.setText('')
        self.cb_tamanho_entrada.setCurrentIndex(0)
        self.spin_quantidade.setValue(0)
        self.txt_sku_saida.setText('')
        self.txt_nome_saida.setText('')
        self.txt_tipo_saida.setText('')
        self.cb_tamanho_2.setCurrentIndex(0)
        self.spin_quantidade_saida.setValue(0)
    


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()
    app.exec_()