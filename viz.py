from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from ete3 import Tree
import math

#These store the layout of the first visualisation
x = []
y = []
s = []      #size of circles
colors = []

#These store the layout of the second visualisation
x2 = []
y2 = []
s2 = []     #size of circles
colors2 = []


def main(tree):
    #Compute the layout of both visualisations
    computeNode1(tree, 0.0, 0.0, 50.0, 1, 0.0)
    computeNode2(tree, 0.0, 0.0, 80.0, 1)

    # output to static HTML file
    output_file("line.html")

    #left figure for the first visualization
    left = figure(plot_width=400, plot_height=400,
               x_range=(-100, 100), y_range=(-100, 100))
    #add circles for first visualization
    left.circle(x, y, radius=s, color=colors, alpha=1)

    #right figure for second visualisation
    right = figure(plot_width=400, plot_height=400,
               x_range=(-100, 100), y_range=(-100, 100))
    # add circles for second visualisation
    right.circle(x2, y2, radius=s2, color="red", alpha=0.1)

    # show the results
    plot=gridplot([[left,right]])
    show(plot)

#Computes the layout of the first visualisation
def computeNode1(node, xx, yy, size, depth, ang):
    global x, y, s, colors

    t = 2 * math.pi if depth == 1 else math.pi / 1.3

    x.append(xx)
    y.append(yy)
    s.append(size)

    colors.append("#{:02x}{:02x}{:02x}".format(
        int(depth * 50),
        int(depth * 50),
        150))

    m = len(node.children)
    if(m == 0):
        return

    for i in range(m):
        angle = (ang - t / 2 + t * i / m + t / (2 * m))
        radius = min(size * math.sin(t / (2 * m)), size / 2)
        computeNode1(node.children[i],
                     xx + math.cos(angle) * size,
                     yy + math.sin(angle) * size,
                     radius,
                     depth + 1,
                     angle)

#Computes the layout of second visualisation
def computeNode2(node, xx, yy, size, depth):
    global x2, y2, s2, colors2

    x2.append(xx)
    y2.append(yy)
    s2.append(size)

    m = len(node.children)
    if(m == 0):
        return

    for i in range(m):
        angle = i * 2 * math.pi / m
        radius = (math.sin(math.pi / m) * size) / (1 + math.sin(math.pi / m))
        computeNode2(node.children[i],
                     xx + math.cos(angle) * (size-radius),
                     yy + math.sin(angle) * (size-radius),
                     radius,
                     depth + 1)
