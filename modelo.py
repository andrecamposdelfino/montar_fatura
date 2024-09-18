class Fatura:
    def __init__(self, id, data, credor, documento, parcela, valor, classificacao, centro_custo):
        self.id = id
        self.data = data
        self.credor = credor
        self.documento = documento
        self.parcela = parcela
        self.valor = valor
        self.classificacao = classificacao
        self.centro_custo = centro_custo


class Cartao:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero

class Centro:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Credor:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
       
