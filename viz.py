from bokeh.plotting import figure, output_file, show
from bokeh.models import *
from bokeh.layouts import gridplot
import math

num_elements = 0


def main(tree, filename):
    fig_list = compute_figures(tree, filename)

    pre = Div(text='<div style="font-size: 15px ;">Dataset: <i>'+filename+'</i><br>Number of elements: <i>' + str(num_elements)+"</i></div>")

    show(gridplot([[pre], fig_list], sizing_mode='scale_width', merge_tools=True))


def compute_figures(tree, filename):
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
    output_file("HTML/" + filename + ".html")

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
            high=high,
            alpha1=[1] * len(x1),
            alpha2=[0.2] * len(x1)))

    collapse = '''
    parent.postMessage( {'task': 'start'}, '*');
    sel = source.selected.indices[0];
    var d = source.data;
    var collapsed=d['collapsed'][sel];
    d['collapsed'][sel]=!collapsed;
    low=d['low'][sel];
    high=d['high'][sel];
    if(low>-1)
        for (i = low; i <= high; i++) {
            d['alpha1'][i] = +collapsed;
            d['alpha2'][i] = collapsed*0.2;
            d['collapsed'][i]=!collapsed;
        }
    source.selected.indices = [];
    source.change.emit();
    parent.postMessage( {'task': 'stop'}, '*');
    '''

    # dimensions and tools of each fig
    fig_list = [
        figure(
            plot_width=400,
            plot_height=400,
            x_range=(-100, 100),
            y_range=(-100, 100),
            tools=[
                "box_select,lasso_select,reset,wheel_zoom,pan",
                BoxZoomTool(match_aspect=True),
                TapTool(
                    callback=CustomJS(
                        args=dict(source=source),
                        code=collapse)),
                HoverTool(tooltips=[("Name: ",
                                     "@name"), ("Leaves in subtree: ",
                                                "@num_leaves")]),
            ]) for i in range(2)
    ]
    # add circles to visualizations
    fig_list[0].circle(
        'x1',
        'y1',
        radius='radius1',
        fill_color='colors1',
        line_color='colors1',
        alpha='alpha1',
        source=source
        )

    fig_list[1].circle(
        'x2',
        'y2',
        radius='radius2',
        fill_color='red',
        line_color='red',
        alpha='alpha2',
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

    colors1.append("#{:02x}{:02x}{:02x}".format(int(depth * 35),
                                                int(depth * 35),
                                                150))

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