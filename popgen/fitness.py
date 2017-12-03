#!/usr/bin/env python3

import numpy

class Fitness:
	def __init__(self, source = 'data.fitness', haplotypes = 2, default_value = 1.0):
		self.default_value = default_value
		self.data = self.load(source)
	
		self.total = self.total_fitness(haplotypes)
		self.weight = self.get_weight(haplotypes)
		self.vector = self.get_vector(haplotypes)

	def get_vector(self,n):
		vector = []
		for i in range(n):
			for j in range(i,n):
				vector.append( '{},{}'.format(i+1, j+1) )
		return vector


	def get_weight(self,n):
		weight = []
		for i in range(n):
			for j in range(i,n):
				f = float( self.get( (str(i+1), str(j+1)) ) )/self.total
				weight.append(f)
		return weight

	def ok(self, indiv, weight = None):
		try:
			if weight != None:
				l = len(weight)

				v = []
				w = []
				for a,b in weight.items():
					v.append(a)
					w.append(b)
			else:
				w = self.weight
				v = self.vector

			return numpy.random.choice( v, p = w) == ','.join(indiv)
		except:
			return False
		

	def total_fitness(self, n):
		s = 0
		for i in range(n):
			for j in range(i,n):
				s += float(self.get((str(i+1), str(j+1))))

		return s

	def load(self, file):
		try:
			data = {}
			for line in open(file):
				g, f = line.strip().split('\t')
				data[g] = f
		except:
			pass

		return data

	def get(self, individual):
		return self.data.get(','.join(sorted(individual)), self.default_value)
