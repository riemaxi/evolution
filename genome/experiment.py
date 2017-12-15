#!/usr/bin/env python3

from parameter import *
from tree import navigate
import os

def simula(trial, a, b, d, rate):
	if b != None:
		os.system('./simula.py {:03} data.seq.{} data.seq.{} {} {}'.format(trial, a, b,d, rate))

for trial in range(1,trials + 1):
	navigate( lambda a,b,d : simula(trial, a , b , d, rate))

