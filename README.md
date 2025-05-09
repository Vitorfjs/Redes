# 🚀 Projeto APIs Independentes com Docker e Nginx Reverse‑Proxy

Este repositório orquestra três micro‑serviços REST independentes, cada um em seu próprio container Docker, com bancos de dados MariaDB isolados, phpMyAdmin para administração, containers de backup e um Nginx funcionando como proxy reverso. Tudo isso em redes Docker privadas (10.10.10.0/24) para garantir segurança, isolamento e escalabilidade.

---

## 📂 Estrutura do Repositório

| Caminho              | Descrição                                           |
| -------------------- | --------------------------------------------------- |
| `api-clientes/`      | Código da API Clientes (Django com Templates)       |
| `api-inventario/`    | Código da API Inventário (Django REST)              |
| `api-relatorios/`    | Código da API Relatórios (Django REST)              |
| `nginx/nginx.conf`   | Configuração do Nginx reverse‑proxy                 |
| `docker-compose.yml` | Orquestra todos os containers e redes               |
| `requirements.txt`   | Dependências necessárias para o projeto             |
| `wait-for-it.sh`     | Script shell para correta inicialização dos Dockers |
| `README.md`          | Documentação e instruções de uso                    |

## 🛠 Tecnologias

- **Linguagem & Framework**: Python, Django, Django REST Framework  
- **Banco de Dados**: MariaDB (cada API com seu próprio schema)  
- **Admin DB**: phpMyAdmin  
- **Containerização**: Docker & Docker Compose  
- **Proxy Reverso**: Nginx  
- **Rede Privada Docker**: 10.10.10.0/24  
  
## 🚀 Como Executar

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/Vitorfjs/Redes
   ```
2. 
