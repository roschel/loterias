from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import validator
from sqlmodel import Field, SQLModel, Column, ARRAY, INTEGER


class Jogo(SQLModel, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    name: str = Field(None, title="Nome do concurso")
    data: datetime = Field(title="Data e hora do concurso")
    concurso: int = Field(title="Número do concurso")
    dezenas: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))

    class Config:
        arbitrary_types_allowed = True

    @validator("data", pre=True)
    def check_data(cls, v):
        if type(v) == str:
            return datetime.strptime(v, "%d/%m/%Y")
        return v
