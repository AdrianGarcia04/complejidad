import arguments
import numpy as np
import copy
from Individuo import Individuo

def generaTableroInicial():
    rango = list(range(1, nReinas + 1))
    return Individuo(np.random.choice(rango, nReinas, replace=False))

def generarVecino(configuracion):
    confCopy = copy.deepcopy(configuracion)
    swap1 = np.random.randint(1, nReinas)
    swap2 = np.random.randint(1, nReinas)
    while swap1 == swap2:
        swap2 = np.random.randint(1, nReinas)

    tmp = confCopy.tablero[swap1]
    confCopy.tablero[swap1] = confCopy.tablero[swap2]
    confCopy.tablero[swap2] = tmp
    confCopy.calcFitness()
    return confCopy

def main(args):
    args = vars(args)
    global nReinas
    global temperatura
    nReinas = args['nReinas']
    temperatura = args['temperatura']

    configuracion = generaTableroInicial()
    mejorConfiguracion = configuracion

    while temperatura > 0:
        vecino = generarVecino(configuracion)
        fitnessActual = configuracion.fitness
        fitnessVecino = vecino.fitness

        if fitnessVecino > fitnessActual:
            configuracion = vecino
            if fitnessVecino > mejorConfiguracion.fitness:
                mejorConfiguracion = vecino
        else:

            probabilidadAceptacion = np.exp(-(fitnessVecino - fitnessActual) / temperatura)

            if np.random.rand() < probabilidadAceptacion:
                configuracion = vecino

        temperatura -= 1

    print(mejorConfiguracion.tablero)
    print(mejorConfiguracion.fitness)
main(arguments.defineArgs())
