from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente

# Função para adicionar um cliente ao banco de dados
def adicionar_cliente(nome, matricula, setor, diretoria, regiao, nome_da_capacitacao, email):
    try:
        # Criar engine para se conectar ao banco de dados
        engine = create_engine('mysql://admin:Ckarlos36/database-1.cluster-c5wag6so2stq.us-east-2.rds.amazonaws.com')

        # Criar uma sessão
        Session = sessionmaker(bind=engine)
        session = Session()

        # Criar um novo cliente
        novo_cliente = Cliente(nome=nome, matricula=matricula, setor=setor, diretoria=diretoria, regiao=regiao, nomeDaCapacitacao=nome_da_capacitacao, email=email)

        # Adicionar o cliente à sessão
        session.add(novo_cliente)

        # Commit para salvar no banco de dados
        session.commit()

        session.close()

    except Exception as e:
        print(f"Erro ao adicionar cliente: {e}")
