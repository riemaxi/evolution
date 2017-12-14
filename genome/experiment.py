#!/usr/bin/env python3

from parameter import *
import os

for trial in range(trials):
	os.system('./align.sh {:03}'.format(trial))
