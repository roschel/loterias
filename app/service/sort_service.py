from math import gamma
import random
from time import gmtime
import uuid

from fastapi import HTTPException

from database import session
from repository.postgres import PostgresRepository
from schemas import Jogo
from schemas.my_results import MyResultsIN, MyResults

postgres = PostgresRepository(session=session)

values_per_game = {
    "lotofacil": {"game_sort": 15, "game_quantity": 25},
    "mega-sena": {"game_sort": 6, "game_quantity": 60},
    "quina": {"game_sort": 5, "game_quantity": 80},
    "lotomania": {"game_sort": 20, "game_quantity": 100},
    "timemania": {"game_sort": 7, "game_quantity": 80},
}


def get_odd_pair(numbers):
    pair = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pair.append(number)
        else:
            odd.append(number)

    result = dict(numbers=numbers, pair=pair, odd=odd)

    return result


def sort_logic(total_value: dict):
    numbers = []

    while len(numbers) != total_value["game_sort"]:
        number = random.randint(1, total_value["game_quantity"])
        if number == 100:
            number = 0
        if number not in numbers:
            numbers.append(number)

    numbers.sort()

    result = get_odd_pair(numbers=numbers)

    return result


def sort_game(game: str):

    return sort_logic(total_value=values_per_game[game])


def save_game(game: MyResultsIN):
    if len(game.numbers) < values_per_game[game.name]["game_sort"]:
        raise HTTPException(
            status_code=400,
            detail=f"O jogo {game.name} precisar ter pelo menos 15 números",
        )

    results_already_saved = postgres.get_by_game(game=game.concurso, model=MyResults)

    for saved in results_already_saved:
        if game.numbers == saved.numbers:
            raise HTTPException(status_code=409, detail="Jogo já existente")

    result = get_odd_pair(numbers=game.numbers)
    my_result = MyResults(
        id=uuid.uuid4(), **result, concurso=game.concurso, name=game.name
    )

    result = postgres.save(my_result)
    return result


def check(game: int):
    my_results = postgres.get_by_game(game, MyResults)
    game = postgres.get_by_game(game, Jogo)

    result = {
        str(i.numbers): 15 - len(set(game[0].dezenas) - set(i.numbers))
        for i in my_results
    }

    result.update({game[0].concurso: str(game[0].dezenas)})

    return result
