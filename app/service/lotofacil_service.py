import uuid
from datetime import datetime
from typing import List

from database import session
from repository.api_loterias_repository import ApiLoteriasRepository
from repository.postgres import PostgresRepository
from schemas import Lotofacil

postgres = PostgresRepository(session=session)

api_loterias = ApiLoteriasRepository()


def sync_lotofacil():
    last_contest = postgres.get_last_contest(Lotofacil)
    result = api_loterias.get_result(jogo="lotofacil", concurso="latest")

    if not last_contest:
        last_contest = 0

    if result.get("concurso") == last_contest:
        return

    diff = result.get("concurso") - last_contest

    if diff == result.get("concurso"):
        results = api_loterias.get_result(jogo="lotofacil")

        lotos = [Lotofacil(**result).dict(exclude_none=True) for result in results]

        create_all_lotofacil(lotos)
        return

    if diff == 1:
        loto = Lotofacil(**result)
        loto.data = datetime.strptime(result.get("data"), "%d/%m/%Y")

        create_lotofacil(loto)

    else:
        lotos = []
        for i in range(last_contest + 1, result.get("concurso") + 1, 1):
            result = api_loterias.get_result(jogo="lotofacil", concurso=str(i))

            loto = Lotofacil(**result).dict(exclude_none=True)
            lotos.append(loto)

        create_all_lotofacil(lotos)


def create_lotofacil(loto: Lotofacil):
    loto.id = uuid.uuid4()
    result = postgres.save(loto)
    return result


def create_all_lotofacil(loto: List[dict]):
    lotos = [Lotofacil(id=uuid.uuid4(), **x) for x in loto]
    postgres.save_all(lotos)
    return


def get_all(skip: int, limit: int):
    result = postgres.get_all(Lotofacil, skip, limit)
    return result


def get_by_id(id: str):
    result = postgres.get_by_id(id, Lotofacil)
    return result
