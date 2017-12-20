#!/usr/bin/env python3

import sys
from parameter import *

def density(column):
	return 100*(1 - column.count('-')/len(column))

def print_block(count, end, total, min_total, output):
	if count > 0:
		total = total/count
		if total >= min_total:
			print( '{}\t{}\t{:0.2f}'.format( end - count, end, total * count ) )
			output.write( '{}\t{}\t{:0.2f}\n'.format( end - count, end, total * count ) )


total = 0
count = 0
with open(blocks_output,'w') as output:
	for column in sys.stdin: 
		i, data = column.strip().split('\t')
		d =  density( data )
		if d >= min_density:
			count += 1
			total += d
		else:
			print_block(count, int(i), total, min_total, output)
			count = 0
			total = 0

	print_block(count, int(i), total, min_total, output)
