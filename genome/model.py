import numpy as np

class Model:
	def __init__(self, data = None):
		self.load(data)


	def divergency(self, a, b):
		return 0
	
	def load(self, data):
		self.matrix = [[float(p) for p in r.split('\t')] for r in open(data).read().strip().split('\n')]
		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))

	def codes(self, seq):
		code = 'AGCT'
		return [code.index(b) for b in seq]

	def letters(self, seq):
		letter = ['A','G','C','T']
		return ''.join([letter[int(i)] for i in seq])


	def weight(self, base, g, data = None):
		return self.matrix[base]

	def next(self, base, generation, data = None):
		return np.random.choice(self.bases, p = self.weight(base, generation, data), size = 1)[0]
