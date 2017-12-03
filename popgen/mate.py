#!/usr/bin/env python3
import random 
import sys 

def offspring(a,b):
	parent = (a,b)
	print('\t'.join([ parent[random.randint(0,1)][i] for i in range(len(a)) ]) )
	
# logic
a = sys.stdin.readline().strip().split('\t') 
b = sys.stdin.readline().strip().split('\t') 

first_a = a[:] 
first_b = b[:]

for ind in sys.stdin:
	offspring(a,b)
	a = b[:]
	b = ind.strip().split('\t') 

offspring(a,first_b) 
offspring(b,first_a)
