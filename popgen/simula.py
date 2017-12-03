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

	os.system('./evolution.sh {} {} {}'.format(generation, trial, destination))

trial = sys.argv[1]
destination = sys.argv[2]
generation = 1

initialize(generation, trial)

while generation <= max_generation and not fixed(haplotypes):
	os.system('./mate.sh')
	os.system('./mutate{}.sh'.format(breeding_mode))

	generation += 1
	os.system('./evolution.sh {} {} {}'.format(generation, trial, destination))

	os.system('./report_frequency.sh {} {}'.format(trial, destination))

os.system('rm data.mutant data.mutant.current')
