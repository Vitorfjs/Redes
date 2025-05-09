# Usando uma imagem base do Python
FROM python:3.10-slim

# Instalando dependências do sistema necessárias para compilar mariadb
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    mariadb-client \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Definindo o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt
COPY requirements.txt /app/

# Instalando as dependências do python
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . /app/

# Expondo a porta da API
EXPOSE 8002

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

