import numpy

def individual(ploidy, ht_no, weight):
	htvector = list(range(1,ht_no + 1))
	return [numpy.random.choice(htvector, p = weight) for i in range(ploidy)]


def population(size, ploidy, ht_no, weight):
	pop = []
	for i in range(size):
		pop.append( individual(ploidy, ht_no, weight) )

	return pop

