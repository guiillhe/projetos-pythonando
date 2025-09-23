# Sistema de Login e Cadastro

Este é um sistema simples de login e cadastro desenvolvido em Python, utilizando criptografia SHA-256 para proteger as senhas dos usuários.

## 📋 Descrição do Projeto

O sistema permite que os usuários se cadastrem fornecendo nome, email e senha. As senhas são criptografadas usando o algoritmo SHA-256 antes de serem armazenadas no banco de dados. Após o cadastro, os usuários podem fazer login usando suas credenciais.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **SQLite**: Banco de dados leve para armazenamento das informações
- **SQLAlchemy**: ORM (Object-Relational Mapping) para manipulação do banco de dados
- **Hashlib**: Biblioteca padrão do Python para criptografia SHA-256

## 📦 Pacotes Necessários

Os seguintes pacotes Python são necessários para executar o projeto:

```
SQLAlchemy==2.0.43
greenlet==3.2.4
typing_extensions==4.15.0
```

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Criar um Ambiente Virtual (Recomendado)

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o Sistema

```bash
python view.py
```

## 📁 Estrutura do Projeto

```
├── controller.py     # Lógica de controle (validações, regras de negócio)
├── models.py         # Definição do modelo de dados e banco de dados
├── view.py           # Interface do usuário (console)
├── requirements.txt  # Dependências do projeto
├── .gitignore        # Arquivos e diretórios ignorados pelo Git
└── pythonando.db     # Banco de dados SQLite (gerado automaticamente)
```

## 🔐 Segurança

- **Criptografia de Senhas**: As senhas são criptografadas usando SHA-256 antes de serem armazenadas
- **Validação de Dados**: Validação de campos obrigatórios, formato de email e tamanho mínimo de senha
- **Prevenção de Duplicatas**: Não permite cadastro com email já existente

## ⚙️ Funcionalidades

1. **Cadastro de Usuário**:
   - Nome (obrigatório)
   - Email (obrigatório e único)
   - Senha (mínimo 6 caracteres)

2. **Login de Usuário**:
   - Autenticação com email e senha
   - Verificação de credenciais criptografadas

3. **Validações**:
   - Campos obrigatórios
   - Formato de email válido
   - Tamanho mínimo de senha
   - Prevenção de emails duplicados

## 🧪 Exemplo de Uso

Ao executar `python view.py`, você verá um menu interativo:

```
=== Sistema de Cadastro e Login ===
1. Cadastrar usuário
2. Fazer login
3. Sair
Escolha uma opção:
```

## 📝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona MinhaFeature'`)
4. Faça push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.


## 📞 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.