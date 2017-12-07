#!/usr/bin/env python3

from mutation import *
from parameter import *

pop = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]

print(pop)

for i in range(10):
	pop = mutate(pop)
	print(pop)
