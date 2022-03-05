from fastapi import APIRouter

from schemas.my_results import MyResultsIN
from service.sort_service import sort_game, save_game, check

sort_controller = APIRouter()


@sort_controller.get(
    ''
)
def sorting_number(game: str):
    result = sort_game(game)
    return result


@sort_controller.post(
    '/save'
)
def save_sorting_games(game: MyResultsIN):
    return save_game(game)


@sort_controller.get(
    '/check'
)
def check_results(game: int):
    return check(game)
