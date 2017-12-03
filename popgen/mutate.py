#!/usr/bin/env python3

import sys
import random
from parameter import *
from fitness import *

def load_population(htnames):
	population = []
	dist = {}
	distsize = 0
	for i in sys.stdin:
		key = ','.join(sorted(i.strip().split('\t')))

		if key in htnames:
			dist[key] = dist.get(key,0) + 1
			distsize += 1

		population.append([int(h) for h in i.strip().split('\t')])

	random.shuffle(population)

	dist = {k:v/distsize for k,v in dist.items()}

	return population, dist


def mutation(indiv, max_allele):
	idx = random.randint(0, len(indiv)-1)
	indiv[idx] = max_allele + 1

	return indiv, max_allele + 1

def get_max_allele(population):
	return max([max(i) for i in population])


def update_distribution(population, htnames):
	dist = {}
	distsize = 0
	for indiv in population:
		key = ','.join([str(a) for a in sorted(indiv)])
		if key in htnames:
			dist[key] = dist.get(key,0) + 1
			distsize += 1

	dist = {k:v/distsize for k,v in dist.items()}

	return dist

def get_haplotypenames(ht):
	names = []
	for i in range(ht):
		for j in range(i,ht):
			names.append('{},{}'.format(i+1,j+1))

	return names

haplotypenames = get_haplotypenames(haplotypes)
population, distribution = load_population(haplotypenames)

max_allele = get_max_allele(population)

fitness = Fitness(fitness_data, haplotypes, default_fitness)
max_mutations = mutate_max
for i in range(len(population)):
	indiv = population[i]

	# environmental pressure plus fitness control rate of mutation
	if max_mutations > 0 and random.randint(0,2*max_mutations) > max_mutations and not fitness.ok([str(a) for a in indiv], distribution):
		indiv, max_allele  = mutation(indiv, max_allele)
		population[i] = indiv[:]

		distribution = update_distribution(population, haplotypenames)

		max_mutations -= 1

	print('\t'.join( [str(ht) for ht in indiv] ) )
