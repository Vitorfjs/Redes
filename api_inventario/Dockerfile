# Usando uma imagem oficial do Python
FROM python:3.10-slim

# Instalar dependências para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie todos os arquivos da API para o contêiner
COPY . /app/

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta para a API
EXPOSE 8001

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
