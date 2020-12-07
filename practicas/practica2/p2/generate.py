import sys
import numpy as np

if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    p = int(sys.argv[3])

    problem_set = list(np.random.randint(m, size=n))
    t = np.sum(np.random.choice(problem_set, 5))

    problem_set_str = "["
    for v in problem_set:
        problem_set_str += f"{v},"
    problem_set_str = problem_set_str[:-1] + "]"

    print(problem_set_str, t)
