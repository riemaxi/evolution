#!/usr/bin/env python3

import sys
from parameter import *

def density(column):
	n = len(column)
	d = 100*(1 - column.count('-')/n)
	l = [column[i]!=column[j] for i in range(n) for j in range(i+1,n)]	

	return d,l.count(True)/len(l)

def print_block(count, end, total, polymorphism,  min_total, output):
	if count>0 and total/count >= min_total:
		print( '{}\t{}\t{:0.2f}\t{:0.2f}'.format( end - count + 1, end, total, polymorphism/count ) )
		output.write( '{}\t{}\t{:0.2f}\t{:0.2f}\n'.format( end - count + 1, end, total, polymorphism/count ) )


total = 0
count = 0
polymorphism = 0
with open(blocks_output,'w') as output:
	for column in sys.stdin: 
		i, data = column.strip().split('\t')
		d,p =  density( data )
		if d >= min_density:
			count += 1
			total += d
			polymorphism += p
		else:
			print_block(count, int(i) - 1, total, polymorphism, min_total, output)
			count = 0
			total = 0
			polymorphism = 0

	print_block(count, int(i), total, polymorphism, min_total, output)
