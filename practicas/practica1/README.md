# Requerimientos:

Python >= 3.7.7
Numpy >= 1.17.4
Networkx >= 2.5

# Problema 1: Árbol Generador con Pesos

El problema se encuentra en la carpeta p1, que tiene
la siguiente estructura:

| p1
├── data
│   └── instance.txt
├── GenerateProblem.py
├── Graph.py
├── makefile
└── p1.py

## Ejecución

Para ejecutarse, nos posicionamos en la carpeta p1
y ejecutamos alguno de los siguientes comandos.
El archivo makefile tiene tres comandos, "run", "test" y
"gen". "run" ejecuta todo el programa, "test" solo lee el
archivo data/instance.txt para después dar una solución
aleatoria y verificarla, y "gen" crea el archivo instance.txt.

## Ejemplos de ejecución

make run
  El cual muestra en pantalla el ejemplar del problema y
  la solución aleatoria propuesta.

make test MAX_WEIGHT=600
  El cual genera la solución aleatoria y MAX_WEIGHT=600 representa
  el peso que buscamos que la gráfica cumpla al sumar todas
  las aristas. Si la solución aleatoria excede dicho MAX_WEIGHT,
  el programa muestra que el problema no se solucionó.

make gen NODES=10
  El cual genera una gráfica y la guarda en el archivo
  data/instance.txt, donde su número de nodos
  corresponde a lo que indica NODES.

# Problema 2: 3-SAT

El problema se encuentra en la carpeta p2, que tiene
la siguiente estructura:

| p2
├── data
│   └── instance.txt
├── GenerateProblem.py
├── Instance.py
├── makefile
├── p2.py
└── Solution.py


## Ejecución

Para ejecutarse, nos posicionamos en la carpeta p2
y ejecutamos alguno de los siguientes comandos.
El archivo makefile tiene tres comandos, "run", "test" y
"gen". "run" ejecuta todo el programa, "test" solo lee el
archivo data/instance.txt para después dar una solución
aleatoria y verificarla, y "gen" crea el archivo instance.txt.

## Ejemplos de ejecución

make run
  El cual muestra en pantalla el ejemplar del problema y
  la solución aleatoria propuesta, mostrando si se solucionó
  o no el problema.

make test
  El cual genera la solución aleatoria y la prueba. Si la solución aleatoria hace que todas las cláusulas sean satisfacibles,
  el programa muestra que el problema se solucionó.

make gen NUM_VARS=15 NUM_CLAUSES=10
  El cual genera un ejemplar de 3-SAT con 15
  variables denotadas x_1, x_2, ..., x_15 y con
  15 cláusulas, y la guarda en el archivo
  data/instance.txt.
  Nótese que el número de cláusulas debe
  ser al menos mayor a 3 veces el número de variables
  para que el ejemplar sea construido como se requiere.
  Si se quisiera un ejemplar de 2 cláusulas y 10
  variables, 4 variables no serían consideradas
  en el ejemplar, solo 6.

Por ejemplo, para usar el primer programa basta con
ejecutar "make" desde la carpeta p1. Análogamente,
basta con ejecutar "make" desde la carpeta p2 para
ejecutar el segundo programa.
