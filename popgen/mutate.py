#!/usr/bin/env python3

import sys
import random
from parameter import *
from fitness import *

def load_population():
	population = []
	for i in sys.stdin:
		population.append([int(h) for h in i.strip().split('\t')])

	random.shuffle(population)
	
	return population


def mutation(indiv, max_allele, fitness):
	idx = random.randint(0, len(indiv)-1)
	indiv[idx] = max_allele + 1
	return (indiv, max_allele + 1)

def get_max_allele(population):
	return max([max(i) for i in population])

population = load_population()

max_allele = get_max_allele(population)

fitness = Fitness(fitness_data, haplotypes, default_fitness)
max_mutations = mutate_max
for indiv in population:
	# environmental pressure plus fitness control rate of mutation
	if max_mutations > 0 and not fitness.ok([str(a) for a in indiv]):
		indiv, max_allele = mutation(indiv, max_allele, fitness)
		max_mutations -= 1

	print('\t'.join( [str(ht) for ht in indiv] ) )
		

