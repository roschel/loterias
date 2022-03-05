from typing import List, Optional

from sqlmodel import Field, SQLModel, Column, ARRAY, INTEGER
from uuid import UUID


class MyResultsIN(SQLModel):
    numbers: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    concurso: int = Field(title="Número do concurso")
    name: str = Field("Lotofácil", title="Nome do concurso")


class MyResults(MyResultsIN, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    numbers: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    concurso: int = Field(title="Número do concurso")
    name: str = Field("Lotofácil", title="Nome do concurso")
    odd: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))
    pair: List[int] = Field(sa_column=Column(ARRAY(INTEGER)))
