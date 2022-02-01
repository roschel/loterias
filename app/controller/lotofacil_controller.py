from fastapi import APIRouter, Response

from schemas import Lotofacil
from service.lotofacil_service import sync_lotofacil, create_lotofacil, get_all, get_by_id

loto_controller = APIRouter()


@loto_controller.get(
    ''
)
def find_all(skip: int = None, limit: int = 100):
    result = get_all(skip, limit)
    return result


@loto_controller.get(
    '/{id}'
)
def find_by_id(id: str):
    result = get_by_id(id)
    return result


@loto_controller.post(
    '/sync/all'
)
def sync_results():
    sync_lotofacil()
    return Response(None, status_code=204)


@loto_controller.post(
    ''
)
def post_result(lotofacil: Lotofacil):
    result = create_lotofacil(lotofacil)
    return result
