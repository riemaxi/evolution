#!/usr/bin/env python3

import sys

i = int(sys.argv[1])

print(i, end = '\t')
for line in sys.stdin:
	print(line.strip()[i], end = '')

print()
