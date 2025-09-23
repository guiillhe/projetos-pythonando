from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

conn = 'sqlite:///pythonando.db'


engine = create_engine(conn)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(200), nullable=False)


Base.metadata.create_all(engine)