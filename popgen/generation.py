import numpy
import random

def offspring(a,b):
	parent = (a,b)
	l = min(len(a), len(b))
	return [ parent[random.randint(0,1)][i] for i in range(l) ]


def pack(i):
	return ','.join([str(a)for a in sorted(i)])

def fitness_weight(pop, fitness):
	weight = [fitness.get(pack(i),0) for i in pop]
	return [w/sum(weight) for w in weight]

def generation(pop, fitness):
	new_pop = []
	weight = fitness_weight(pop, fitness)
	candidate = list(range(len(pop)))
	for i in range(len(pop)):
		k,l = numpy.random.choice(candidate, size = 2, p = weight)
		new_pop.append( offspring(pop[k], pop[l]) )

	return new_pop

