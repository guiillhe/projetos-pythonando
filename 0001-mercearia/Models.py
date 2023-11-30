from datetime import datetime
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Vendas:
    def __init__(self, itensVendidos : Produtos, vendedor, comprador, quantidadeVendida, data=datetime.now()):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, telefone,email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, cpf, telefone, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, email, endereco)