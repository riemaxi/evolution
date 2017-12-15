
class Distance:
	def dna(self, a,b):
		size = min(len(a), len(b))
		value = sum([[0,1][a[i] != b[i]] for i in range(size)])/max(len(a), len(b))

		return value
