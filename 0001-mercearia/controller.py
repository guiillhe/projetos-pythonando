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
            #TODO: colocar sem categoria no estoque.    
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
            #TODO:  ALTERAR TAMBEM DO ESTOQUE
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
    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        x = DaoEstoque.listar()
        temp =[]

        est = list(filter(lambda x: x.produto.nome == nome_produto, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome_produto:
                    if x[i].quantidade <= quantidade_vendida:
                        print('Quantidade indisponível!')
                        return 2
                    else:
                        x[i].quantidade -= quantidade_vendida
                        venda = Vendas(x[i].produto, vendedor, comprador, quantidade_vendida, datetime.now())

                        valor_venda = int(quantidade_vendida) * int(x[i].produto.preco)
                        DaoVenda.salvar(venda)
                        print(valor_venda)
                        print('Venda cadastrada com sucesso!')
                        temp.append(x[i])
                        for i in temp:
                            if i.quantidade == 0:
                                x.remove(i)
                        with open('003-estoque.txt', 'w') as arquivo:
                            for i in x:
                                arquivo.write(i.produto.nome + ';' + str(i.produto.preco) + ';' + i.produto.categoria + ';' + str(i.quantidade))
                                arquivo.write('\n')
                        return 3, valor_venda
        else:
            print('Produto não encontrado!')
            return 1

    def listar_venda(self):
        x = DaoVenda.listar()

        if len(x) == 0:
            print('Nenhuma venda cadastrada!')
            return
        else:
            produtos = []
            for i in x:
                if i.itensVendidos.nome not in produtos:
                    produtos.append(i.itensVendidos.nome)
                else:
                    produtos = list(map(lambda x: x.itensVendidos.nome, x))
            for i in produtos:
                print(f'Produto: {i} - Quantidade vendida: {produtos.count(i)}')


#batata;8;comida;15
a= ControllerVenda()
a.cadastrar_venda('batata', 'jao', 'zá', 2)
b = ControllerEstoque()

b.listarProduto()