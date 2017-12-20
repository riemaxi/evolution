#!/usr/bin/env python3

import os
import sys
from parameter import *

fasta = sys.argv[1]
for i in range(transpose_begin, transpose_end + 1):
	os.system('./flatten.sh {} | ./column.py {}'.format(fasta, i))
