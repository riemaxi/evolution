#!/usr/bin/env python3

def count_alleles(pop, ht_no):
	flatten = [a for lst in pop for a in lst]
	return [flatten.count(i) for i in range(1,ht_no+1)], len(flatten)

def fixed(pop, ht_no):
	v, size = count_alleles(pop, ht_no)
	return v.count(0) == len(v) - 1

def frequency(pop, ht_no):
	v, size = count_alleles(pop, ht_no)
	return ['{:.2f}'.format(c/size) for c in v]

_pop = [(1,1),(2,1),(2,2),(1,2),(2,2),(1,2)]
pop = [(11,21),(12,3),(32,42),(41,62),(22,42),(51,2)]

print( count_alleles(pop, 2))
print( fixed(pop, 2) )
print( frequency(pop, 2) )
