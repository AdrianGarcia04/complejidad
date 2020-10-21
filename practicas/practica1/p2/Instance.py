import numpy as np

class Instance:
    def __init__(self):
        self.num_vars = 0
        self.num_clauses = 0
        self.formulas = []

    def read_file(self, path):
        file = open(path, "r")

        line = file.readline().strip()
        segments = line.split(' ')
        self.num_vars = int(segments[0])
        self.num_clauses = int(segments[1])

        for line in file:
            segments = line.split(' ')
            v1 = int(segments[0].strip())
            v2 = int(segments[1].strip())
            v3 = int(segments[2].strip())

            self.formulas.append((v1, v2, v3))

    def __str__(self):
        res = ""
        for formula in self.formulas:
            (v1, v2, v3) = formula
            v1 = abs(v1)
            v2 = abs(v2)
            v3 = abs(v3)
            res += "(x_{} v x_{} v x_{}) ^ ".format(v1, v2, v3)
        return res[:-2]
