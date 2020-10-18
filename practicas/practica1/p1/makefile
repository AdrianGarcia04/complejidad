NODES=15
EDGE_PROB=20
DATA_DIR=data
MAX_WEIGHT=650

run: gen test

test:
	python3 p1.py data/instance.txt $(MAX_WEIGHT)

gen:
	python3 GenerateProblem.py $(NODES) $(EDGE_PROB) > $(DATA_DIR)/instance.txt
