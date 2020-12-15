from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_Ez1_Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -2, 3, 4])

grid = Grid([-3, 0.5, 3], [-2, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 3])
axes.drawticks()

axes.setlabels([-2, 1, 2], # you can do this separately with seth(v)labels
               [-1, 1, 3])
axes.drawlabels()

label = Label(r"$p$", [-2, 2.5])
label.draw()

def f(x):
    return 2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3.5,-1])
graph.draw()

def f(x):
    return x**2 + 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return 2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3.5])
graph.draw()

#thisgraphwidth = 1.25

p1 = Point([-1,3], 2)
p1.setfillcolor(graphcolor)
p1.fill()
p1.draw()

p1 = Point([-1,2], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

restore()

endfigure()
