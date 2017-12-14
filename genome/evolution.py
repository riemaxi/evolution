
import numpy
import random
from model import *

class Evolution(object):
	def __init__(self, model , size = 20):
		self.data = numpy.random.choice(model.bases, size = size).tolist()
		self.size = size
		self.model = model
	
	def wildtype(self):
		return ''.join(self.data)


	def substitution(self):
		i = random.randint(0,len(self.data)-1)

		self.data[i] = self.model.next(self.data[i])


	def insertion(self):
		i = random.randint(0,self.model.size-1)
		j = random.randint(1,len(self.data))

		seql = numpy.random.choice(list(range(1,self.model.size + 1)), p = [0.15,0.15,0.55,0.15])
		seq = list(numpy.random.choice(self.model.bases, size = seql))

		self.data = self.data[:j] + seq + self.data[j:]


	def deletion(self):
		j = random.randint(1,len(self.data))
		dell = numpy.random.choice([1,2], p = [0.50, 0.50])

		self.data = self.data[:j] + self.data[j+dell:]


	def none(self):
		pass

	def mutation(self):
		return numpy.random.choice([0,1,2,3],p = self.model.mutation_distribution)

	def __iter__(self):
		numpy.random.seed()

		return self
	

	def __next__(self):
		[
			self.substitution,
			self.insertion,
			self.deletion,
			self.none
		][self.mutation()]()

		return ''.join([str(b) for b in self.data])
