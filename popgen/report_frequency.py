#!/usr/bin/env python3

import sys
from parameter import *

frequency = []
for gen in sys.stdin:
	gen = gen.strip().replace('\t',',').split(',')
	gennr = gen[0]
	gen = [int(a) for a in gen[1:]]

	count = [0]*(haplotypes + 1)
	count[0] = gennr
	for ht in range(1,len(count)):
		count[ht] = str(float(gen.count(ht))/population_size)

	frequency.append(count)

for f in frequency:
	print('\t'.join(f))
