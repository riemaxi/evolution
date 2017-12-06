#!/usr/bin/env python3

import sys
import os
from parameter import *
import datetime

destination = sys.argv[1] if len(sys.argv)>1 else 'experiment_{}'.format(datetime.datetime.now().microsecond)

destination = result + '/' + destination

os.system('rm -rf {}'.format(destination))
os.system('mkdir -p {}'.format(destination))

for trial in range(trials):
	os.system('./simula.py {:04} {}'.format(trial + 1, destination))

os.system('./tool.transpose.sh {}/report.frequency'.format(destination))
os.system('cat {0}/report.frequency.transposed | ./tool.graphic_heatmap.py > {0}/heatmap.html'.format(destination))
