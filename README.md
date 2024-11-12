# Projeto APIs Independentes

Este projeto contém três APIs independentes desenvolvidas para diferentes propósitos. Cada API está conectada a um banco de dados específico e foi configurada para operar em um bloco de IP privado `10.10.10.0/24`, garantindo isolamento e segurança na rede.

## Estrutura do Projeto

- **API Clientes**: API responsável pelo gerenciamento dos clientes da empresa.
- **API Inventário**: API para controle e monitoramento dos itens em estoque.
- **API Relatórios**: API que gera relatórios com base nos dados de clientes e inventário.

## Tecnologias Utilizadas

- Python
- Django e Django REST Framework
- MySQL (para os bancos de dados)
- Docker (opcional, para containerização)
  
## Configuração do Projeto

1. Clone este repositório.
2. Instale as dependências para cada API:
   ```bash
   pip install -r requirements.txt
