# 2) Subset Sum
import sys

def merge_lists(l1, l2):
    return sorted(set(l1 + l2))

def suml(l, x):
    return [e + x for e in l]

def trim(l, delta):
    m = len(l)
    l_p = [l[0]]
    last = l[0]
    for i in range(1, m):
        if l[i] > last * (1 + delta):
            l_p.append(l[i])
            last = l[i]
    return l_p

def remove(l, t):
    return [e for e in l if e <= t]

if __name__ == '__main__':
    problem_set = [int(c) for c in sys.argv[1].strip('[]').split(',')]
    print("Conjunto de entrada: ", problem_set)
    problem_set.insert(0, 0)

    t = int(sys.argv[2])
    print("Valor de t: ", t)

    eps = float(sys.argv[3])
    print("Valor de epsilon: ", eps)

    n = len(problem_set)
    lists = [[]] * n
    lists[0] = [0]

    for i in range(1, n):
        lists[i] = merge_lists(lists[i - 1], suml(lists[i - 1], problem_set[i]))
        lists[i] = trim(lists[i], eps / (2 * n))
        lists[i] = remove(lists[i], t)

    print("Se encontró un subconjunto cuya suma es: ", max(lists[n - 1]))
