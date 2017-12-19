#!/usr/bin/env python

from tn93model import *

metric = TN93Metric(0.25, 0.25, 0.25, 0.25)

#a = 'ATCG--CCTG-A'
#b = 'GTAT--TCTG-T'

a = 'AAAACCCCGGGGTTTTAA'
b = 'TTTTGGGGAAAACCCCTT'

print( metric.divergency(a,b) )



