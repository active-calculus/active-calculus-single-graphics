from figures import *
from math import *
margin = 5
width = 250
height = 150

N0 = 20

beginfigure("8_1_Sequence_1overn", width, height)
setupcoordinates([20, 15, width-margin, height-margin],
                 [0, 0, N0, 1])

def sequence(f, n0, n1):
    n = n0
    while n <= n1:
        p = Point([n, f(n)], 2.5, fillcolor=blue)
        p.fill()
        p.draw()
        n+=1
def f(n):
    return 1/float(n)

Grid([0, 2, N0], [0, 0.25, 1], color=lightgray).draw()

mkaxes([0, 2, N0], [0, 0.25, 1])
Label(r"$n$", [N0, 0], alignment="rb", offset=[0,3]).draw()
Label(r"$s_n$", [0,1], alignment="lt", offset=[3,-3]).draw()

sequence(f, 1, N0)

endfigure()
