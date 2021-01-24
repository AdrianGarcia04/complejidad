import arguments
import numpy as np
from Individuo import Individuo

def generaPoblacionInicial():
    rango = list(range(1, nReinas + 1))
    return [Individuo(np.random.choice(rango, nReinas, replace=False)) for _ in range(nInd)]

def evaluaPoblacion(poblacion):
    fitness = []
    for ind in poblacion:
        fitness.append(ind.calcFitness())
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

    gen = 0
    while gen < maxGen:
        print(f'Gen {gen}:{maxGen}', end='\r')
        poblacion = formaNuevaPoblacion(poblacion, fitness)
        fitness = evaluaPoblacion(poblacion)
        gen += 1

    ordenados = sorted(poblacion, key=lambda x: x.fitness)
    max_choques = np.sum(list(range(nReinas)))
    print(str(ordenados[49]), f'{max_choques - ordenados[49].fitness} colision(es)')

main(arguments.defineArgs())
