#!/usr/bin/env python3

import random
import sys
from parameter import *
import numpy

def create_individual(ploidy, haplotypes, weight):
	htvector = list(range(1,haplotypes+1))
	return [str(numpy.random.choice(htvector, p = weight)) for i in range(ploidy)]

def load_fitness(file):
	try:
		data = {}
		for line in open(file):
			g, f = line.strip().split('\t')
			data[g] = f
	except:
		pass

	return data

def get_fitness(table, individual, default_fitness):
	return table.get(','.join(sorted(individual)), default_fitness)

fitness = load_fitness(fitness_data)


# logic
for i in range(population_size):
	individual = create_individual(ploidy, haplotypes, populate_weight)

	print('\t'.join(individual))
