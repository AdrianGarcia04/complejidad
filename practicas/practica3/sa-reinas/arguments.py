import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='problema de las n-reinas')

    parser.add_argument('-n', '--nReinas', help='numero de reinas',
        type=int, default=8)

    parser.add_argument('-t', '--temperatura', help='temperatura inicial', type=float,
        default=100.0)

    return parser.parse_args()
