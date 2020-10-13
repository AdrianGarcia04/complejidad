import numpy as np

class Solution:
    def __init__(self, num_vars):
        self.num_vars = num_vars
        self.asigns = np.zeros(num_vars, dtype='int')

        for i in range(num_vars):
            self.asigns[i] = (np.random.rand() * 1000) % 2

    def eval(self, instance):
        passed = 0
        evals = []
        for formula in instance.formulas:
            (v1, v2, v3) = formula
            (i1, i2, i3) = self.to_var(formula)

            eval1 = self.asigns[i1] if v1 >= 0 else (not self.asigns[i1])
            eval2 = self.asigns[i2] if v2 >= 0 else (not self.asigns[i2])
            eval3 = self.asigns[i3] if v3 >= 0 else (not self.asigns[i3])

            eval = (eval1 or eval2 or eval3)
            evals.append(eval)
            passed = passed + 1 if eval else passed

        return passed

    def to_var(self, variables):
        (v1, v2, v3) = variables
        return (np.absolute(v1) - 1, np.absolute(v2) - 1, np.absolute(v3) - 1)
