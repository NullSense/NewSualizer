from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from ete3 import Tree
import math

x = []
y = []
s = []
colors = []
x2 = []
y2 = []
s2 = []
colors2 = []


def main(tree):
    global x, y, s
    computeNode1(tree, 0.0, 0.0, 50.0, 1, 0.0)
    computeNode2(tree, 0.0, 0.0, 80.0, 1)
    # output to static HTML file
    output_file("line.html")

    left = figure(plot_width=400, plot_height=400,
               x_range=(-100, 100), y_range=(-100, 100))

    # add a circle renderer with a size, color, and alpha
    left.circle(x, y, radius=s, color=colors, alpha=1)

    right = figure(plot_width=400, plot_height=400,
               x_range=(-100, 100), y_range=(-100, 100))

    # add a circle renderer with a size, color, and alpha
    right.circle(x2, y2, radius=s2, color="red", alpha=0.1)

    # show the results
    p=gridplot([[left,right]])
    show(p)


def computeNode1(node, xx, yy, ss, depth, ang):
    global x, y, s, colors

    t = 2 * math.pi if depth == 1 else math.pi / 1.3

    x.append(xx)
    y.append(yy)
    s.append(ss)

    colors.append("#{:02x}{:02x}{:02x}".format(
        int(depth * 50),
        int(depth * 50),
        150))

    m = len(node.children)
    if(m == 0):
        return

    for i in range(m):
        angle = (ang - t / 2 + t * i / m + t / (2 * m))
        rad = min(ss * math.sin(t / (2 * m)), ss / 2)
        computeNode1(node.children[i],
                     xx + math.cos(angle) * ss,
                     yy + math.sin(angle) * ss,
                     rad,
                     depth + 1,
                     angle)


def computeNode2(node, xx, yy, ss, depth):
    global x2, y2, s2, colors2

    x2.append(xx)
    y2.append(yy)
    s2.append(ss)

    # colors.append("#{:02x}{:02x}{:02x}".format(
    #    int(depth * 50),
    #    int(depth * 50),
    #    150))

    m = len(node.children)
    if(m == 0):
        return

    for i in range(m):
        angle = i * 2 * math.pi / m
        rad = (math.sin(math.pi / m) * ss) / (1 + math.sin(math.pi / m))
        computeNode2(node.children[i],
                     xx + math.cos(angle) * (ss-rad),
                     yy + math.sin(angle) * (ss-rad),
                     rad,
                     depth + 1)
