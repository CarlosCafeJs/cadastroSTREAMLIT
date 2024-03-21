import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Apenas importa a Base, não é necessário importar Cliente

# Função para criar a tabela no banco de dados
def criar_tabela_clientes():
    try:
        # Criar engine para se conectar ao banco de dados
        engine = create_engine('mysql://seu_usuario:sua_senha@seu_host/seu_banco_de_dados')

        # Criar todas as tabelas definidas em Base
        Base.metadata.create_all(engine)

        st.success("Tabela 'clientes' criada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao criar tabela: {e}")

# Aplicativo Streamlit
def main():
    st.title("Criação de Tabela no Banco de Dados")

    # Botão para criar a tabela
    if st.button("Criar Tabela 'clientes'"):
        criar_tabela_clientes()

# Execução do aplicativo
if __name__ == "__main__":
    main()
