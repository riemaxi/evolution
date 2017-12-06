#!/usr/bin/env python3

from mutation import *
from parameter import *
from generation import *
from population import *
from stats import *

def load_fitness(source):
	data = {}
	for line in open(source):
		g, f = line.strip().split('\t')
		data[g] = float(f)

	return data

fitness = load_fitness(fitness_data)
pop = population(pop_size, ploidy, haplotype_no, genotype_weight)

for gen in range(100):
	pop = generation(pop, fitness)

	print(1, 1,'\t'.join(['{:.2f}'.format(f) for f in frequency(pop, haplotype_no)]), sep = '\t' )

