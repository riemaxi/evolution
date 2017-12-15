
import numpy
import random
from model import *

class Evolution(object):
	def __init__(self, model , root = None, size =20, mutation_distribution = [0.25]*4):
		self.data = [int(b) for b in root] if root != None else numpy.random.choice(model.bases, size = size).tolist()
		self.model = model
		self.mutation_distribution = mutation_distribution
	
	def wildtype(self):
		return ''.join(self.data)


	def substitution(self):
		i = random.randint(0,len(self.data)-1)

		self.data[i] = self.model.next(self.data[i], self.generation)


	def insertion(self):
		i = random.randint(0,self.model.size-1)
		j = random.randint(1,len(self.data))

		seql = numpy.random.choice(list(range(1,self.model.size + 1)), p = [0.1,0.1,0.5,0.3])
		seq = list(numpy.random.choice(self.model.bases, size = seql))

		self.data = self.data[:j] + seq + self.data[j:]


	def deletion(self):
		j = random.randint(1,len(self.data))
		dell = numpy.random.choice([1,2], p = [0.50, 0.50])

		self.data = self.data[:j] + self.data[j+dell:]


	def none(self):
		pass

	def mutation(self):
		return numpy.random.choice([0,1,2,3],p = self.mutation_distribution)

	def __iter__(self):
		numpy.random.seed()
		self.generation = 1

		return self
	

	def __next__(self):
		[
			self.substitution,
			self.insertion,
			self.deletion,
			self.none
		][self.mutation()]()

		self.generation += 1

		return ''.join([str(b) for b in self.data])
