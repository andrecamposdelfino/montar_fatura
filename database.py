import sqlite3
from modelo import Credor, Cartao, Fatura

# id, data, credor, documento, parcela, valor, classificacao, centro_custo

conexao = sqlite3.connect("cartao.db")
cursor = conexao.cursor()


def inserir_credor(credor):
    try:
        query = """
            INSERT INTO credor VALUES(:id, :nome)
        """
        cursor.execute(query, vars(credor))
        conexao.commit()
        print("Credor cadastrado com sucesso!!")

    except Exception as error:
        print(f"Error ao tentar cadastrar o centro : {error}")

fatura = Fatura(None, "16/09/2024", "Comercial dragão", "1022", 1, 250, "Produto de pouca durabilidade", "ETS - Administrador")



def inserir_fatura(fatura):
    try:
        query = """
            INSERT INTO fatura VALUES(:id, :data, :credor, :documento, :parcela, :valor, :classificacao, :centro_custo)
        """
        cursor.execute(query, vars(fatura))
        conexao.commit()
        print("Fatura cadastrada com sucesso!!")

    except Exception as error:
        print(f"Error ao tentar cadastrar a fatura : {error}")



def inserir_centro(centro):
    try:
        query = """
            INSERT INTO centro VALUES(:id, :nome)
        """
        cursor.execute(query, vars(centro))
        conexao.commit()
        print("Credor cadastrado com sucesso!!")


    except Exception as error:
        print(f"Error ao tentar cadastrar o centro : {error}")


def inserir_cartao(cartao):
    try:
        query = """
            INSERT INTO cartao VALUES(:id, :numero)
        """
        cursor.execute(query, vars(cartao))
        conexao.commit()
        print("Cartão cadastrado com sucesso!!")

    except Exception as error:
        print(f"Error ao tentar cadastrar o cartão : {error}")


def lista_centro():
    try:
        query = """
            SELECT * FROM centro
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar os credores : {error}")

def lista_fatura():
    try:
        query = """
            SELECT * FROM fatura
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")


def lista_fatura_soma_alpha():
    try:
        query = """
            SELECT sum(valor) FROM fatura WHERE  centro = "ETS - Alpha"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")




def lista_fatura_soma_oficina():
    try:
        query = """
            SELECT sum(valor) FROM fatura WHERE  centro = "ETS - Oficina"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")


def lista_fatura_soma_administrador():
    try:
        query = """
            SELECT sum(valor) FROM fatura WHERE  centro = "ETS - Administrador"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")

def lista_fatura_soma_maquinas():
    try:
        query = """
            SELECT sum(valor) FROM fatura WHERE  centro = "ETS - Maq e Equip"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")

def lista_fatura_soma_jaiba():
    try:
        query = """
            SELECT sum(valor) FROM fatura WHERE  centro = "ETS - Jaiba Loc"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar a fatura : {error}")


    
def lista_credor():
    try:
        query = """
            SELECT * FROM credor
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar os credores : {error}")


def lista_credor_nome(credor):
    try:
        query = f"""
            SELECT * FROM credor WHERE NOME LIKE "%{credor}%"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar os credores : {error}")

def lista_centro_nome(credor):
    try:
        query = f"""
            SELECT * FROM centro WHERE NOME LIKE "%{credor}%"
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(f"Error ao tentar listar os credores : {error}")



