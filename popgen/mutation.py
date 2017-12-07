import random
import numpy

def max_haplotype(pop):
	return max([max(i) for i in pop])

def mutate(pop, on = True):
	if on:
		selection = numpy.random.choice(list(range(len(pop))), size = min(len(pop), max(int(len(pop)/10),10)))
		maxhp = max_haplotype(pop)
		for i in selection:
			a = random.randint(0, len(pop[i])-1)
			pop[i][a] = maxhp + 1

	return pop

def _mutate(pop, on = True):
	if on:
		i = numpy.random.choice(list(range(len(pop))))
		a = random.randint(0, len(pop[i])-1)
		pop[i][a] = max_haplotype(pop) + 1

	return pop
