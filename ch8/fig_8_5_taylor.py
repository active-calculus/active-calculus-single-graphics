from figures import *
from math import *

width = 120
height = 120
margin = 5

def func(x):
    return sin(x)

def taylor(x, n):
    sum = 0
    sign = 1
    den = 1
    term = x
    for i in range(n+1):
        sum += term
        term *= -x*x/float(2*(i+1)*(2*i+3))
    return sum

x0 = 5
y0 = 3
def fig(n):
    m = 2*n + 1
    filename = "8_5_Taylor"+str(m)
    beginfigure(filename, width, height)
    setupcoordinates([margin, margin, width-margin, height-margin],\
                     [-x0, -y0, x0, y0])

#    Grid([-x0, 1, x0], [-y0, 1, y0], color=lightgray).draw()
    mkaxes([-4, 2, 4], [-y0, 1, y0])
    mklabels(x0, r"$x$", y0, r"$y$")

    cliptoboundingbox()

    Graph(Function(func), color=red).draw()

    colors = [blue, magenta, lightorange, green, magenta]

    Graph(Function(lambda x: taylor(x,n)), color=colors[n]).draw()

    endfigure()

for i in range(5):
    fig(i)

    
