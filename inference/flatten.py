#!/usr/bin/env python3

import sys

print(next(sys.stdin).strip())

seq = ''
for line in sys.stdin:
	if line.startswith('>'):
		print(seq)
		seq = ''
		print(line.strip())

	else:
		seq += line.strip()

print(seq)
