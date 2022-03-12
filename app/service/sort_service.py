import random
import uuid

from fastapi import HTTPException

from database import session
from repository.postgres import PostgresRepository
from schemas import Lotofacil
from schemas.my_results import MyResultsIN, MyResults

postgres = PostgresRepository(session=session)


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


def sort_logic(total_value: int):
    numbers = []

    while len(numbers) != total_value:
        number = random.randint(1, 25)
        if number not in numbers:
            numbers.append(number)

    numbers.sort()

    result = get_odd_pair(numbers=numbers)

    return result


def sort_game(game: str):
    if game == 'lotofacil':
        total_value = 15
        return sort_logic(total_value=total_value)


def save_game(game: MyResultsIN):
    if game.name.lower() == 'lotofácil':
        if len(game.numbers) < 15:
            raise ValueError(f"O jogo {game.name} precisar ter pelo menos 15 números")

    results_already_saved = postgres.get_by_game(game=game.concurso, model=MyResults)

    for saved in results_already_saved:
        if game.numbers == saved.numbers:
            raise HTTPException(status_code=409, detail="Jogo já existente")

    result = get_odd_pair(numbers=game.numbers)
    my_result = MyResults(id=uuid.uuid4(), **result, concurso=game.concurso, name=game.name)

    result = postgres.save(my_result)
    return result


def check(game: int):
    my_results = postgres.get_by_game(game, MyResults)
    game = postgres.get_by_game(game, Lotofacil)

    result = {
        str(i.numbers): 15 - len(set(game[0].dezenas) - set(i.numbers)) for i in my_results
    }

    result.update({game[0].concurso: str(game[0].dezenas)})

    return result
