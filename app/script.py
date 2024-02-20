import matplotlib.pyplot as plt
from database import session
from repository.postgres import PostgresRepository
from schemas import Jogo

postgres = PostgresRepository(session=session)


def numbers_per_game(jogo, skip=None, limit=None):
    msg = 'Todos os jogos'

    if limit:
        msg = f'Ultimos {limit} jogos'

    final_result = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
        23: 0,
        24: 0,
        25: 0,
    }
    x=[]
    heights=[]
    multiplier = 0
    width = 0.25

    fig, ax = plt.subplots(figsize=(17, 8))

    resultados = postgres.get_all(Jogo, skip, limit, jogo)

    for resultado in resultados:
        resultado_dict = resultado.dict()
        for number in resultado_dict['dezenas']:
            final_result[number] += 1

    for x_coord, y_coord in final_result.items():
        x.append(x_coord)
        heights.append(y_coord)

        offset = width + multiplier
        rects = ax.bar(x_coord, y_coord, label=y_coord)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    ax.set_title(msg)
    plt.ylim(min(heights), max(heights)+5)
    plt.xticks(x)
    plt.show()


if __name__ == '__main__':
    numbers_per_game(jogo="lotofacil", limit=20)
