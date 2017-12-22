#!/usr/bin/env python3

import sys
from parameter import *

i = int(sys.argv[1])


lst = []
for line in sys.stdin:
	lst.append(line.strip()[column_block*i:column_block*(i + 1)])

lst = list(zip(*lst))
for j in range(len(lst)):
	print(j + column_block*i, ''.join(lst[j]), sep = '\t')
