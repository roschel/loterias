import os
from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    # API LOTERIAS
    API_LOTERIAS_URL: str = Field("https://loteriascaixa-api.herokuapp.com/api")

    # POSTGRES
    DB_USERNAME: str = Field("postgres", title="Usuário do banco de dados")
    DB_PASSWORD: str = Field("password", title="Senha")
    DB_HOST: str = Field("localhost", title="Host")
    DB_PORT: str = Field("5432", title="Porta")
    DB_DATABASE: str = Field("", title="Banco de dados")
    REPOSITORY_NAME: str = Field("postgresql")

    class Config:
        env_file = os.getenv("ENV_FILE")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
