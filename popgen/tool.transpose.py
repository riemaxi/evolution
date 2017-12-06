#!/usr/bin/env python3

import sys
from parameter import *

def print_gens(gens, maxl):
	for label,lst in gens.items():
		print(label,'\t'.join(lst), sep = '\t')
		maxl = max(maxl, len(lst))
	return maxl


trial = None
gens = {}
max_gen = -1
for line in sys.stdin:
	field = line.strip().split('\t')
	f = field[2:]

	if field[0] != trial:
		max_gen = print_gens(gens, max_gen)

		trial = field[0]
		gens = {}
	else:
		for i in range(1,len(f)+1):
			lst = gens.get(i,[])
			lst.append(f[i-1])
			gens[i] = lst
	
max_gen = print_gens(gens, max_gen)

print('\t','\t'.join([str(g) for g in list(range(1,max_gen+1))]))
