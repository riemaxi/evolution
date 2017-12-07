import random
import numpy

def max_haplotype(pop):
	return max([max(i) for i in pop])

def radiation(pop, size = 1, on = True):
	if on:
		selection = numpy.random.choice(list(range(len(pop))), size = size)
		for i in selection:
			a = random.randint(0, len(pop[i])-1)
			pop[i][a] = max_haplotype(pop) + 1


	return pop

def flat(pop, size = 1, on = True):
	if on:
		selection = numpy.random.choice(list(range(len(pop))), size = size)
		maxhp = max_haplotype(pop)
		for i in selection:
			a = random.randint(0, len(pop[i])-1)
			pop[i][a] = maxhp + 1


	return pop

def mutate(pop, size = 1, on = True, type = 'flat'):
	if type == 'flat':
		return flat(pop, size, on)
	else:
		return radiation(pop, size, on)
