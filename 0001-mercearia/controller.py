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

    
    def remover_categoria(self, categoria_remover):
        x = DaoCategoria.listar()
        cat = list(filter(lambda x: x.categoria == categoria_remover, x))
        #a_estoque =''
        if len(cat) > 0:
            for i in range(len(x)):
                if x[i].categoria == categoria_remover:
                    x.pop(i)
                    break            
            

            with open('001-categorias.txt', 'w') as arquivo:
                for i in x:
                    arquivo.write(i.categoria)
                    arquivo.write('\n')
            print('Categoria removida com sucesso!')
        else:
            print('Categoria não encontrada!')
        
        estoque = DaoEstoque.listar()
        a_estoque = list(
            map(
                lambda x: Estoque(Produtos(x.produto.nome,x.produto.preco,'sem_categoria'),x.quantidade)if(x.produto.categoria == categoria_remover) else (x), 
                estoque
                )
            )
        
        with open('003-estoque.txt','w') as arquivo:
            for produto in a_estoque:
                arquivo.writelines(f'{produto.produto.nome};{produto.produto.preco};{produto.produto.categoria};{produto.quantidade}\n')



                

    def alterar_categoria(self, categoria, novaCategoria):
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
            estoque = DaoEstoque.listar()
            a_estoque = list(
                map(
                    lambda x: Estoque(Produtos(x.produto.nome,x.produto.preco,novaCategoria),x.quantidade)if(x.produto.categoria == categoria) else (x), 
                    estoque
                    )
                )
            
            with open('003-estoque.txt','w') as arquivo:
                for produto in a_estoque:
                    arquivo.writelines(f'{produto.produto.nome};{produto.produto.preco};{produto.produto.categoria};{produto.quantidade}\n')

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


class ControllerFornecedor:
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.listar()
        lista_cnpj = list(filter(lambda x: x.cnpj ==cnpj, x))
        lista_telefone = list(filter(lambda x: x.telefone ==telefone, x))

        if len(lista_cnpj) > 0:
            print('CNPJ já cadastrado!!!')
        elif len(lista_telefone) > 0:
            print('Já existe um fornecedor com o mesmo numero de telefone!!!')
        else:
            if len(cnpj) < 14 or len(cnpj) >14:
                print('CNPJ inválido, favor verificar')
            elif len(telefone) != 11:
                print("Numero de telefone inválido")
            else:
                DaoFornecedor.salvar(Fornecedor(nome,cnpj,telefone,categoria))
                print("Fornecedor salvo com sucesso")
    

    def alterar_fornecedor(self, cnpj_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        dao_fornecedores = DaoFornecedor.listar()
        
        fornecedores = list(filter(lambda x: x.cnpj == cnpj_alterar, dao_fornecedores))

        if len(fornecedores) == 0:
            print('Fornecedor não encontrado, favor verificar')
            
        else:         
            fornecedores = list(filter(lambda y: y.cnpj.strip() == novo_cnpj.strip(), dao_fornecedores))
            
            if len(fornecedores) == 0:
                dao_fornecedores = list(map(lambda y: Fornecedor(novo_nome, novo_cnpj, novo_telefone, nova_categoria)if y.cnpj == cnpj_alterar else y, dao_fornecedores))
                with open('004-fornecedores.txt','w') as arq:
                    for fornecedor in dao_fornecedores:
                        arq.writelines(f"{fornecedor.nome};{fornecedor.cnpj};{fornecedor.telefone};{fornecedor.categoria}\n")
                    print('Fornecedor alterado com sucesso')
            else:
                print('Já existe um fornecedor com o cnpj que voce deseja usar')
    

    def remover_fornecedor(self, cnpj_excluir):
        dao_fornecedor = DaoFornecedor.listar()

        lista_fornecedores = list(filter(lambda x: x.cnpj == cnpj_excluir, dao_fornecedor))
        
        if len(lista_fornecedores) > 0:
            for indice in range(len(dao_fornecedor)):
                
                if dao_fornecedor[indice].cnpj == cnpj_excluir:
                    del dao_fornecedor[indice]
                    break
                    
            with open('004-fornecedores.txt','w') as arq:
                for fornecedor in dao_fornecedor:
                    print(fornecedor)
                    arq.writelines(f"{fornecedor.nome};{fornecedor.cnpj};{fornecedor.telefone};{fornecedor.categoria}\n")
                print('Fornecedor removido com sucesso') 
        else: 
            print("O CNPJ do fornecedor nao foi localizado!!!")


    def listar_fornecedor(self):
        lista = DaoFornecedor.listar()
        print(f"======== Lista Fornecedores ========")
        for indice, fornecedor in enumerate(lista):
            print(f'== Nome     : {fornecedor.nome} ==')
            print(f'== CNPJ     : {fornecedor.cnpj} ==')
            print(f'== Telefone : {fornecedor.telefone} ==')
            print(f'== Categoria: {fornecedor.categoria} ==')
        print(f"==============================")


class ControllerCliente:
    def cadastrar_cliente(self, nome, cpf, telefone,email, endereco):
        x = DaoPessoa.listar()
        lista_cpf = list(filter(lambda x: x.cpf ==cpf, x))
        lista_telefone = list(filter(lambda x: x.telefone ==telefone, x))

        if len(lista_cpf) > 0:
            print('CPF já cadastrado!!!')
        elif len(lista_telefone) > 0:
            print('Já existe um cliente com o mesmo numero de telefone!!!')
        else:
            if len(cpf) < 11 or len(cpf) >11:
                print('CPF inválido, favor verificar')
            elif len(telefone) != 11:
                print("Numero de telefone inválido")
            else:
                DaoPessoa.salvar(Pessoa(nome,cpf,telefone,email, endereco))
                print("Cliente salvo com sucesso")
    

    def alterar_cliente(self, cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco):
        dao_pessoas = DaoPessoa.listar()
        
        pessoas = list(filter(lambda x: x.cpf == cpf_alterar, dao_pessoas))

        if len(pessoas) == 0:
            print('Cliente não encontrado, favor verificar')
            
        else:         
            pessoas = list(filter(lambda y: y.cpf.strip() == novo_cpf.strip(), dao_pessoas))
            
            if len(pessoas) == 0:
                pessoas = list(map(lambda y: Pessoa(novo_nome, novo_cpf, novo_telefone, novo_email,novo_endereco)if y.cpf == cpf_alterar else y, dao_pessoas))
                with open('006-pessoas.txt','w') as arq:
                    for pessoa in pessoas:
                        arq.writelines(f"{pessoa.nome};{pessoa.cpf};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
                    print('Cliente alterado com sucesso')
            else:
                print('Já existe um Cliente com o cpf que voce deseja usar')
    

    def remover_cliente(self, cpf_excluir):
        dao_clientes = DaoPessoa.listar()

        lista_clientes = list(filter(lambda x: x.cpf == cpf_excluir, dao_clientes))
        
        if len(lista_clientes) > 0:
            for indice in range(len(dao_clientes)):
                
                if dao_clientes[indice].cpf == cpf_excluir:
                    del dao_clientes[indice]
                    break
                    
            with open('006-pessoas.txt','w') as arq:
                for cliente in dao_clientes:
                    arq.writelines(f"{cliente.nome};{cliente.cpf};{cliente.telefone};{cliente.email};{cliente.endereco}\n")
                print('Cliente removido com sucesso') 
        else: 
            print("O CPF  nao foi localizado!!!")


    def listar_clientes(self):
        lista = DaoPessoa.listar()
        print(f"======== Lista Clientes ========")
        for indice, cliente in enumerate(lista):
            print(f'== Nome     : {cliente.nome} ==')
            print(f'== CNPJ     : {cliente.cpf} ==')
            print(f'== Telefone : {cliente.telefone} ==')
            print(f'== Email: {cliente.email} ==')
            print(f'== endereco: {cliente.endereco} ==')
        print(f"==============================")

class ControllerFuncionario:
    def cadastrar_funcionario(self,clt, nome, cpf, telefone,email, endereco):
        lista_funcionarios = DaoFuncionario.listar()
        lista_cpf = list(filter(lambda x: x.cpf ==cpf, lista_funcionarios))
        lista_telefone = list(filter(lambda x: x.telefone ==telefone, lista_funcionarios))
        lista_clt = list(filter(lambda x: x.telefone ==telefone,lista_funcionarios ))

        if len(lista_cpf) > 0:
            print('CPF já cadastrado!!!')
        elif len(lista_telefone) > 0:
            print('Já existe um colaborador com o mesmo numero de telefone!!!')
        elif len(lista_clt) > 0:
            print('CLT já cadastrado!!!')
    
        else:
            if len(cpf) < 11 or len(cpf) >11:
                print('CPF inválido, favor verificar')
            elif len(telefone) != 11:
                print("Numero de telefone inválido")
            else:
                DaoFuncionario.salvar(Funcionario(clt,nome,cpf,telefone,email, endereco))
                print("Colaborador salvo com sucesso")
    

    def alterar_colaborador(self, cpf_alterar, novo_clt, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco):
        lista_funcionarios = DaoFuncionario.listar()
        
        pessoas = list(filter(lambda x: x.cpf == cpf_alterar, lista_funcionarios))
        colaboradores = list(filter(lambda y: y.clt.strip() == novo_clt.strip(), lista_funcionarios))
        if len(pessoas) == 0:
            print('Colaborador não encontrado, favor verificar')
        elif len(colaboradores) != 0:
            print('Ja existe um colaborador com o codigo clt informado') 
        else:         
            colaboradores = list(filter(lambda y: y.cpf.strip() == novo_cpf.strip(), lista_funcionarios))
            
            if len(colaboradores) == 0:
                colaboradores = list(map(lambda y: Funcionario(novo_clt, novo_nome, novo_cpf, novo_telefone, novo_email,novo_endereco)if y.cpf == cpf_alterar else y, lista_funcionarios))
                with open('005-funcionarios.txt','w') as arq:
                    for colaborador in colaboradores:
                        arq.writelines(f"{colaborador.clt};{colaborador.nome};{colaborador.cpf};{colaborador.telefone};{colaborador.email};{colaborador.endereco}\n")
                    print('Colaborador alterado com sucesso')
            else:
                print('Já existe um Colaborador com o cpf que voce deseja usar')
    

    def remover_colaborador(self, cpf_excluir):
        dao_funcionarios = DaoFuncionario.listar()

        lista_clientes = list(filter(lambda x: x.cpf == cpf_excluir, dao_funcionarios))
        
        if len(lista_clientes) > 0:
            for indice in range(len(dao_funcionarios)):
                
                if dao_funcionarios[indice].cpf == cpf_excluir:
                    del dao_funcionarios[indice]
                    break
                    
            with open('005-funcionarios.txt','w') as arq:
                for funcionario in dao_funcionarios:
                    arq.writelines(f"{funcionario.clt};{funcionario.nome};{funcionario.cpf};{funcionario.telefone};{funcionario.email};{funcionario.endereco}\n")
                print('Colaborador removido com sucesso') 
        else: 
            print("O CPF  nao foi localizado!!!")


    def listar_colaboradores(self):
        lista = DaoFuncionario.listar()
        print(f"======== Lista Funcionarios ========")
        for indice, funcionario in enumerate(lista):
            print(f'funcionario {indice+1}')
            print(f'== CLT     : {funcionario.clt} ==')
            print(f'== Nome     : {funcionario.nome} ==')
            print(f'== CNPJ     : {funcionario.cpf} ==')
            print(f'== Telefone : {funcionario.telefone} ==')
            print(f'== Email: {funcionario.email} ==')
            print(f'== endereco: {funcionario.endereco} ==')
        print(f"==============================")


        
#batata;8;comida;15
a= ControllerCategoria()
a.alterar_categoria('Bebida','bebida')
# b = ControllerEstoque()

# b.listarProduto()