#!/usr/bin/env python3

from Bio import pairwise2 as pw
from distance import *
import sys

OK = '\t!\t'
NK = '\t?\t'

d = Distance()

trial = sys.argv[1]
a = open(sys.argv[2]).read().strip()
b = open(sys.argv[3]).read().strip()


try:
	alignment = pw.align.globalmx(a,b,2,-1)

	print(trial + OK + alignment[0][0], trial + OK + alignment[1][0], sep = '\n')
	print('{0}{1}{2:0.2f}'.format(trial,OK,d.dna(alignment[0],alignment[1][0])))
except:
	print(trial + '\t?\t' + alignment[0][0], trial + '\t?\t' + alignment[0][1], sep = '\n')
	print('{0}{1}{2:0.2f}'.format(trial,NK,d.dna(alignment[0],alignment[0][1])))


