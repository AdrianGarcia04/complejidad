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

    # Generating random solution
    solution = Solution(instance.num_vars)

    # Show solution and how many num_clauses are true
    print(solution.asigns, solution.eval(instance))
