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


def get_all():
    result = postgres.get_all(Lotofacil)
    return result


def get_by_id(id: str):
    result = postgres.get_by_id(id, Lotofacil)
    return result


def number():
    results: List[Lotofacil] = get_all()
    quantity_1 = 0
    quantity_2 = 0
    quantity_3 = 0
    quantity_4 = 0
    quantity_5 = 0
    quantity_6 = 0
    quantity_7 = 0
    quantity_8 = 0
    quantity_9 = 0
    quantity_10 = 0
    quantity_11 = 0
    quantity_12 = 0
    quantity_13 = 0
    quantity_14 = 0
    quantity_15 = 0
    quantity_16 = 0
    quantity_17 = 0
    quantity_18 = 0
    quantity_19 = 0
    quantity_20 = 0
    quantity_21 = 0
    quantity_22 = 0
    quantity_23 = 0
    quantity_24 = 0
    quantity_25 = 0

    for x in results:
        if 1 in x.dezenas:
            quantity_1 += 1
        if 2 in x.dezenas:
            quantity_2 += 1
        if 3 in x.dezenas:
            quantity_3 += 1
        if 4 in x.dezenas:
            quantity_4 += 1
        if 5 in x.dezenas:
            quantity_5 += 1
        if 6 in x.dezenas:
            quantity_6 += 1
        if 7 in x.dezenas:
            quantity_7 += 1
        if 8 in x.dezenas:
            quantity_8 += 1
        if 9 in x.dezenas:
            quantity_9 += 1
        if 10 in x.dezenas:
            quantity_10 += 1
        if 11 in x.dezenas:
            quantity_11 += 1
        if 12 in x.dezenas:
            quantity_12 += 1
        if 13 in x.dezenas:
            quantity_13 += 1
        if 14 in x.dezenas:
            quantity_14 += 1
        if 15 in x.dezenas:
            quantity_15 += 1
        if 16 in x.dezenas:
            quantity_16 += 1
        if 17 in x.dezenas:
            quantity_17 += 1
        if 18 in x.dezenas:
            quantity_18 += 1
        if 19 in x.dezenas:
            quantity_19 += 1
        if 20 in x.dezenas:
            quantity_20 += 1
        if 21 in x.dezenas:
            quantity_21 += 1
        if 22 in x.dezenas:
            quantity_22 += 1
        if 23 in x.dezenas:
            quantity_23 += 1
        if 24 in x.dezenas:
            quantity_24 += 1
        if 25 in x.dezenas:
            quantity_25 += 1
