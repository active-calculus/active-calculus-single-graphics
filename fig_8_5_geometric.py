from figures import *
from math import *

width = 120
height = 120
margin = 5

def func(x):
    return 1/(1-x)

def taylor(x, n):
    sum = 0
    term = 1
    for i in range(n+1):
        sum += term
        term *= x
    return sum

x0 = 1.5
def fig():
    filename = "8_5_1over1minusx_graphs"
    beginfigure(filename, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],\
                     [-x0, -2, x0, 10])

    Grid([-x0,0.5, x0], [-2, 2, 10], color=lightgray).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-2,1,2], [-2, 2, 10])
    axes.setlabels([-2,1,2], [-2, 2, 10])
    axes.drawticks()
    axes.drawlabels()
    mklabels(x0, r"$x$", 10, r"$y$")

    cliptoboundingbox()

    colors = [blue, magenta, lightorange, green, magenta]
    nvalues = [5, 9, 11, 20]
    
    for i in range(3):
        n = nvalues[i]
        color = colors[i]
        Graph(Function(lambda x: taylor(x,n)), color=color).draw()

    Graph(Function(func), color=red, domain=[-x0, 0.999]).draw()
    Graph(Function(func), color=red, domain=[1.001, x0]).draw()

    endfigure()

fig()

    
