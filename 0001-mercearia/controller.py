from Models import Categoria, Produtos, Estoque, Vendas, Fornecedor, Pessoa, Funcionario
from dao import DaoCategoria, DaoEstoque, DaoVenda, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategotria(self, novaCategoria):
        existe = False
        x = DaoCategoria.listar()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:           
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já cadastrada!')
    
    def removerCategoria(self, categoria):
        x = DaoCategoria.listar()
        cat = list(filter(lambda x: x.categoria == categoria, x))
        if len(cat) > 0:
            for i in range(len(x)):
                if x[i].categoria == categoria:
                    x.pop(i)
                    break
            with open('001-categorias.txt', 'w') as arquivo:
                for i in x:
                    arquivo.write(i.categoria)
                    arquivo.write('\n')
            print('Categoria removida com sucesso!')
        else:
            print('Categoria não encontrada!')
    
    def alterarCategoria(self, categoria, novaCategoria):
        x = DaoCategoria.listar()
        cat = list(filter(lambda x: x.categoria == categoria, x))
        nova = list(filter(lambda x: x.categoria == novaCategoria, x))
        if len(nova) > 0:
            print(f'Categoria {novaCategoria} já cadastrada, favor escolher outro nome de categoria!')
            return
        if len(cat) > 0:
            
            for i in range(len(x)):
                if x[i].categoria == categoria:
                    x[i].categoria = novaCategoria
                    break
            with open('001-categorias.txt', 'w') as arquivo:
                for i in x:
                    arquivo.write(i.categoria)
                    arquivo.write('\n')
            print('Categoria alterada com sucesso!')
        else:
            print('Categoria não encontrada!')

    def listarCategoria(self):
        x = DaoCategoria.listar()

        if len(x) == 0:
            print('Nenhuma categoria cadastrada!')
            return
        else:
            for i in x:
                print(f'Categoria: {i.categoria}')


class  ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoCategoria.listar()
        y = DaoEstoque.listar()

        cat = list(filter(lambda x: x.categoria == categoria, x))
        est = list(filter(lambda x: x.produto.nome == nome, y))
        if len(cat) == 0:
            print('Categoria não encontrada!')
            return
        else:
            if len(est) > 0:
                print('Produto já cadastrado!')
                return
            else:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')


    def excluirProduto(self, nome):
        x = DaoEstoque.listar()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:            
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    x.pop(i)
                    break
            with open('003-estoque.txt', 'w') as arquivo:
                for i in x:
                    arquivo.write(i.produto.nome + ';' + str(i.produto.preco) + ';' + i.produto.categoria + ';' + str(i.quantidade))
                    arquivo.write('\n')
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado!')
    
    def alterarProduto(self, nome, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.listar()
        y = DaoCategoria.listar()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        cat = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(cat) == 0:
            print('Categoria não encontrada!')
            return
        else:
            if len(est) > 0:
                for i in range(len(x)):
                    if x[i].produto.nome == nome:
                        x[i].produto.nome = novoNome
                        x[i].produto.preco = novoPreco
                        x[i].produto.categoria = novaCategoria
                        x[i].quantidade = novaQuantidade
                        break
                with open('003-estoque.txt', 'w') as arquivo:
                    for i in x:
                        arquivo.write(i.produto.nome + ';' + str(i.produto.preco) + ';' + i.produto.categoria + ';' + str(i.quantidade))
                        arquivo.write('\n')
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado!')
        

    def listarProduto(self):
        x = DaoEstoque.listar()

        if len(x) == 0:
            print('Nenhuma categoria cadastrada!')
            return
        else:
            for i in x:
                print(f'Produto: {i.produto.nome} - Preço: {i.produto.preco} - Categoria: {i.produto.categoria} - Quantidade: {i.quantidade}')


class ControllerVenda:
    pass

a = ControllerEstoque()
a.listarProduto()