#!/usr/bin/env python3

import os
import sys
from parameter import *

fasta = sys.argv[1]
for i in range(transpose_begin//column_block, transpose_end//column_block ):
	os.system('./flatten.sh {} | ./column.py {}'.format(fasta, i))
