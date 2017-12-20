#!/usr/bin/env python3

import sys
from parameter import *

a,b,d = next(sys.stdin).strip().split('\t')

interval = [[float(d),int(a),int(b)]]
count = 1
for line in sys.stdin:
	a,b,d = line.strip().split('\t')

	if int(a) - interval[-1][2] <= pack_gap:
		interval[-1][2] = int(b)
		interval[-1][0] += float(d)
		count += 1
	else:
		interval.append([float(d), int(a),int(b)])
		count = 1

[print( '{:<8s}\t{}\t{}'.format('{:0.2f}'.format(i[0]), i[1],i[2]) ) for i in interval]
