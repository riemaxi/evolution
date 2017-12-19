from model import *
import math

class HKYModel(Model):
	def __init__(self, alpha = 0.5, beta = 0.5, base_frequency = [0.25]*4):
		Model.__init__(self)

		self.alpha = alpha
		self.beta = beta
		self.A = base_frequency[0]		
		self.C = base_frequency[1]
		self.G = base_frequency[2]
		self.T = base_frequency[3]

	def t0(self,t, f):
		return f*(1 - math.exp(-self.beta * t))

	def t1(self,t,f):
		return f[0] + ((f[1]*(f[2] + f[3]))/(f[4]+f[5]))*math.exp(-self.beta * t)

	def t2(self,t,f):
		return (f[0]/(f[1]+f[2]))*math.exp(-((f[3] + f[4])*self.alpha + (f[5] + f[6])*self.beta) * t)

	def h(self, t):
		return 1 - self.i(t) - self.p(t) - self.q(t)

	def i(self, t):
		return self.t1(t,[self.C,self.C,self.A,self.G,self.T,self.C] ) - self.t2(t,[self.C,self.T,self.C,self.T,self.C,self.A,self.G])		

	def j(self, t):
		return self.t1(t,[self.T,self.T,self.A,self.G,self.T,self.C] ) - self.t2(t,[self.C,self.T,self.C,self.T,self.C,self.A,self.G])

	def k(self, t):
		return 1 - self.j(t) - self.p(t) -self.q(t)

	def l(self, t):
		return 1 - self.r(t) - self.s(t) - self.m(t)

	def m(self, t):
		return self.t1(t,[self.G,self.G,self.T,self.C,self.A,self.G] ) - self.t2(t,[self.G,self.A,self.G,self.A,self.G,self.T,self.C])

	def n(self, t):
		return self.t1(t,[self.A,self.A,self.T,self.C,self.A,self.G] ) - self.t2(t,[self.G,self.A,self.G,self.A,self.G,self.T,self.C])

	def o(self, t):
		return 1 - self.r(t) - self.s(t) - self.n(t)

	def p(self, t):
		return self.t0(self.A,t)

	def q(self, t):
		return self.t0(self.G,t)

	def r(self, t):
		return self.t0(self.T,t)

	def s(self, t):
		return self.t0(self.C,t)


	def load(self,data):
		self.matrix = [
			[self.h, self.i, self.p, self.q],
			[self.j, self.k, self.p, self.q],
			[self.r, self.s, self.l, self.m],
			[self.r, self.s, self.n, self.o]
		]

		self.size = len(self.matrix[0])
		self.bases = list(range(self.size))


	def codes(self, seq):
		code = 'ACGT'
		return [code.index(b) for b in seq]

	def letters(self, seq):
		letter = ['A','C','G','T']
		return ''.join([letter[int(i)] for i in seq])


	def weight(self, base, t, data = None):
		return [p(t) for p in self.matrix[base]]
