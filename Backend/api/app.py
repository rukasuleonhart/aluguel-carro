from fastapi import FastAPI
from routers import users

app = FastAPI(title="Sistema de Aluguel de Carros")

app.include_router(users.router)

@app.route("/")
def pagina_inicial():
    return "Bem vindo a página inicial!"
