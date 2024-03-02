import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from database import session
from repository.postgres import PostgresRepository
from schemas import Jogo

postgres = PostgresRepository(session=session)


def _grafico_barras_total_numeros_por_jogos(msg, numbers):
    x = []
    heights = []

    fig, ax = plt.subplots(layout='constrained')
    for x_coord, y_coord in numbers.items():
        x.append(x_coord)
        heights.append(y_coord)
        rects = ax.bar(x_coord, y_coord, label=y_coord)
        ax.bar_label(rects, padding=3)
    ax.set_title('Dezenas por jogos - ' + msg)
    plt.ylim(min(heights), max(heights) + 5)
    plt.xticks(x)
    plt.show()


def _grafico_total_de_pares_e_impares_por_jogo(msg, numbers):
    fig, ax = plt.subplots(layout='constrained')
    df = pd.DataFrame(numbers)
    subjects = ['par', 'impar']

    indx = np.arange(len(numbers.keys()))
    pares = list(df.T[0])
    impares = list(df.T[1])

    bar_width = 0.35
    par_bar = ax.bar(indx - bar_width/2, pares, bar_width, label="par")
    ax.bar_label(par_bar, label_type='center')
    impar_bar = ax.bar(indx + bar_width/2, impares, bar_width, label="impar")
    ax.bar_label(impar_bar, label_type='center')

    ax.legend(loc='upper right')
    
    ax.set_xticks(indx + bar_width, list(numbers.keys()))
    ax.set_title('Pares e Impares dos ' + msg)
    plt.show()


def _define_msg(limit=None):
    msg = 'Todos os jogos'

    if limit:
        msg = f'Ultimos {limit} jogos'
    return msg


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
    par_impar_por_jogo = {}

    resultados = postgres.get_all(Jogo, skip, limit, jogo)

    for resultado in resultados:
        resultado_dict = resultado.dict()
        concurso = resultado_dict['concurso']
        par = 0
        impar = 0

        for number in resultado_dict['dezenas']:
            final_result[number] += 1
            if number % 2 == 0:
                par += 1
            else:
                impar += 1
        par_impar_por_jogo[concurso] = [par, impar]

    # _grafico_barras_total_numeros_por_jogos(msg, final_result)

    _grafico_total_de_pares_e_impares_por_jogo(msg, par_impar_por_jogo)


if __name__ == '__main__':
    numbers_per_game(jogo="lotofacil", skip=0, limit=10)
