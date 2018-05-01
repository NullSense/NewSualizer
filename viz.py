from bokeh.plotting import figure, output_file, show
from ete3 import Tree
import math

x = []
y = []
s = []
colors = []

def main(tree):
	global x,y,s
	computeNode(tree,0.0,0.0,50.0,1,0.0)
	# output to static HTML file
	output_file("line.html")

	p = figure(plot_width=400, plot_height=400, x_range=(-100,100),y_range=(-100,100))

	# add a circle renderer with a size, color, and alpha
	p.circle(x, y, radius=s, color=colors, alpha=1)

	# show the results
	show(p)

def computeNode(node,xx,yy, ss, depth,ang):
	global x,y,s,colors
	#x=[1, 2, 3, 4, 5]
	#y=[6, 7, 2, 4, 5]
	#s=[10,20,30,40,50]

	t=2*math.pi if depth==1 else math.pi/1.3

	x.append(xx)
	y.append(yy)
	s.append(ss)
	print(ss)
	colors.append("#{:02x}{:02x}{:02x}".format(int(depth*50),int(depth*50),150))

	m=len(node.children)
	if(m==0):
		return

	for i in range(m):
		angle=(ang-t/2+t*i/m+t/(2*m))
		rad = min(ss*math.sin(t/(2*m)),ss/2)
		computeNode(node.children[i],	\
			xx+math.cos(angle)*ss,		\
			yy+math.sin(angle)*ss,		\
			rad,						\
			depth+1,
			angle)


