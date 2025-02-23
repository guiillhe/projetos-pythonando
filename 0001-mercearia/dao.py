from Models import * 


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('001-categorias.txt', 'a') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines('\n')

    
    @classmethod
    def listar(cls):
        with open('001-categorias.txt', 'r') as arquivo:
            cls.categorias = arquivo.readlines()


            lista_categorias = []
            
            
            for categoria in cls.categorias:
                lista_categorias.append(Categoria(categoria.replace('\n', '')))


            return lista_categorias


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Vendas):
        with open('002-vendas.txt', 'a') as arquivo:
            arquivo.write(venda.itensVendidos.nome + ';' + str(venda.itensVendidos.preco) + ';' + venda.itensVendidos.categoria + ';' + venda.vendedor + ';' + venda.comprador + ';' + str(venda.quantidadeVendida) + ';' + str(venda.data))
            arquivo.writelines('\n')



    @classmethod
    def listar(cls):
        with open('002-vendas.txt', 'r') as arquivo:
            cls.vendas = arquivo.readlines()
            lista_vendas = []

            
            for venda in cls.vendas:
                venda.replace('\n', '')
                venda = venda.split(';')
                if len(venda) == 7:
                    lista_vendas.append(Vendas(Produtos(venda[0], venda[1], venda[2]), venda[3], venda[4], venda[5], venda[6]))
                else:
                    print(f"Erro: linha com venda incorretos - {venda}")
                
        
            return lista_vendas 
        

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('003-estoque.txt', 'a') as arquivo:
            arquivo.write(produto.nome + ';' + str(produto.preco) + ';' + produto.categoria + ';' + str(quantidade))
            arquivo.writelines('\n')
            

    @classmethod
    def listar(cls):
        with open('003-estoque.txt', 'r') as arquivo:
            cls.produtos = arquivo.readlines()
            lista_produtos = []
            for produto in cls.produtos:
                produto = produto.replace('\n', '')
                produto = produto.split(';')                
                lista_produtos.append(Estoque(Produtos(produto[0], produto[1], produto[2]), int(produto[3])))
            return lista_produtos
        

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor):
        with open('004-fornecedores.txt', 'a') as arquivo:
            arquivo.write(fornecedor.nome + ';' + fornecedor.cnpj + ';' + fornecedor.telefone + 
                          ';' + fornecedor.categoria)
            arquivo.writelines('\n')
    

    @classmethod
    def listar(cls):
        with open('004-fornecedores.txt', 'r') as arquivo:
            cls.fornecedores = arquivo.readlines()
            lista_fornecedores = []
            for fornecedor in cls.fornecedores:
                fornecedor = fornecedor.replace('\n', '')
                fornecedor = fornecedor.split(';')
                lista_fornecedores.append(Fornecedor(fornecedor[0], fornecedor[1], fornecedor[2], fornecedor[3]))
            return lista_fornecedores


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario):
        with open('005-funcionarios.txt', 'a') as arquivo:
            arquivo.write(funcionario.clt+';'+funcionario.nome + ';' + funcionario.cpf + ';' + funcionario.telefone + 
                          ';' + funcionario.email + ';' + funcionario.endereco )
            arquivo.writelines('\n')
    
    @classmethod
    def listar(cls):
        with open('005-funcionarios.txt', 'r') as arquivo:
            cls.funcionarios = arquivo.readlines()
            lista_funcionarios = []
            for funcionario in cls.funcionarios:
                funcionario = funcionario.replace('\n', '')
                funcionario = funcionario.split(';')
                lista_funcionarios.append(Funcionario(funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4], funcionario[5]))
            return lista_funcionarios
        
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa):
        with open('006-pessoas.txt', 'a') as arquivo:
            arquivo.write(pessoa.nome + ';' + pessoa.cpf + ';' + pessoa.telefone + 
                          ';'+pessoa.email+';' + pessoa.endereco)
            arquivo.writelines('\n')
    
    @classmethod
    def listar(cls):
        with open('006-pessoas.txt', 'r') as arquivo:
            cls.pessoas = arquivo.readlines()
            lista_pessoas = []
            for pessoa in cls.pessoas:
                pessoa = pessoa.replace('\n', '')
                pessoa = pessoa.split(';')
                lista_pessoas.append(Pessoa(pessoa[0], pessoa[1], pessoa[2], pessoa[3], pessoa[4]))
            return lista_pessoas
        

