import math
from model import *

class TN93Metric:
	def __init__(self, pa,pg,pc,pt):
		self.pa = pa
		self.pg = pg
		self.pc = pc
		self.pt = pt

	def codes(self, seq):
		code = 'AGCT-'
		return [code.index(b) for b in seq]

	def s1(self, a,b): # pyrimidine variation proportion
		return float([a[i]!=b[i] for i in range(len(a)) if a[i] in [2,3] and b[i] in [2,3]].count(True))/float(len(a))

	def s2(self, a,b): # purine variation proportion
		return float([a[i]!=b[i] for i in range(len(a)) if a[i] in [0,1] and b[i] in [0,1]].count(True))/float(len(a))


	def v(self, a, b): # transversion proportion
		return float([a[i]<=1 and b[i]>=2 or a[i]>=2 and b[i]<=1 for i in range(len(a)) if a[i] < 4 and b[i] < 4].count(True))/float(len(a))

	def divergency(self, seqa, seqb):
		seqa = self.codes(seqa)
		seqb = self.codes(seqb)

		py = self.pt + self.pc
		pr = self.pa + self.pg
		s1 = self.s1(seqa,seqb)
		s2 = self.s2(seqa,seqb)
		v = self.v(seqa,seqb)

		a1 = -math.log(1 - (py*s1)/(2*self.pt*self.pc) - v/(2*py))
		a2 = -math.log(1 - (py*s1)/(2*self.pa*self.pg) - v/(2*pr))
		b = -math.log(1 - v/(2*py*pr))

		return (2*self.pt*self.pc*(a1 - pr*b))/py + 2*self.pa*self.pg*(a2 - py*b) + 2*py*pr*b

class TN93Model(Model):
	def __init__(self,alpha1 = 0.2, alpha2 = 0.2, beta = 0.4,base_frequency = [0.25]*4):
		Model.__init__(self)

		self.alpha1 = alpha1
		self.alpha2 = alpha2
		self.beta = beta

		self.A = base_frequency[0]
		self.G = base_frequency[1]
		self.C = base_frequency[2]
		self.T = base_frequency[3]


	def divergency(self, a, b):
		return TN93Metric(self.A, self.G, self.C, self.T).divergency(a,b)

	def d1(self,t, a,b,c,d):
		return a + a*b*math.exp(-self.beta * t)/c + d*math.exp(-(c * self.alpha1 + b * self.beta) * t)/c

	def d11(self, t):
		return self.d1(t, self.T, self.A + self.G, self.T + self.C, self.C)

	def d12(self, t):
		return self.d1(t, self.C, self.A + self.G, self.T + self.C, -self.C)

	def d21(self, t):
		return self.d1(t, self.T, self.A + self.G, self.T + self.C, -self.T)

	def d22(self, t):
		return self.d1(t, self.C, self.A + self.G, self.T + self.C, self.T)


	def d3(self,t, a,b,c,d):
		return a + a*b*math.exp(-self.beta * t)/b + d*math.exp(-(b * self.alpha2 + c * self.beta) * t)/b

	def d31(self, t):
		return self.d3(t,self.A, self.T + self.C, self.A + self.G, self.G)

	def d34(self, t):
		return self.d3(t,self.G, self.T + self.C, self.A + self.G, -self.G)


	def d43(self, t):
		return self.d3(t,self.A, self.T + self.C, self.A + self.G, -self.A)

	def d44(self, t):
		return self.d3(t,self.G, self.T + self.C, self.A + self.G, self.A)


	def ad(self, b,t):
		return b*(1 - math.exp(-self.beta * t))

	def aad(self, t):
		return self.ad(self.A, t)

	def gad(self, t):
		return self.ad(self.G, t)

	def tad(self, t):
		return self.ad(self.T, t)

	def cad(self, t):
		return self.ad(self.C, t)

	def codes(self, seq):
		code = 'ACGT'
		return [code.index(b) for b in seq]

	def letters(self, seq):
		letter = ['A','C','G','T']
		return ''.join([letter[int(i)] for i in seq])

	def load(self, data):
		self.matrix = [
			[self.d11, self.d12, self.aad, self.gad],
			[self.d21, self.d22, self.aad, self.gad],
			[self.tad, self.cad, self.d31, self.d34],
			[self.tad, self.cad, self.d43, self.d44]
		]
		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))

	def weight(self, b, t, data = None):
		return [p(t) for p in self.matrix[b]]
