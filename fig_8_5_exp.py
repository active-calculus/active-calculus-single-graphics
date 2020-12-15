from figures import *
from math import *

width = 150
height = 120
margin = 5

def func(x):
    return exp(x)

def taylor(x, n):
    sum = 0
    term = 1
    for i in range(n+1):
        sum += term
        term *= x/float(i+1)
    return sum

x0 = 3
y0 = 15
def fig():
    filename = "8_5_exp_graphs"
    beginfigure(filename, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],\
                     [-x0, -3, x0, y0])

    Grid([-x0, 1, x0], [-3, 3, y0], color=lightgray).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-x0, 1, x0], [-3, 3, y0])
    axes.setlabels([-x0, 1, x0], [-3, 3, y0])
    axes.drawticks()
    axes.drawlabels()
    mklabels(x0, r"$x$", y0, r"$y$")

    cliptoboundingbox()

    colors = [magenta, blue, green, lightorange, green, magenta]
    nvalues = [3, 4, 5, 14, 20]
    
    for i in range(3):
        n = nvalues[i]
        color = colors[i]
        Graph(Function(lambda x: taylor(x,n)), color=color, N = 200).draw()

    Graph(Function(func), color=red, N = 200).draw()

    endfigure()

fig()

    
