N = 12
M = 200
P = 4
EPSILON = 0.2

PARAMS := $(shell python3 generate.py $(N) $(M) $(P))

run:
	@python3 p2.py $(PARAMS) $(EPSILON)
