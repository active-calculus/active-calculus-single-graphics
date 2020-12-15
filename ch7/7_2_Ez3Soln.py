from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("7_2_Ez3Soln", width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 7, 10])

grid = Grid([-1, 1, 7], [-1, 1, 10])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 7])
axes.setvticks([-1, 1, 9])
axes.drawticks()

axes.setlabels([0, 3, 3], [0, 3, 9])
axes.drawlabels()

label = Label("$P$", [6.5, 0.3])
label.draw()

label = Label("$dP/dt$", [0.2, 9])
label.draw()

#label = Label("$f$", [4, 4])
#label.draw()

def f(x):
    return x*(6-x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,7])
graph.draw()

def f(x):
    return x*(6-x)-1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkgreen)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,7])
graph.draw()

restore()

endfigure()
