# Use a imagem base do Python
FROM python:3.9

# Instale o MariaDB
RUN apt-get update && apt-get install -y mariadb-server

# Copie os arquivos necessários para o contêiner
COPY requirements.txt /
COPY database.py /
COPY models.py /
COPY app.py /
COPY pages/cadastro.py /pages/cadastro.py
COPY pages/dados.py /pages/dados.py

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale as dependências do Python
RUN pip install --no-cache-dir -r /requirements.txt

# Exponha a porta 8501 para o Streamlit
EXPOSE 8501

# Comando para executar o aplicativo Streamlit
CMD ["streamlit", "run", "app.py"]
