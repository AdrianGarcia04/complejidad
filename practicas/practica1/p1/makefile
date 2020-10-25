NODES=15
DATA_DIR=data
MAX_WEIGHT=650

run: gen test

test:
	python3 p1.py data/instance.txt $(MAX_WEIGHT)

gen:
	python3 GenerateProblem.py $(NODES) > $(DATA_DIR)/instance.txt
