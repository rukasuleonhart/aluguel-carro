from fastapi import FastAPI
from routers import users, cars, auth, rentals
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sistema de Aluguel de Carros")

# add cors allowed origins
origins = [
    'http://192.168.3.51:8081'
]

# add middleware and specify cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(cars.router)
app.include_router(auth.router)
app.include_router(rentals.router)

@app.get("/")
def pagina_inicial():
    return "Bem vindo a página inicial!"
