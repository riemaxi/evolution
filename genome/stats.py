
class Stats:
	def __init__(self):
		pass

	def base_frequency(self, seq):
		freq = {}
		for b in seq:
			freq[b] = freq.get(b,0) + 1

		return [freq[i]/len(seq) for i in sorted(freq.keys()) ]
