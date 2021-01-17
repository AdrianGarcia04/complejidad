# Requerimientos:

Python >= 3.7.7
Numpy >= 1.17.4
Networkx >= 2.5

# Problema 1: Algoritmo de Christofides

El problema se encuentra en la carpeta p1, que tiene
la siguiente estructura:

| p1
├── ejemplares
│   └── p10.tsp
│   └── p20.tsp
│   └── p25.tsp
│   └── p30.tsp
│   └── p40.tsp
│   └── p50.tsp
├── Graph.py
├── p1.py
└── utils.py

## Ejecución

Para ejecutarse, nos posicionamos en la carpeta p1
y ejecutamos el comando "python3 p1.py ejemplares/p10.tsp",
lo cual mostrara en pantalla la gráfica inducida
por los vertices considerando como ciudades las coordenadas
en "p10.tsp", y mostrará el tour encontrado para la
gráfica.

## Ejemplos de ejecución

python3 p1.py ejemplares/p10.tsp

python3 p1.py ejemplares/p20.tsp

.
.
.

python3 p1.py ejemplares/p50.tsp

# Problema 2: SubsetSum

El problema se encuentra en la carpeta p2, que tiene
la siguiente estructura:

| p2
├── generate.py
├── makefile
└── p2.py


## Ejecución

Para ejecutarse, nos posicionamos en la carpeta p2
y ejecutamos el comando "make".
De esta manera, se ejecuta el programa "generate.py"
que da un ejemplar del problema de Subset sum construido
con los parametros N, M y P, el numero de elementos en el
conjunto, el valor maximo que pueden tomar y cuantos
elementos al azar tomaremos para la solucion, respectivamente.

Posteriormente, se ejecuta "p2.py" que aplica el
esquema de aproximacion definido en los requerimientos de
la tarea y utilizando la variable epsilon del archivo
makefile como parámetro.

## Ejemplos de ejecución

make

make run
