import numpy as np

class Individuo:

    def __init__(self, tablero, fitness=0):
        self.tablero = list(tablero)
        self.fitness = fitness

    def calcFitness(self):
        indTablero = [x - 1 for x in self.tablero]
        hits = 0
        tablero = llenar_tablero(crear_tablero(len(self.tablero)), list(indTablero))
        col = 0
        for queen in list(indTablero):
            try:
                for i in range(col - 1, -1, -1):
                    if tablero[queen][i] == 1:
                        hits += 1
            except IndexError:
                pass
            for i, j in zip(range(queen - 1, -1, -1), range(col - 1, -1, -1)):
                if tablero[i][j] == 1:
                    hits += 1
            for i, j in zip(range(queen + 1, len(self.tablero), 1), range(col - 1, -1, -1)):
                if tablero[i][j] == 1:
                    hits += 1
            col += 1
        self.fitness = np.sum(list(range(len(self.tablero)))) - hits
        return self.fitness

    def __str__(self):
        #    _ _ _ _ _ _ _ _
        #   |Q|_|_|_|_|_|_|_|
        #   |_|Q|_|_|_|_|_|_|
        #   |_|_|Q|_|_|_|_|_|
        #   |_|_|_|Q|_|_|_|_|
        #   |_|_|_|_|Q|_|_|_|
        #   |_|_|_|_|_|Q|_|_|
        #   |_|_|_|_|_|_|Q|_|
        #   |_|_|_|_|_|_|_|Q|
        n = len(self.tablero)
        matr = crear_tablero(n)
        for i in range(n):
            for j in range(n):
                if (i + 1) == self.tablero[j]:
                    matr[i][j] = 1

        tablero = " _ _ _ _ _ _ _  \n"
        for i in range(n):
            for j in range(n):
                tablero += '|'
                tablero += '♛' if matr[i][j] == 1 else '_'
            tablero = tablero[:-1] + '\n'

        return tablero


def crear_tablero(n):
    return np.zeros((n, n), dtype=int)

def llenar_tablero(tablero, gen):
    for (i, pos) in enumerate(gen):
        tablero[pos][i] = 1
    return tablero
