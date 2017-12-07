#!/usr/bin/env python3

import sys
import numpy
from parameter import *
from population import *
from mutation import *
from generation import *
from stats import *

def load_fitness(source):
	data = {}
	for line in open(source):
		g, f = line.strip().split('\t')
		data[g] = float(f)

	return data

def fixed(pop, ht_no, end):
	v, size = count_alleles(pop, ht_no)
	return v.count(0) == len(v) - 1 or end

def print_stats(trial, gen, pop, ht_no, file):
	freq, count, size = frequency(pop, ht_no)
	file.write('{}\t{}\t{}\n'.format( trial, gen,'\t'.join(['{:.2f}'.format(f) for f in freq]) ) )
	print(trial, gen, count,  sep = '\t')


trial = sys.argv[1]
dest = sys.argv[2]
report = '{}/report.frequency'.format(dest)

fitness = load_fitness(fitness_data)
pop = mutate( population(pop_size, ploidy, haplotype_no, genotype_weight), mutation_size, mutation_on, mutation_type )

gen = 1
with open(report,'a') as file:
	while not fixed(pop, haplotype_no, gen > max_generations):
		print_stats(trial, gen, pop, haplotype_no, file )

		pop = generation(pop, fitness) 

		gen += 1

	print_stats(trial, gen, pop, haplotype_no, file )


