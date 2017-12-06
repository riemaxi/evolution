#!/usr/bin/env python3

from mutation import *
from parameter import *

def load_fitness(source):
	data = {}
	for line in open(source):
		g, f = line.strip().split('\t')
		data[g] = float(f)

	return data

fitness = load_fitness(fitness_data)
pop = [[1,1],[2,1],[2,2],[1,2],[2,2],[1,2]]

print(pop)
print( mutate(mutate(mutate(pop))) )

