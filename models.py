from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    matricula = Column(String(100))
    setor = Column(String(100))
    diretoria = Column(String(100))
    regiao = Column(String(100))
    nomeDaCapacitacao = Column(String(100))
    email = Column(String(100))
