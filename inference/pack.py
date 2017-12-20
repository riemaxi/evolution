#!/usr/bin/env python3

import sys

a,b,d = next(sys.stdin).strip().split('\t')

interval = [[float(d),int(a),int(b)]]
count = 1
for line in sys.stdin:
	a,b,d = line.strip().split('\t')

	if interval[-1][2] + 1 == int(a):
		interval[-1][2] = int(b)
		interval[-1][0] += float(d)
		count += 1
	else:
		interval[-1][0] /= count
		interval.append([float(d), int(a),int(b)])
		count = 1

interval[-1][0] /= count

[print( '{:0.2f}\t{}\t{}'.format(i[0], i[1],i[2]) ) for i in interval]
