import os
from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    # API LOTERIAS
    API_LOTERIAS_URL: str

    # POSTGRES
    DB_USERNAME: str = Field("", title="Usuário do banco de dados")
    DB_PASSWORD: str = Field("", title="Senha")
    DB_HOST: str = Field("", title="Host")
    DB_PORT: str = Field("", title="Porta")
    DB_DATABASE: str = Field("", title="Banco de dados")
    REPOSITORY_NAME: str

    class Config:
        env_file = os.getenv('ENV_FILE')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
