from bokeh.plotting import figure, output_file, show
from ete3 import Tree
import math

x = []
y = []
s = []
t = 0.0

def main(tree):
	global x,y,s, t
	t=math.pi
	computeNode(tree,0,0,50)
	# output to static HTML file
	output_file("line.html")

	p = figure(plot_width=400, plot_height=400)

	# add a circle renderer with a size, color, and alpha
	p.circle(x, y, radius=s, color="navy", alpha=0.5)

	# show the results
	show(p)

def computeNode(node,xx,yy, ss):
	global x,y,s
	#x=[1, 2, 3, 4, 5]
	#y=[6, 7, 2, 4, 5]
	#s=[10,20,30,40,50]

	x.append(xx)
	y.append(yy)
	s.append(ss)

	m=len(node.children)
	if(m==0):
		return

	for i in range(m):
		angle=math.pi-t/2+t*i/m+t/(2*m)
		rad = ss/m
		computeNode(node.children[i],xx+math.cos(angle)*rad,yy+math.sin(angle)*rad,rad)


