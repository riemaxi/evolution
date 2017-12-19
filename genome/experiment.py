#!/usr/bin/env python3

from parameter import *
from tree import navigate
import os
import sys

def simula(trial, a, b, d, rate, destination):
	if b != None:
		os.system('./simula.py {:03} data.seq.{} data.seq.{} {} {} {}'.format(trial, a, b,d, rate, destination))

destination = sys.argv[1] if len(sys.argv)>1 else 'experiment_{}'.format(datetime.datetime.now().microsecond)

destination = result + '/' + destination

os.system('rm -rf {}'.format(destination))
os.system('mkdir -p {}'.format(destination))

for trial in range(1,trials + 1):
	navigate( lambda a,b,d : simula(trial, a , b , d, rate, destination))

