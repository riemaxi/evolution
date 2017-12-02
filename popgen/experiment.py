#!/usr/bin/env python3

import os
from parameter import *

os.system('rm -f data.evolution.*')
for trial in range(trials):
	os.system('./simula.py {:04}'.format(trial + 1))
