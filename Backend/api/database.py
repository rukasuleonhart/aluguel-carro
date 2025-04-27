from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings

# Conectando-se ao banco de dados
engine = create_engine(settings.database_url) 

# Criando uma sessão ao banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# função para ser injetada nos endpoints
def get_db():
    db = SessionLocal() # abrindo sessão
    try:
        yield db # entregando sessão
    finally:
        db.close() # fechando sessão