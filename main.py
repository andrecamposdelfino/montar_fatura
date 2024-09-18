from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
import locale

# importações do banco
import database
from modelo import Credor, Centro, Cartao, Fatura

def msgInfo(msg):
    QMessageBox.information(
        None, 
        "Informação",
        msg
    )

def msgWarning(msg):
    QMessageBox.warning(
        None, 
        "Informação",
        msg
    )



def form_lista_fatura():
    lista_fatura.show()
    dados = database.lista_fatura()
    lista_fatura.dgvDadoCompras.setRowCount(len(dados))
    lista_fatura.dgvDadoCompras.setColumnCount(8)
    lista_fatura.dgvDadoCompras.setColumnWidth(0, 50)
    lista_fatura.dgvDadoCompras.setColumnWidth(1, 70)
    lista_fatura.dgvDadoCompras.setColumnWidth(2, 220)
    lista_fatura.dgvDadoCompras.setColumnWidth(3, 80)
    lista_fatura.dgvDadoCompras.setColumnWidth(4, 60)
    lista_fatura.dgvDadoCompras.setColumnWidth(5, 60)
    lista_fatura.dgvDadoCompras.setColumnWidth(6, 150)
    lista_fatura.dgvDadoCompras.setColumnWidth(7, 120)


    for l in range(0, len(dados)):
        for c in range(0, 8):
            lista_fatura.dgvDadoCompras.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))


def form_lista_credor():
    lista_credor.show()

    dados = database.lista_credor()
    lista_credor.dgvDadosCredor.setRowCount(len(dados))
    lista_credor.dgvDadosCredor.setColumnCount(2)   
    lista_credor.dgvDadosCredor.setColumnWidth(1, 330)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            lista_credor.dgvDadosCredor.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    lista_credor.dgvDadosCredor.cellClicked.connect(recupera_dados_credor)

def listar_por_nome():
    credor = lista_credor.txtPesquisar.text()
    dados = database.lista_credor_nome(credor)
    lista_credor.dgvDadosCredor.setColumnCount(2)   
    lista_credor.dgvDadosCredor.setColumnWidth(1, 330)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            lista_credor.dgvDadosCredor.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    lista_credor.dgvDadosCredor.cellClicked.connect(recupera_dados_credor)


def recupera_dados_credor(row, column):
    item = lista_credor.dgvDadosCredor.item(row, column)
    adicionar_compra.txtCredor.setText(item.text())
    msgInfo(f"Credor ( {item.text()}  ) adicionado ao campo") 
    
def form_lista_centro():
    lista_centro.show()

    dados = database.lista_centro()
    lista_centro.dgvDadosCentro.setRowCount(len(dados))
    lista_centro.dgvDadosCentro.setColumnCount(2)   
    lista_centro.dgvDadosCentro.setColumnWidth(1, 300)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            lista_centro.dgvDadosCentro.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    lista_centro.dgvDadosCentro.cellClicked.connect(recupera_dados_centro)

def listar_centro_por_nome():
    centro = lista_centro.txtPesquisar.text()
    dados = database.lista_centro_nome(centro) 

    lista_centro.dgvDadosCentro.setColumnCount(2)   
    lista_centro.dgvDadosCentro.setColumnWidth(1, 300)

    for l in range(0, len(dados)):
        for c in range(0, 2):
            lista_centro.dgvDadosCentro.setItem(l, c, QtWidgets.QTableWidgetItem(str(dados[l][c])))
    
    lista_centro.dgvDadosCentro.cellClicked.connect(recupera_dados_centro)

def recupera_dados_centro(row, column):
    item = lista_centro.dgvDadosCentro.item(row, column)  
    adicionar_compra.txtCentro.setText(item.text()) 
    msgInfo(f"Centro de custo ( {item.text()}  ) adicionado ao campo")      


def form_compra():
    adicionar_compra.show()

def form_add_cartao():
    adicionar_cartao.show()

def form_add_credor():
    adicionar_credor.show()

def form_add_centro():
    adicionar_centro.show()

def add_centro():
    nome = adicionar_centro.txtCentro.text()
    centro = Centro(None, nome)
    
    if nome != "":
        database.inserir_centro(centro)
        adicionar_centro.txtCentro.setText("")
        msgInfo("Centro de custo cadastrado com sucesso!!")
    else:
        msgWarning("Erro não foi possivel cadastrar!")

def close_centro():
    adicionar_centro.close()


def add_credor():
    nome = adicionar_credor.txtCredor.text()
    credor = Credor(None, nome)
    
    if nome != "":
        database.inserir_credor(credor)
        adicionar_credor.txtCredor.setText("")
        msgInfo("Credor cadastrado com sucesso!!")
    else:
        msgWarning("Erro não foi possivel cadastrar!")

def close_credor():
    adicionar_credor.close()

def add_cartao():
    numero_cartao = adicionar_cartao.txtNumero.text()
    cartao = Cartao(None, numero_cartao)

    if numero_cartao != "":
        database.inserir_cartao(cartao)
        adicionar_cartao.txtNumero.setText("")
        msgInfo("Lançamento feito com sucesso")
    else:
        msgWarning("Erro não foi possivel cadastrar!")

def close_cartao():
    adicionar_cartao.close()

def add_fatura():
    data = adicionar_compra.txtData.text()
    credor = adicionar_compra.txtCredor.text()
    documento = adicionar_compra.txtDoc.text()
    parcela = adicionar_compra.txtParcela.text()
    valor = adicionar_compra.txtValor.text()
    classificacao = adicionar_compra.txtClassificacao.text()
    centro = adicionar_compra.txtCentro.text()
    
    if data != "" and credor != "" and documento != "" and parcela != "" and valor != "" and classificacao != "" and centro != "":
        fatura = Fatura(None, data, credor, documento, parcela, valor, classificacao, centro)
        database.inserir_fatura(fatura)
        form_lista_fatura()
        atualiza_dash_board()
        msgInfo("Cadastrado com sucesso!!")
    else:
        msgWarning("Erro não foi possivel cadastrar!")



app = QtWidgets.QApplication([])

janela_principal = uic.loadUi("form_pricipal.ui")
lista_fatura = uic.loadUi("lista_fatura.ui")
lista_credor = uic.loadUi("lista_credor.ui")
lista_centro = uic.loadUi("lista_centro.ui")
adicionar_cartao = uic.loadUi("form_add_cartao.ui")
adicionar_credor = uic.loadUi("form_add_credor.ui")
adicionar_centro = uic.loadUi("form_add_centro.ui")
adicionar_compra = uic.loadUi("form_add_compra.ui")

lista_fatura.btnNovo.clicked.connect(form_compra)


janela_principal.btnAbriFatura.clicked.connect(form_lista_fatura)
janela_principal.btnAddCartao.clicked.connect(form_add_cartao)
janela_principal.btnAddCredor.clicked.connect(form_add_credor)
janela_principal.btnAddCentro.clicked.connect(form_add_centro)

adicionar_centro.btnSalvarCentro.clicked.connect(add_centro)
adicionar_centro.btnCancelar.clicked.connect(close_centro)

adicionar_credor.btnSalvarCredor.clicked.connect(add_credor)
adicionar_credor.btnCancelar.clicked.connect(close_credor)

adicionar_compra.btnLocCredor.clicked.connect(form_lista_credor)
adicionar_compra.btnLocCentro.clicked.connect(form_lista_centro)
adicionar_compra.btnSalvar.clicked.connect(add_fatura)

lista_credor.btnCadCredor.clicked.connect(form_add_credor)
lista_credor.btnExecutar.clicked.connect(listar_por_nome)


lista_centro.btnCadCentro.clicked.connect(form_add_centro)
lista_centro.btnExecutar.clicked.connect(listar_centro_por_nome)

adicionar_cartao.btnSalvarCartao.clicked.connect(add_cartao)
adicionar_cartao.btnCancelar.clicked.connect(close_cartao)


janela_principal.show()
def atualiza_dash_board():
    soma_oficina = database.lista_fatura_soma_oficina()
    soma_alpha = database.lista_fatura_soma_alpha()
    soma_adm = database.lista_fatura_soma_administrador()
    soma_maquinas_equip = database.lista_fatura_soma_maquinas()
    soma_jaiba = database.lista_fatura_soma_jaiba()

    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    janela_principal.lblSomaOficina.setText(str(locale.currency(soma_oficina[0][0])))
    janela_principal.lblSomaAlpha.setText(str(locale.currency(soma_alpha[0][0])))
    janela_principal.lblAdm.setText(str(locale.currency(soma_adm[0][0])))
    janela_principal.lblMaquinas.setText(str(locale.currency(soma_maquinas_equip[0][0])))
    janela_principal.lblJaiba.setText(str(locale.currency(soma_jaiba[0][0])))

    

atualiza_dash_board()

app.exec()