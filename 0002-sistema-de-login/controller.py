from models import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib
engine = create_engine('sqlite:///pythonando.db')

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerCadastro():
    @classmethod
    def valida_dados(cls, nome, email,senha):
        if not nome or not email or not senha:
            raise ValueError("Nome, email e senha são obrigatórios.")
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido.")

        return True
    @classmethod
    def create(cls, nome, email, senha):
        if cls.valida_dados(nome, email, senha):
            session = create_session()
            validar_email = session.query(Pessoa).filter_by(email=email).all()
            if len(validar_email) > 0:
                raise ValueError("Email já cadastrado.")

            try:
                senha= hashlib.sha256(senha.encode()).hexdigest()

                pessoa = Pessoa(nome=nome, email=email, senha=senha)
                session.add(pessoa)
                session.commit()
                session.close()
                #print("Usuário cadastrado com sucesso.")
                return pessoa
            except Exception as ex:
                raise f'Falha ao Cadastrar Usuário: {ex}.'

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = create_session()
        try:
            pessoa = session.query(Pessoa).filter_by(email=email).first()
            if not pessoa or pessoa.senha != hashlib.sha256(senha.encode()).hexdigest():
                raise ValueError("Email ou senha inválidos.")
            return f'Bem vindo ao sistema {pessoa.nome}'
        finally:
            session.close()
#print(ControllerCadastro.create('Caio','123@hotmail.com','123456789'))

#print(ControllerLogin.login('levanto@hotmail.com', '123456789'))