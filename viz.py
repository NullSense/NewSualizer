from bokeh.plotting import figure, output_file, show
from ete3 import Tree

x = []
y = []
size = []

def main(tree):
	global x,y,size
	computeNode(tree)
	# output to static HTML file
	output_file("line.html")

	p = figure(plot_width=400, plot_height=400)

	# add a circle renderer with a size, color, and alpha
	p.circle(x, y, size=size, color="navy", alpha=0.5)

	# show the results
	show(p)

def computeNode(node,xx,yy):
	global x,y,size
	x=[1, 2, 3, 4, 5]
	y=[6, 7, 2, 4, 5]
	size=[10,20,30,40,50]

	for child in 
