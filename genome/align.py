#!/usr/bin/env python3

from Bio import pairwise2 as pw
import sys

n,a = next(sys.stdin).strip().split('\t')
n,b = next(sys.stdin).strip().split('\t')

trial = sys.argv[1]

try:
	alignment = pw.align.globalmx(a,b,2,-1)

	print(trial + '\t!\t' + alignment[0][0], trial + '\t!\t' + alignment[1][0], sep = '\n')
except:
	print(trial + '\t?\t' + alignment[0][0], trial + '\t?\t' + alignment[0][1], sep = '\n')

