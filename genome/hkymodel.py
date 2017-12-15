from model import *
import math

class HKYModel(Model):
	def __init__(self, mu):
		Model.__init__(self, data = 'data.hky')
		self.mu = mu

	def weight(self, base, g, data = None):
		return [0.25]*4
