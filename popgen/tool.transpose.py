#!/usr/bin/env python3

import sys
from parameter import *

def print_row(first, gens, max_gen):
	if not first:
		for l,ls in gens.items():
			print(l, '\t'.join(ls), sep = '\t')
			max_gen = max(max_gen, len(ls))
	return max_gen
		

def add_column(f, gens):
	for i in range(1,len(f)+1):
		if gens.get(i) == None:
			gens[i] = []
		gens[i].append(f[i-1])

trial = None
gens = {}
max_gen = 0
for line in sys.stdin:
	field = line.strip().split('\t')

	if field[0] != trial:
		max_gen = print_row(trial == None, gens, max_gen)

		trial = field[0]
		gens = {}

	add_column(field[2:], gens)

max_gen = print_row(False, gens, max_gen)

print('\t','\t'.join([str(g+1) if g%10==0 else '' for g in list(range(max_gen))]))
