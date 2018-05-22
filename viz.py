from bokeh.plotting import figure, output_file, show
from bokeh.models import *
from bokeh.layouts import gridplot
import math

num_elements = 0


def main(tree):
    fig_list = compute_figures(tree)

    pre = PreText(text="Number of elements: " + str(num_elements))

    show(gridplot([[pre], fig_list]))


def compute_figures(tree):
    # These store the layout of the first visualisation
    x1 = []
    y1 = []
    radius1 = []  # size of circles
    colors1 = []
    name = []
    num_leaves = []
    num_elements = 0  # number of elements in the whole tree
    low = []
    high = []
    # Compute the layout of both visualisations
    compute_visualization1(tree, x1, y1, radius1, colors1, name, num_leaves,
                           0.0, 0.0, 50.0, 1, 0.0, low, high)

    # These store the layout of the second visualisation
    x2 = []
    y2 = []
    radius2 = []  # size of circles
    compute_visualization2(tree, x2, y2, radius2, 0.0, 0.0, 80.0, 1)

    # output to static HTML file
    output_file("line.html")

    source = ColumnDataSource(
        data=dict(
            x1=x1,
            y1=y1,
            radius1=radius1,
            x2=x2,
            y2=y2,
            radius2=radius2,
            colors1=colors1,
            collapsed=[False] * len(x1),
            name=name,
            num_leaves=num_leaves,
            low=low,
            high=high))
    fil = BooleanFilter([True] * len(x1))
    view1 = CDSView(source=source, filters=[fil])
    view2 = CDSView(source=source, filters=[fil])

    collapse = '''
    sel = source.selected.indices[0];

    var d = source.data;
    var collapsed=d['collapsed'][sel];
    d['collapsed'][sel]=!collapsed;
    low=d['low'][sel];
    high=d['high'][sel];

    if(low>-1)
        for (i = low; i <= high; i++) {
            fil.booleans[i] = collapsed;
            d['collapsed'][i]=!collapsed;
        }

    view1.filters[0] = fil;
    view2.filters[0] = fil;
    source.change.emit();
    '''

    # tools for each fig
    tools = [
        BoxZoomTool(match_aspect=True),
        # TODO: Disable wheel axis zoom
        WheelZoomTool(),
        LassoSelectTool(),
        BoxSelectTool(),
        ResetTool(),
        PanTool(),
        TapTool(callback=CustomJS(
                args=dict(source=source, fil=fil, view1=view1, view2=view2),
                code=collapse)),
        HoverTool(tooltips=[("Name: ", "@name"), ("Leaves in subtree: ",
                                                  "@num_leaves")])
    ]

    # dimensions and tools of each fig
    fig_list = [
        figure(
            plot_width=500,
            plot_height=500,
            x_range=(-100, 100),
            y_range=(-100, 100),
            tools=[
                BoxZoomTool(match_aspect=True),
                # TODO: Disable wheel axis zoom
                WheelZoomTool(),
                LassoSelectTool(),
                BoxSelectTool(),
                ResetTool(),
                PanTool(),
                TapTool(callback=CustomJS(
                    args=dict(source=source, fil=fil,
                              view1=view1, view2=view2),
                    code=collapse)),
                HoverTool(tooltips=[("Name: ", "@name"), ("Leaves in subtree: ",
                                                          "@num_leaves")])
            ],
            toolbar_location="left" if i == 0 else "right") for i in range(2)
    ]

    # add circles to visualizations
    fig_list[0].circle(
        'x1',
        'y1',
        radius='radius1',
        fill_color='colors1',
        line_color='colors1',
        alpha=1,
        source=source
        )

    fig_list[1].circle(
        'x2',
        'y2',
        radius='radius2',
        fill_color='red',
        line_color='red',
        alpha=0.1,
        source=source)

    # Remove grid lines
    fig_list[0].xgrid.visible = False
    fig_list[0].ygrid.visible = False

    fig_list[1].xgrid.visible = False
    fig_list[1].ygrid.visible = False

    return fig_list


# Filters for optimization
def compute_filters(r1, r2):
    radii = [1, 0.2, 0.04]
    opt_filters = []
    for j in range(len(radii)):
        opt_filters.extend([IndexFilter(indices=[]) for i in range(2)])
        for i in range(len(r1)):
            if(r1[i] > radii[j]):
                opt_filters[j * 2].indices.append(i)
            if(r2[i] > radii[j]):
                opt_filters[j * 2 + 1].indices.append(i)
    return opt_filters


# Computes the layout of the first visualisation
def compute_visualization1(node, x1, y1, radius1, colors1, name, num_leaves,
                           xx, yy, size, depth, ang, low, high):
    global num_elements
    num_elements += 1

    t = 2 * math.pi if depth == 1 else math.pi / 1.3

    index = len(x1)

    x1.append(xx)
    y1.append(yy)
    radius1.append(size)
    name.append('unnamed' if node.name == '' else node.name)
    num_leaves.append(len(node))

    colors1.append("#{:02x}{:02x}{:02x}".format(
        230, int(depth * 40) % 230, 10))

    m = len(node.children)
    if (m == 0):
        low.append(-1)
        high.append(-1)
        return

    low.append(index + 1)
    high.append(0)

    for i in range(m):
        angle = (ang - t / 2 + t * i / m + t / (2 * m))

        radius = min(size * math.sin(t / (2 * m)), size / 2)
        compute_visualization1(node.children[i], x1, y1, radius1, colors1,
                               name, num_leaves, xx +
                               math.cos(angle) * size,
                               yy +
                               math.sin(
            angle) * size, radius, depth + 1,
            angle, low, high)
    high[index] = len(x1) - 1


# Computes the layout of second visualisation
def compute_visualization2(node, x2, y2, radius2, xx, yy, size, depth):
    x2.append(xx)
    y2.append(yy)
    radius2.append(size)

    m = len(node.children)
    if (m == 0):
        return

    for i in range(m):
        angle = i * 2 * math.pi / m
        radius = (math.sin(math.pi / m) * size) / (1 + math.sin(math.pi / m))
        compute_visualization2(node.children[i], x2, y2, radius2,
                               xx + math.cos(angle) * (size - radius),
                               yy + math.sin(angle) * (size - radius), radius,
                               depth + 1)
