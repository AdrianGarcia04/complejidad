import sys
import numpy as np

if __name__ == '__main__':
    num_vars = int(sys.argv[1])
    num_clauses = int(sys.argv[2])

    print(num_vars, num_clauses)

    assigns = 0
    for i in range(num_clauses):

        if (assigns < num_vars):
            v1 = 1 + (assigns % num_vars)
            assigns = assigns + 1

            v2 = 1 + (assigns % num_vars)
            assigns = assigns + 1

            v3 = 1 + (assigns % num_vars)
            assigns = assigns + 1
        else:
            v1 = 1 + (i % num_vars)
            v2 = 1 + int(np.random.rand()*1000 % (num_vars))
            v3 = 1 + int(np.random.rand()*1000 % (num_vars))

            while (v1 == v2): v2 = 1 + int(np.random.rand()*1000 % (num_vars))
            while (v2 == v3): v3 = 1 + int(np.random.rand()*1000 % (num_vars))
            while (v1 == v3): v3 = 1 + int(np.random.rand()*1000 % (num_vars))

        rand1 = int((np.random.random() * 1000) % 2)
        rand2 = int((np.random.random() * 1000) % 2)
        rand3 = int((np.random.random() * 1000) % 2)

        v1 = v1 if (rand1 == 0) else -v1
        v2 = v2 if (rand2 == 0) else -v2
        v3 = v3 if (rand3 == 0) else -v3

        print(v1, v2, v3)
