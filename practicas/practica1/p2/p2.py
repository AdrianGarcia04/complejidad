# b) 3SAT

import sys
import numpy as np
from Instance import Instance
from Solution import Solution

if __name__ == '__main__':
    # Reading args
    file = sys.argv[1]

    # Reading file
    instance = Instance()
    instance.read_file(file)
    print("Ejemplar del problema a tratar de resolver:\n", str(instance))

    # Generating random solution
    solution = Solution(instance.num_vars)
    print("Candidato a solución:\n", str(solution))

    eval = solution.eval(instance)
    if eval < instance.num_clauses:
        print("El candidato no resuelve el problema, {} de {} cláusulas son válidas.".format(eval, instance.num_clauses))
    else:
        print("El candidato resuelve el problema, todas las cláusulas son válidas")
