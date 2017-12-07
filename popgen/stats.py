
def count_alleles(pop, ht_no):
	flatten = sorted([a for lst in pop for a in lst])
	s = set(flatten)
	#return [flatten.count(i) for i in range(1,ht_no+1)], len(flatten)
	return [flatten.count(e) for e in s], len(flatten)


def frequency(pop, ht_no):
	v, size = count_alleles(pop, ht_no)
	return [c/size for c in v], v, size

