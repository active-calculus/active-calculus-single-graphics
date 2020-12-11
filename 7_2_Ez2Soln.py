from figures import *
from defaults import *

width = standardwidth
height = standardheight
margin = 5
beginfigure("7_2_Ez2Soln", width, height)

save()
setupcoordinates([margin, margin, width-margin, height-margin], [-1, -1, 5, 5])

Grid([-1,1,5], [-1,1,5], color=lightgray).draw()

axes = Axes()
axes.draw()
axes.setticks([0,1,4], [0,1,4])
axes.drawticks()
axes.setlabels([0,1,4], [0,1,4])
axes.drawlabels()


Label(r"$t$", [3.9,0], offset=[-3,3], alignment="rb").draw()
Label(r"$y$", [0,4], offset=[3,-3], alignment="lt").draw()

import math

def f(x,y):
    return -0.5*y*(y-1)*(y-3)
field = SlopeField(f, [-0.5,0.5,4.5], [-0.5,0.5,4.5], color = darkmagenta)
field.draw()

restore()
endfigure()
