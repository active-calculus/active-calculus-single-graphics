from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_8_Ez1Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0.5, -2.5, 5.5, 2.5])

grid = Grid([0.5, 0.5, 5.5], [-2.5, 0.5, 2.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1, 1, 5]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 1, 2])
axes.drawticks()


axes.setlabels([1, 1, 5], # you can do this separately with seth(v)labels
               [-2, 1, 2])
axes.drawlabels()

def f(x):
    return -1*(x-3)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([0.5,5.5])
graph.draw()

def f(x):
    return 0.5*(x-3)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([0.5,5.5])
graph.draw()

a = 3
dx = 1.4
cliptoboundingbox()
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(darkgreen)
tangent.draw()

p1 = Point([3,0], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$f$", [3,-1], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$g$", [3,0.5], alignment = "lb", offset = [2, 2])
label.draw()

restore()

endfigure()
