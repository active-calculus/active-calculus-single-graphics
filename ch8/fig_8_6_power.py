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
    for i in range(1, n+1):
        sum += x**(i)/float(i*i)
    return sum

x0 = 2
y0 = 10
def fig():
    filename = "8_6_Power_Series"
    beginfigure(filename, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],\
                     [-x0, -y0, x0, y0])

    Grid([-x0, 0.5, x0], [-y0, 2.5, y0], color=lightgray).draw()

    axes = Axes()
    axes.draw()
    axes.setticks([-x0, 1, x0], [-y0, 5, y0])
    axes.setlabels([-x0, 1, x0], [-y0, 5, y0])
    axes.drawticks()
    axes.drawlabels()
    mklabels(x0, r"$x$", y0, r"$y$")

    cliptoboundingbox()

    colors = [red, blue, green]
    nvalues = [10, 25, 50]
    
    for i in range(3):
        n = nvalues[i]
        color = colors[i]
        Graph(Function(lambda x: taylor(x,n)), color=color, N = 200).draw()

#    Graph(Function(func), color=red, N = 200).draw()

    endfigure()

fig()

    
