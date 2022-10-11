import requests

from config import settings
from fastapi import HTTPException


class ApiLoteriasRepository:
    @staticmethod
    def get_result(jogo: str, concurso: str = None):
        url = f"{settings.API_LOTERIAS_URL}/{jogo}"

        if concurso:
            url = url + f"/{concurso}"

        result = requests.get(url)
        if result.status_code == 404:
            raise HTTPException(status_code=400, detail=result.json()["message"])

        return result.json()
