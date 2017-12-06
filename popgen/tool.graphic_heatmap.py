#!/usr/bin/env python3

import sys
import math

TITLE = 'evolution heatmap'
SCALE_SIZE = 200
GAUSS_WIDTH = 20

R_SHIFT = 0
G_SHIFT = 0
B_SHIFT = 0

def gauss(x, u,xscale, yscale = 255):
	x = xscale*x - 10
	return int(yscale * math.exp(-math.pow(x-u,2)/16))

def colorscale(size = 10):
	xscale = GAUSS_WIDTH/size
	result = []
	for i in range(size):
		r = gauss(i,R_SHIFT,xscale)
		g = gauss(i,G_SHIFT,xscale)
		b = gauss(i,B_SHIFT, xscale)
		result.append('<tr><td width="50" bgcolor="#{:02x}{:02x}{:02x}"></td></tr>'.format(r,g,b))

	return '<table cellspacing="0" cellpadding="0" height="500">\n{}\n</table>'.format('\n'.join(result))

def getcolor(score, mns, mxs, size = 10):
	xscale = GAUSS_WIDTH/size

	if score <= mxs:
		if score >= mns:
			i = (score + abs(mns))*size/(mxs - mns)

			r = gauss(i,R_SHIFT,xscale)
			g = gauss(i,G_SHIFT,xscale)
			b = gauss(i,B_SHIFT, xscale)

			return '#{:02x}{:02x}{:02x}'.format(r,g,b)
		else:
			return '#fffffe'
	else:
		return '#ffffff'

def positive_real(r):
	return r if r != 0.0 else abs(r)

def scorescale(mns, mxs, size):
	step = (mxs -  mns)/10
	data = ''.join(['<tr><td>{:.2f}</td></tr>'.format(positive_real(mns + i*step)) for i in range(11)])
	return '<table height="500">{}</table>'.format(data)

def heatmap(columns, minscore, maxscore, size):
	data = ['<table cellspacing="0" cellpassing="0" height="500">',
		''.join(['<td width="60" align="center">{}</td>'.format(c) for c in columns])]
	for line in sys.stdin:
		line = line.strip('\n').split('\t')
		scores = [float(s) for s in line[1:]]
		data.append('<tr>\n<td>{}</td>'.format(line[0]) + ''.join(['<td bgcolor="{}"></td>'.format(getcolor(score,minscore, maxscore, size)) for score in scores]) + '</tr>')
	
	data.append('</table>')

	return '\n'.join(data)


def html(columns, minscore, maxscore, size, title):
	templ = open('template.heatmap.html').read()

	templ = templ.replace('_DS_TITLE_DS_', title)
	templ = templ.replace('_DS_HEATMAP_DS_', heatmap(columns, minscore, maxscore, size))

	return templ


minscore, maxscore = [0.2,1.0]

columns = next(sys.stdin).strip('\n').split('\t')

print( html(columns, minscore, maxscore, SCALE_SIZE, TITLE) )
