# Requerimientos:

Python >= 3.7.7
Numpy >= 1.17.4

# Programa 1: Algoritmo Genético

El programa se encuentra en la carpeta ag-reinas, que tiene
la siguiente estructura:

| practica3
└── ag-reinas
    └── arguments.py
    └── Individuo.py
    └── main.py

## Ejecución

Para ejecutarse, nos posicionamos en la carpeta practica3
y ejecutamos el comando "make ag",
lo cual mostrara en pantalla en qué número de generación
se encuentra la ejecución y el número máximo de generaciones,
y cuando termine, mostrará una representación del mejor
tablero encontrado y el número de colisiones de reinas que tiene.
Los parámetros del archivo makefile se pueden cambiar manualmente
o al momento de ejecutar el programa.

## Ejemplos de ejecución

make ag

make ag NREINAS=10

make ag NIND=100 MAXGEN=300

## Ejemplos de resultados

 _ _ _ _ _ _ _  
|_|_|_|_|_|_|♛|
|_|_|_|_|♛|_|_|
|_|_|♛|_|_|_|_|
|♛|_|_|_|_|_|_|
|_|_|_|_|_|♛|_|
|_|_|_|_|_|_|_|
|_|♛|_|_|_|_|_|
|_|_|_|♛|_|_|_|
0 colision(es)


 _ _ _ _ _ _ _  
|_|_|_|_|_|♛|_|
|_|_|♛|_|_|_|_|
|_|♛|_|_|_|_|_|
|_|_|_|_|_|_|_|
|♛|_|_|_|_|_|_|
|_|_|_|♛|_|_|_|
|_|_|_|_|_|_|♛|
|_|_|_|_|♛|_|_|
1 colision(es)


# Problema 2: Recocido Simulado

El programa se encuentra en la carpeta sa-reinas, que tiene
la siguiente estructura:

| practica3
└── sa-reinas
    └── arguments.py
    └── Individuo.py
    └── main.py

## Ejecución

Para ejecutarse, nos posicionamos en la carpeta practica3
y ejecutamos el comando "make sa",
lo cual mostrara en pantalla el valor de la temperatura en la que
se encuentra la ejecución,
y cuando termine, mostrará una representación del mejor
tablero encontrado y el número de colisiones de reinas que tiene.
Los parámetros del archivo makefile se pueden cambiar manualmente
o al momento de ejecutar el programa.

## Ejemplos de ejecución

make sa

make sa NREINAS=10

make sa NREINAS=12 TEMPERATURA=200

## Ejemplos de resultados

 _ _ _ _ _ _ _  
|_|_|_|_|_|♛|_|
|_|_|♛|_|_|_|_|
|_|_|_|_|_|_|♛|
|_|_|_|♛|_|_|_|
|♛|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|♛|_|_|_|_|_|
|_|_|_|_|♛|_|_|
0 colision(es)


 _ _ _ _ _ _ _  
|_|_|_|_|♛|_|_|
|_|_|_|_|_|_|♛|
|♛|_|_|_|_|_|_|
|_|_|♛|_|_|_|_|
|_|_|_|_|_|♛|_|
|_|_|_|_|_|_|_|
|_|♛|_|_|_|_|_|
|_|_|_|♛|_|_|_|
1 colision(es)
