#!/usr/bin/env python3

import sys

gen = sys.argv[1]

print(gen, end = '\t')
for indiv in sys.stdin:
	print( indiv.strip().replace('\t',','), end = '\t' )
	
print()
