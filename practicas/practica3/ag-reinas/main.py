import arguments
import numpy as np

class Individuo:
    def __init__(self, tablero, fitness=0):
        self.tablero = list(tablero)
        self.fitness = fitness

def generaPoblacionInicial():
    rango = list(range(1, nReinas + 1))
    return [Individuo(np.random.choice(rango, nReinas, replace=False)) for _ in range(nInd)]

def evaluaPoblacion(poblacion):
    fitness = []
    for ind in poblacion:
        fitness.append(calcFitness(ind))
    return fitness

def formaNuevaPoblacion(poblacion, fitness):
    nuevosIndividuos = int(len(poblacion) * porcNewInd)
    padres = []

    # Seleccion de los padres por ruleta o torneo
    if funSeleccion == 'ruleta':
        fitnessMax = np.sum(fitness)
        fitnessProb = [x / fitnessMax for x in fitness]
        for _ in range(nuevosIndividuos):
            elegidos = np.random.choice(poblacion, 2, p=fitnessProb)
            padres.append(elegidos[0])
            padres.append(elegidos[1])

    elif funSeleccion == 'torneo':
        while len(padres) < nuevosIndividuos:
            participantes = np.random.choice(poblacion, size=2)
            participantes = sorted(participantes, key=lambda x: x.fitness)
            padres.append(participantes[1])

    # Se cruzan los padres
    nuevos = []
    while len(nuevos) < nuevosIndividuos:
        p1 = np.random.choice(poblacion)
        p2 = np.random.choice(poblacion)
        nuevos.append(cruza(p1, p2))

    # Mutacion de hijos
    for hijo in nuevos:
        for i, x in enumerate(hijo.tablero):
            if np.random.rand() < porcMutacion:
                hijo.tablero[i] = np.random.randint(1, nReinas + 1)

    ordenados = sorted(poblacion, key=lambda x: x.fitness)
    while len(nuevos) < len(poblacion):
        nuevos.append(ordenados.pop())
    return nuevos

def cruza(ind1, ind2):
    rn = np.random.randint(1, nReinas)
    i = 0
    nuevo = [0] * nReinas
    while i < nReinas:
        if i <= rn:
            nuevo[i] = ind1.tablero[i]
        else:
            nuevo[i] = ind2.tablero[i]
        i += 1
    return Individuo(nuevo)

def crear_tablero(n):
    return np.zeros((n, n), dtype=int)

def llenar_tablero(tablero, gen):
    for (i, pos) in enumerate(gen):
        tablero[pos][i] = 1
    return tablero

def calcFitness(ind):
    indTablero = [x - 1 for x in ind.tablero]
    hits = 0
    tablero = llenar_tablero(crear_tablero(nReinas), list(indTablero))
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
        for i, j in zip(range(queen + 1, nReinas, 1), range(col - 1, -1, -1)):
            if tablero[i][j] == 1:
                hits += 1
        col += 1
    ind.fitness = np.sum(list(range(nReinas))) - hits
    return ind.fitness

def main(args):
    args = vars(args)
    global nReinas
    global nInd
    global maxGen
    global porcNewInd
    global porcMutacion
    global funSeleccion
    nReinas = args['nReinas']
    nInd = args['nInd']
    maxGen = args['maxGen']
    porcNewInd = args['porcNewInd']
    porcMutacion = args['porcMutacion']
    funSeleccion = args['funSeleccion']

    poblacion = generaPoblacionInicial()
    fitness = evaluaPoblacion(poblacion)

    fitnessMedio = np.zeros((maxGen,), dtype=int)
    mejorFitness = np.zeros((maxGen,), dtype=int)
    mejorIndividuo = np.zeros((maxGen, nReinas), dtype=int)

    gen = 0
    while gen < maxGen:
        poblacion = formaNuevaPoblacion(poblacion, fitness)
        fitness = evaluaPoblacion(poblacion)
        gen += 1

    ordenados = sorted(poblacion, key=lambda x: x.fitness)
    print(ordenados[49].tablero, ordenados[49].fitness)

main(arguments.defineArgs())
# calcFitness([5,3,1,6,8,2,4,7])
