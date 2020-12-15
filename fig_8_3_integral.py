from figures import *
from math import *
margin = 5
width = 250
height = 150

N0 = 10

def sequence(f, n0, n1):
    n = n0
    while n <= n1:
        p = Point([n, f(n)], 2.5, fillcolor=blue)
        p.fill()
        p.draw()
        n+=1

def f(n):
     return 1.0/n

def fig(mode):
    filename = "8_3_Integral_test"
    if mode == 0:
        filename = filename + "1"
    else:
        filename = filename + "2"
    beginfigure(filename, width, height)
    setupcoordinates([20, 15, width-margin, height-margin],
                     [1, 0, N0, 1])
    
    Grid([1, 1, N0], [0, 0.25, 1], color=lightgray).draw()

    newpath()
    axes = Axes(frame="lb")
    rx = [0,1,N0]
    ry = [0, 0.25, 1]
    axes.draw()
    axes.setticks(rx, ry)
    axes.setlabels(rx, ry)
    axes.drawticks()
    axes.drawlabels()

    if mode == 0:
        style = RiemannSum.LEFT
    else:
        style = RiemannSum.RIGHT
    rs = RiemannSum(Function(f), 9, fillcolor=lightgreen, style = style)
    rs.fill()
    rs.draw()

    Graph(Function(f)).draw()

    sequence(f, 1, N0)
    
    Label(r"$k$", [N0, 0], alignment="rb", offset=[0,3]).draw()
    Label(r"$a_k$", [1,1], alignment="lt", offset=[5,-2]).draw()
    
    endfigure()
    

fig(0)
fig(1)
