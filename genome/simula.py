#!/usr/bin/env python3

from parameter import *
from evolution import *
from hkymodel import *
import sys

def codes(a):
	code = 'AGCT'
	return [code.index(b) for b in a]	

def letters(a):
	letter = ['A','G','C','T',]
	return ''.join([letter[int(i)] for i in a])

trial = sys.argv[1]
root = codes(open(sys.argv[2]).read().strip())
extant = sys.argv[3]

evolution = Evolution(model = HKYModel(mu = 0.1), root = root, mutation_distribution = mutation_distribution, size = seq_size)

gen = 0
for mutant in evolution:
	seq = letters(mutant)
	print('{}\t{:03}\t{}'.format(trial,gen, seq))

	gen += 1

	if gen>max_gen:
		break

open(extant,'w').write(seq + '\n')
