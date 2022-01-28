import requests

from config import settings


class ApiLoteriasRepository:

    @staticmethod
    def get_result(jogo: str, concurso: str = None):
        url = f"{settings.API_LOTERIAS_URL}/{jogo}"

        if concurso:
            url = url + f"/{concurso}"

        result = requests.get(url)
        return result.json()
