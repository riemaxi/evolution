
import numpy as np

class Model:
	def __init__(self, data, mutation_distribution = [0.25]*4):
		self.load(data)
		self.mutation_distribution = mutation_distribution

	def load(self, data):
		self.matrix = [[float(p) for p in r.split('\t')] for r in open(data).read().strip().split('\n')]
		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))

	def weight(self, base):
		return self.matrix[base]

	def next(self, base):
		return np.random.choice(self.bases, p = self.weight(base), size = 1)[0]
