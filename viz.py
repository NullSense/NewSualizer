from bokeh.plotting import figure, output_file, show
from bokeh.models import *
from bokeh.layouts import gridplot
import math

# These store the layout of the first visualisation
x1 = []
y1 = []
s1 = []  # size of circles
colors1 = []
name = []
n_leaves = []

# These store the layout of the second visualisation
x2 = []
y2 = []
s2 = []  # size of circles
colors2 = []


def main(tree):
    # Compute the layout of both visualisations
    computeNode1(tree, 0.0, 0.0, 50.0, 1, 0.0)
    computeNode2(tree, 0.0, 0.0, 80.0, 1)

    # output to static HTML file
    output_file("line.html")

    source = ColumnDataSource(
        data=dict(x1=x1, y1=y1, s1=s1, x2=x2, y2=y2, s2=s2, colors1=colors1, name=name, n_leaves=n_leaves))

    # tools for each fig
    tools = [
        BoxZoomTool(match_aspect=True),
        # TODO: Disable wheel axis zoom
        WheelZoomTool(),
        LassoSelectTool(),
        BoxSelectTool(),
        ResetTool(),
        PanTool(),
        TapTool(),
        HoverTool(tooltips=[("Name: ", "@name"), ("Radius: ", "@s2"), ("Leaves in subtree: ", "@n_leaves")])
    ]

    # dimensions and tools of each fig
    fig_list = [
        figure(
            plot_width=800,
            plot_height=800,
            x_range=(-100, 100),
            y_range=(-100, 100),
            tools=tools) for i in range(2)
    ]

    # add circles to visualizations
    fig_list[0].circle(
        'x1',
        'y1',
        radius='s1',
        fill_color='colors1',
        line_color='colors1',
        alpha=1,
        source=source)

    fig_list[1].circle(
        'x2',
        'y2',
        radius='s2',
        fill_color='red',
        line_color='red',
        alpha=0.1,
        source=source)

    show(gridplot([fig_list]))


# Computes the layout of the first visualisation
def computeNode1(node, xx, yy, size, depth, ang):
    t = 2 * math.pi if depth == 1 else math.pi / 1.3

    x1.append(xx)
    y1.append(yy)
    s1.append(size)
    name.append('unnamed' if node.name == '' else node.name)
    n_leaves.append(len(node))

    colors1.append("#{:02x}{:02x}{:02x}".format(
        int(depth * 50), int(depth * 50), 150))

    m = len(node.children)
    if (m == 0):
        return

    for i in range(m):
        angle = (ang - t / 2 + t * i / m + t / (2 * m))

        radius = min(size * math.sin(t / (2 * m)), size / 2)
        computeNode1(node.children[i], xx + math.cos(angle) * size,
                     yy + math.sin(angle) * size, radius, depth + 1, angle)


# Computes the layout of second visualisation
def computeNode2(node, xx, yy, size, depth):
    x2.append(xx)
    y2.append(yy)
    s2.append(size)

    m = len(node.children)
    if (m == 0):
        return

    for i in range(m):
        angle = i * 2 * math.pi / m
        radius = (math.sin(math.pi / m) * size) / (1 + math.sin(math.pi / m))
        computeNode2(node.children[i], xx + math.cos(angle) * (size - radius),
                     yy + math.sin(angle) * (size - radius), radius, depth + 1)
