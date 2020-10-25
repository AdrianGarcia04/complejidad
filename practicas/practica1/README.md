El primer problema se encuentra en la carpeta P1, el
cual busca resolver el problema de encontrar un Árbol Generador
con Pesos. Puede generarse una gráfica con pesos aleatorios
usando el comando "make gen", y posteriormente con
el comando "make test" se crea un candidato a árbol generador aleatorio
y se comprueba si cumple con tener peso menor o igual a B.

En el archivo makefile pueden especificarse las características
de la gráfica, como el número de nodos y el peso máximo que
se pueden asignar a las aristas.

El segundo problema se encuentra en la carpeta P2,
el cual busca resolver el problema de encontrar una
solución a un ejemplar del 3-SAT. Puede generarse un
ejemplar aleatorio del 3-SAT con el comando "make gen",
y posteriormente con el comando "make test" se crea un candidato
a solución aleatorio y se comprueba si satisface todas
las cláusulas del ejemplar.

En el archivo makefile pueden especificarse
las características del ejemplar, como el número
de variables y el número de cláusulas que
tendrá. Nótese que el número de cláusulas debe
ser al mayor a 3 veces el número de variables
para que el ejemplar sea construido como se requiere.
Si se quisiera un ejemplar de 2 cláusulas y 10
variables, 4 variables no serían consideradas
en el ejemplar.

Por ejemplo, para usar el primer programa basta con
ejecutar "make" desde la carpeta p1. Análogamente,
basta con ejecutar "make" desde la carpeta p2 para
ejecutar el segundo programa.
