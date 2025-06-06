# Aluguel de Carros entre Pessoas Físicas

## Descrição

Este projeto tem como objetivo criar uma plataforma de aluguel de carros entre pessoas físicas. O **backend** foi desenvolvido utilizando **FastAPI** e o **frontend** será desenvolvido com **React Native**. O banco de dados utilizado é o **PostgreSQL**.

A ideia principal do projeto é permitir que usuários possam listar seus carros disponíveis para aluguel, enquanto outros usuários podem alugar esses veículos diretamente através da plataforma.

## Funcionalidades

- Rota de **Usuários** (CRUD)

## Tecnologias Utilizadas

- 🧩 **Backend**: FastAPI
- 📕 **Bibliotecas Backend**:
- **FastAPI**: Framework web para criar APIs com Python de maneira rápida e eficiente.
- **SQLAlchemy**: Biblioteca ORM para interagir com o banco de dados PostgreSQL.
- **Pydantic**: Validação de dados usando anotações de tipo Python.
- **Uvicorn**: Servidor ASGI de alto desempenho para servir a aplicação FastAPI.
- **Python-dotenv**: Para carregar variáveis de ambiente a partir de arquivos `.env`.
- **pydantic_settings**: Gerenciar e validar configurações e variáveis de ambiente de forma simples e segura.
- **pwdlib[argon2]**: criptografia.
- **pyjwt**.

- 🎲 **Banco de Dados**: PostgreSQL
- 🛥️ **Docker**: Para PostgreSQL e pgAdmin (gerenciamento do banco de dados)

## Como Rodar o Projeto
uvicorn app:app --reload --host 0.0.0.0 --port 8000

1. Clone o repositório:

   ```bash
   git clone https://github.com/rukasuleonhart/aluguel-carro.git
