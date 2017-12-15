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
a = codes(open(sys.argv[2]).read().strip())
b = sys.argv[3]

distance = float(sys.argv[4])
rate = float(sys.argv[5])

evolution = Evolution(model = HKYModel(mu = 0.1), root = a, mutation_distribution = mutation_distribution, size = seq_size)

t = 0
step = d*rate
for mutant in evolution:
	seq = letters(mutant)
	print('{}\t{:0.4}\t{}'.format(trial,t, seq))

	t += step

	if t > distance:
		break

open(b,'w').write(seq + '\n')
