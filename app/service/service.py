import uuid
from datetime import datetime
from typing import List

from database import session
from repository.api_loterias_repository import ApiLoteriasRepository
from repository.postgres import PostgresRepository
from schemas import Jogo

postgres = PostgresRepository(session=session)

api_loterias = ApiLoteriasRepository()


def sync_jogo(jogo: str):
    last_contest = postgres.get_last_contest(Jogo, jogo)
    result = api_loterias.get_result(jogo=jogo, concurso="latest")

    if not last_contest:
        last_contest = 0

    if result.get("concurso") == last_contest:
        return

    diff = result.get("concurso") - last_contest

    if diff == result.get("concurso"):
        results = api_loterias.get_result(jogo=jogo)

        lotos = [
            Jogo(**result, name=jogo).dict(exclude_none=True) for result in results
        ]

        create_all(lotos)
        return

    if diff == 1:
        loto = Jogo(**result, name=jogo)
        loto.data = datetime.strptime(result.get("data"), "%d/%m/%Y")

        create_jogo(loto)

    else:
        lotos = []
        for i in range(last_contest + 1, result.get("concurso") + 1, 1):
            result = api_loterias.get_result(jogo=jogo, concurso=str(i))

            loto = Jogo(**result, name=jogo).dict(exclude_none=True)
            lotos.append(loto)

        create_all(lotos)


def create_jogo(jogo: Jogo):
    jogo.id = uuid.uuid4()
    result = postgres.save(jogo)
    return result


def create_all(loto: List[dict]):
    jogos = [Jogo(id=uuid.uuid4(), **x) for x in loto]
    postgres.save_all(jogos)
    return


def get_all(skip: int, limit: int, jogo):
    result = postgres.get_all(Jogo, skip, limit, jogo)
    return result


def get_by_id(id: str):
    result = postgres.get_by_id(id, Jogo)
    return result
