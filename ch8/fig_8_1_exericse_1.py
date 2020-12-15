from figures import *
from math import *
margin = 5
width = 250
height = 150

beginfigure("8_1_Exercise_1.eps", width, height)
setupcoordinates([20, margin, width-margin, height-margin],
                 [0, -1, 10, 1])

Grid([0,1,10], [-1,0.25,1], color=lightgray).draw()
mkaxes([0, 2, 10], [-1, 0.5, 1])
Label(r"$x$", [10, 0], alignment="rb", offset=[0,3]).draw()

Graph(Function(lambda x: sin(4*x)), N = 400, color=blue).draw()

            



endfigure()
