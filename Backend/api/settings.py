from dotenv import load_dotenv
import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Definir o caminho correto para o arquivo .env considerando a estrutura de pastas
env_path = Path(__file__).resolve().parent.parent / '.env'  # Sobe uma pasta e encontra o .env
load_dotenv(dotenv_path=env_path)  # Carregando o .env na memória

# Verificando se as variáveis de ambiente estão sendo carregadas corretamente
print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("DPOSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    POSTGRES_DB: str

    @property
    def database_url(self):
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )

# Instância global
settings = Settings()

# Verificando a URL do banco de dados gerada
print("Database URL:", settings.database_url)
