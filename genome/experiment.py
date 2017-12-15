#!/usr/bin/env python3

from parameter import *
import os

def simula(trial, root):
	os.system('./simula.py {:03} {} {}'.format(trial, root, 'data.a'))
	os.system('./simula.py {:03} {} {}'.format(trial, root, 'data.common'))
	os.system('./simula.py {:03} {} {}'.format(trial, 'data.common', 'data.b'))
	os.system('./simula.py {:03} {} {}'.format(trial, 'data.common', 'data.c'))

def align(trial):
	os.system('./align.py {:03} data.root data.common')
	os.system('./align.py {:03} data.root data.a')
	os.system('./align.py {:03} data.common data.b')
	os.system('./align.py {:03} data.common data.c')


for trial in range(1,trials + 1):
	simula(trial, root)

	align(trial)

