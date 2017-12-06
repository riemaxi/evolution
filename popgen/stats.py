
def count_alleles(pop, ht_no):
	flatten = [a for lst in pop for a in lst]
	return [flatten.count(i) for i in range(1,ht_no+1)], len(flatten)


def frequency(pop, ht_no):
	v, size = count_alleles(pop, ht_no)
	return [c/size for c in v]

