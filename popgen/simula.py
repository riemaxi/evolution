#!/usr/bin/env python3

import os
import sys
from parameter import *


def fixed(haplotypes):
	instances = [0]*haplotypes
	for indiv in open('data.mutant'):
		indiv = indiv.strip().split('\t') 
		for ht in range(1,haplotypes + 1):
			if str(ht) in indiv:
				instances[ht-1] += 1

	return instances.count(0) == len(instances) - 1


def initialize(generation, trial):
	os.system('./populate.sh')

	os.system('rm -f data.evolution.{}'.format(trial))
	os.system('rm -f report.frequency.{}'.format(trial))
	os.system('./evolution.sh {} {}'.format(generation, trial))

trial = sys.argv[1]
generation = 1

initialize(generation, trial)

while generation <= max_generation and not fixed(haplotypes):
	os.system('./mate.sh')
	os.system('./mutate.sh')

	generation += 1
	os.system('./evolution.sh {} {}'.format(generation, trial))

	os.system('./report_frequency.sh {}'.format(trial))

os.system('rm data.mutant data.mutant.current')
