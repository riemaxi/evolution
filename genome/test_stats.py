#!/usr/bin/env python3

from stats import *

stats = Stats()

seq = '1111000022223333'
print( seq, stats.base_frequency(seq),  sum(stats.base_frequency(seq)) ,sep = '\t' )


seq = '11111111222233330'
print( seq, stats.base_frequency(seq), sum(stats.base_frequency(seq)), sep = '\t' )
