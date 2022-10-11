from fastapi import APIRouter, Response, BackgroundTasks

from schemas import Jogo
from service.service import sync_jogo, get_all, get_by_id, create_jogo

loto_controller = APIRouter()


@loto_controller.get("/jogo/{jogo}")
def find_all(jogo: str, skip: int = None, limit: int = 100):
    result = get_all(skip=skip, limit=limit, jogo=jogo)
    return result


@loto_controller.get("/{id}")
def find_by_id(id: str):
    result = get_by_id(id)
    return result


@loto_controller.post("/sync/all/{jogo}")
def sync_results(background_tasks: BackgroundTasks, jogo: str):
    result = sync_jogo(jogo=jogo)
    return result


@loto_controller.post("")
def post_result(jogo: Jogo):
    result = create_jogo(jogo)
    return result
