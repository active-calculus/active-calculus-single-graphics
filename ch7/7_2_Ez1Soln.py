from figures import *
from defaults import *

width = standardwidth
height = standardheight
margin = 5
beginfigure("7_2_Ez1Soln", width, height)

save()
setupcoordinates([margin, margin, width-margin, height-margin], [-4, -4, 4, 4])

Grid([-4,1,4], [-4,1,4], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([-3,1,3], [-3,1,3])
axes.drawticks()
axes.setlabels([-3,1,3], [-3,1,3])
axes.drawlabels()


Label(r"$t$", [3.9,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,4], offset=[3,-3], alignment="lt").draw()

import math
save()
cliptoboundingbox()
C = -4
while C <= 4:
    graph = Graph(Function(lambda x: x-1 + C*math.exp(-x)), 
                  color = graphcolor)
    graph.draw()
    C += 1
restore()

def f(x,y):
    return x-y
field = SlopeField(f, [-3,1,3], [-3,1,3], color = darkmagenta)
field.draw()


restore()
endfigure()
