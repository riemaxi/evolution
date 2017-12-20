#!/usr/bin/env python3

import sys

begin = int(sys.argv[1])
end = int(sys.argv[2])

for line in sys.stdin:
	print( line.strip()[begin:end])
