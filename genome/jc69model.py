from model import *
import math

class JC69Model(Model):
	def __init__(self, mu):
		Model.__init__(self, data = 'data.jc69')
		self.mu = mu

	def weight(self, base, g, data = None):
		return [(1 + p*math.exp(-g*self.mu))/4 for p in self.matrix[base]]
