import argparse

def defineArgs():
    parser = argparse.ArgumentParser(description='problema de las n-reinas')

    parser.add_argument('-n', '--nReinas', help='numero de reinas',
        type=int, default=8)

    parser.add_argument('-i', '--nInd', help='individuos por generacion', type=int,
        default=50)

    parser.add_argument('-m', '--maxGen', help='maximo de generaciones', type=int,
        default=250)

    parser.add_argument('-pn', '--porcNewInd', help='porcentaje nuevos individuos', type=float,
        default=0.97)

    parser.add_argument('-pm', '--porcMutacion', help='porcentaje de mutacion', type=float,
        default=0.1)

    parser.add_argument('-f', '--funSeleccion', help='operador de seleccion', type=str,
        default='ruleta', choices=['ruleta', 'torneo'])

    return parser.parse_args()
