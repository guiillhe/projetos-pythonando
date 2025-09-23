import controller
def menu():
    print("\n=== Sistema de Cadastro e Login ===")
    print("1. Cadastrar usuário")
    print("2. Fazer login")
    print("3. Sair")
    return input("Escolha uma opção: ")

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    
    try:
        
        usuario = controller.ControllerCadastro.create(nome, email, senha)
        print(f"\nUsuário cadastrado com sucesso!")
    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def fazer_login():
    print("\n=== Login ===")
    email = input("Email: ")
    senha = input("Senha: ")
    
    try:        
        mensagem = controller.ControllerLogin.login(email, senha)
        print(f"\n{mensagem}")
    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

def main():
    while True:
        opcao = menu()
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            fazer_login()
        elif opcao == '3':
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()