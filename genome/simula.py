#!/usr/bin/env python3

from parameter import *
from evolution import *

def letters(a):
	letter = ['A','C','G','T',]
	return ''.join([letter[int(i)] for i in a])

evolution = Evolution(model = Model(data = 'data.emodel', mutation_distribution = mutation_distribution), size = seq_size)

gen = 0
for mutant in evolution:
	print('{0:03}\t{1}'.format(gen, letters(mutant)))

	gen += 1

	if gen>max_gen:
		break
