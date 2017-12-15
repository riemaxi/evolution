
import numpy as np

class Model:
	def __init__(self, data):
		self.load(data)

	def load(self, data):
		self.matrix = [[float(p) for p in r.split('\t')] for r in open(data).read().strip().split('\n')]
		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))

	def weight(self, base, g, data = None):
		return self.matrix[base]

	def next(self, base, generation, data = None):
		return np.random.choice(self.bases, p = self.weight(base, generation, data), size = 1)[0]
