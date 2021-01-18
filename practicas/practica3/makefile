NREINAS = 8

NIND = 50
MAXGEN = 250
PORCNEWIND = 0.97
PORCMUTACION = 0.1
FUNSELECCION = ruleta

TEMPERATURA = 100.0

ag:
	@python3 ag-reinas/main.py -n $(NREINAS) -i $(NIND) -m $(MAXGEN) -pn $(PORCNEWIND) -pm $(PORCMUTACION) -f $(FUNSELECCION)

sa:
	@python3 sa-reinas/main.py -n $(NREINAS) -t $(TEMPERATURA)
