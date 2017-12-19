from model import *
import math

class K80Model(Model):
	def __init__(self, alpha = 0.5, beta = 0.5):
		Model.__init__(self)

		self.alpha = alpha
		self.beta = beta

	def p0(self, t):
		return 0.25 + 0.25*math.exp(-4*self.beta*t) + 0.5*math.exp(-2*(self.alpha + self.beta)*t)

	def p2(self, t):
		return 0.25 - 0.25*math.exp(-4*self.beta*t)


	def p1(self, t):
		return 0.25 + 0.25*math.exp(-4*self.beta*t) - 0.5*math.exp(-2*(self.alpha + self.beta)*t)


	def load(self,data):
		self.matrix = [
			[self.p0, self.p1, self.p2, self.p2],
			[self.p1, self.p0, self.p2, self.p2],
			[self.p2, self.p2, self.p0, self.p1],
			[self.p2, self.p2, self.p1, self.p0]
		]

		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))


	def codes(self, seq):
		code = 'ACGT'
		return [code.index(b) for b in seq]

	def letters(self, seq):
		letter = ['A','C','G','T']
		return ''.join([letter[int(i)] for i in seq])


	def weight(self, base, t, data = None):
		return [p(t) for p in self.matrix[base]]
