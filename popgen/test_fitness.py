#!/usr/bin/env python3

from fitness import *
from table import *

pop = Table('data.mutant')
fitness = Fitness()

d = pop.distribution()


print(d)
print('1,1', fitness.ok(('1','1'), d), )
