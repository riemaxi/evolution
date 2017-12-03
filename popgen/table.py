#!/usr/bin/env python3

class Table:
	def __init__(self, source, delim = '\t'):
		self.data = self.load(source, delim)

	def load(self, source, delim = '\t'):
		data = []
		for line in open(source):
			data.append(line.strip().split(delim))

		return data

	#stats
	def distribution(self, delim = ','):
		dist = {}
		fraction = 1.0/len(self.data)
		for e in self.data:
			key = delim.join(sorted(e))
			dist[key] = dist.get(key,0) + fraction

		#dist = [{a : b/len(self.data)} for a,b in dist.items() ]
		return dist

	#iter interface
	def __iter__(self):
		return self.data.__iter__()

	def next(self):
		return self.data.next()

			
