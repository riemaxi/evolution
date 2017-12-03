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

print('G', report_del.join(['F{}'.format(i+1) for i in range(haplotypes)]), sep = report_del)
for f in frequency:
	print(report_del.join(f))
