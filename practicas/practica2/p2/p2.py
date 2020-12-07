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
    problem_set.insert(0, 0)
    t = int(sys.argv[2])
    eps = float(sys.argv[3])

    n = len(problem_set)
    lists = [[]] * n
    lists[0] = [0]
    print(f"line 2: L{0} = ", lists[0], "\n")

    for i in range(1, n):
        lists[i] = merge_lists(lists[i - 1], suml(lists[i - 1], problem_set[i]))
        print(f"line 4: L{i} = ", lists[i])

        lists[i] = trim(lists[i], eps / (2 * n))
        print(f"line 5: L{i} = ", lists[i])

        lists[i] = remove(lists[i], t)
        print(f"line 6: L{i} = ", lists[i], "\n")

    print(max(lists[n - 1]))
