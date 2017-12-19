#!/usr/bin/env python

from k80model import *

model = K80Model(alpha = 1.0, beta = 0.5)

for t in range(50):
	print(0, model.next(0, t))
