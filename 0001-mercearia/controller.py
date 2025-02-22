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


    def relatorio_vendas(self):
        x = DaoVenda.listar()

        if len(x) == 0:
            print('Nenhuma venda cadastrada!')
            return
        else:
            produtos = []
            for i in x:
                nome_produto = i.itensVendidos.nome
                quantidade_vendida= i.quantidadeVendida
                tamanho = list(filter(lambda x: x['produto']== nome_produto, produtos))
                if len(tamanho) > 0:
                    produtos = list(map(lambda x: {'produto' : nome_produto, 'quantidade': int(x['quantidade']) + int(quantidade_vendida)} if (x['produto']== nome_produto) else(x), produtos))
                    
                else:
                   produtos.append({'produto' : nome_produto,'quantidade' : quantidade_vendida })
                   
            ranking = sorted(produtos, key=lambda  k: int(k['quantidade']), reverse=True)  
            print(f'='*10,'Produtos mais vendidos',f'='*10)    
            for produto in ranking:
                print(f"Produto: {produto['produto']} - Quantidade vendida: {produto['quantidade']}")
            print(f'='*44)


    def listar_venda(self, data_inicio, data_fim):
        vendas = DaoVenda.listar()
        data_inicio_1 = datetime.strptime(data_inicio, '%d/%m/%Y')
        data_fim_1 = datetime.strptime(data_fim, '%d/%m/%Y')

        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data[:10],'%Y-%m-%d')>= data_inicio_1 
                                          and datetime.strptime(x.data[:10],'%Y-%m-%d')<= data_fim_1 ,vendas))
        
        contador = 1
        valor_total = 0

        for venda in vendas_selecionadas:
            print(

f"""======== Venda {contador}=======
Nome produto: {venda.itensVendidos.nome}
Categoria   : {venda.itensVendidos.categoria}
Data        : {venda.data[:10].replace('-','/')}
Quantidade  : {venda.quantidadeVendida}
Cliente     : {venda.comprador}
Vendedor    : {venda.vendedor}
====================="""
                              
            )
            valor_total += int(venda.itensVendidos.preco) * int(venda.quantidadeVendida)
            contador +=1
        print(f"Valor total das vendas: R${float(valor_total):.2f}")
#batata;8;comida;15
a= ControllerVenda()
a.listar_venda("01/01/2023","01/01/2025")

# b = ControllerEstoque()

# b.listarProduto()