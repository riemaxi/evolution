import random

def max_haplotype(pop):
	return max([max(i) for i in pop])

def mutate(pop, on = True):
	if on:
		for c in range(10):
			i = random.randint(0, len(pop)-1)
			a = random.randint(0, len(pop[i])-1)
			pop[i][a] = max_haplotype(pop) + 1

	return pop
