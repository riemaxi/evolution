#!/usr/bin/env python

from jc69model import *

model = JC69Model(mu = 0.1)

for g in range(50):
	print(0, model.next(0, g))
