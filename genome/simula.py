#!/usr/bin/env python3

from parameter import *
from evolution import *
from tn93model import *
import sys

model = TN93Model()

trial = sys.argv[1]
a = model.codes(open(sys.argv[2]).read().strip())
b = sys.argv[3]

distance = float(sys.argv[4])
rate = float(sys.argv[5])

destination = sys.argv[6]

evolution = Evolution( step = distance*rate, distance = distance, model = model, root = a, mutation_distribution = mutation_distribution)

with open(destination + '/evolution.{}'.format(trial),'w+') as output:
	for mutant in evolution:
		print('{}\t{:0.4f}'.format(trial,evolution.time))

		output.write('{}\t{:0.4f}\t{}\n'.format(trial,evolution.time, model.letters(mutant)))

open(b,'w').write(model.letters(mutant) + '\n')
