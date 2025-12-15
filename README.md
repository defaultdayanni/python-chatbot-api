# Python Chatbot API (Experimental)

Este repositório contém uma API REST desenvolvida em Python como **experimento técnico privado**, 
com finalidade **exclusivamente educacional**.

O projeto foi utilizado para estudo e prática de:
- desenvolvimento backend em Python
- integração com banco de dados relacional
- organização de código em camadas
- criação e consumo de APIs REST

Não se trata de um produto final nem de uma aplicação comercial.

---

## 🧪 Objetivo do Experimento

Explorar, de forma prática, conceitos de backend, tais como:
- arquitetura básica de APIs
- persistência de dados
- separação de responsabilidades
- testes manuais via Swagger

---

## 🛠 Tecnologias Utilizadas

- **Python 3.13**
- **FastAPI**
- **Uvicorn**
- **SQL Server Express**
- **pyodbc**
- **Pydantic**

---

## 📂 Organização do Projeto

- `app/api`  
  Define as rotas da API.

- `app/schemas`  
  Modelos de dados e validação com Pydantic.

- `app/repositories`  
  Camada de acesso a dados (Repository Pattern).

- `app/database`  
  Configuração e conexão com o banco de dados.

- `scripts`  
  Scripts auxiliares (ex: criação de tabelas).

---

## 🔌 Endpoints Disponíveis

### POST `/api/chat`

Recebe uma mensagem de texto e retorna uma resposta simples.

**Exemplo de request:**
```json
{
  "message": "Olá"
}
