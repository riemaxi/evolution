#!/usr/bin/env python

from hkymodel import *

model = HKYModel()

distance = 0.2
rate = 0.01

step = distance * rate
t = 0
while t<distance:
	print(0, model.next(0, t))
	t += step
