#!/usr/bin/env python3

import sys

def newick(tree, distance):
	return tree

def ischild(branches, c):
	for b in branches:
		if c in b[1].keys():
			return True
	return False

def root(branches):
	for b in branches:
		if not ischild(branches, b[0]):
			return b

	return None

def cutoff(root, branches):
	left = []
	for b in branches:
		if b[0] in root[1].keys():
			root[1][b[0]] = b[1]
		else:
			if b[0] != root[0]:
				left.append(b)
	
	return root, left

def tree(root, branches):
	if len(branches):
		root, left = cutoff(root, branches)

		for child in root[1]:
			root[1][child] = tree([child,root[1][child]], left)[1]

	return root

parent = None
branches = []
distance = {}
for line in sys.stdin:
	p,n,d = line.strip().split('\t')

	if p != parent:
		if parent != None:
			branches.append(branch)

		parent = p
		branch = [p, {}]
	
	distance['{}_{}'.format(p,n)] = d
	branch[1][n] = {}

branches.append(branch)

root = root(branches)
t = tree(root, branches)
print( newick({ t[0] : t[1]}, distance) )
