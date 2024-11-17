# Usando uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de dependências
COPY requirements.txt .

# Instalando dependências
RUN pip install -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Expondo a porta da API
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
