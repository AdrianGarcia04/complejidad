NUM_VARS=15
NUM_CLAUSES=10
DATA_DIR=data

run: gen test

test:
	python3 p2.py data/instance.txt

gen:
	python3 GenerateProblem.py $(NUM_VARS) $(NUM_CLAUSES) > $(DATA_DIR)/instance.txt
