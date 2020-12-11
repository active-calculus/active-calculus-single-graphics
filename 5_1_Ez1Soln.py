from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("5_1_Ez1Soln", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -3.5, 6.5, 3.5])

grid = Grid([-0.5, 0.5, 6.5], [-3.5, 0.5, 3.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 6]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([1, 5, 6], # you can do this separately with seth(v)labels
               [-3, 3, 3])
axes.drawlabels()


label = Label("$f$", [-3.2, 5.3])
label.draw()

f = Function(lambda x: -2 + 0.5*(x-3)**2)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0,1])
area.fill()
area.draw()

f = Function(lambda x: -2 + 0.5*(x-3)**2)

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[1,3])
area.fill()
area.draw()

def f(x):
    return -2 + 0.5*(x-3)**2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,6])
graph.draw()

label = Label("$v$", [5.5, 2], alignment = "rb", offset = [-2,2])
label.draw()

label = Label("$A_1$", [0.3, 0.7], alignment = "cc", offset = [0,0])
label.draw()

label = Label("$A_2$", [2.2, -0.8], alignment = "cc", offset = [0,0])
label.draw()

label = Label("$t$", [6, 0.4], alignment = "cc", offset = [0,0])
label.draw()

restore()

###

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.5, -3.5, 6.5, 3.5])

grid = Grid([-0.5, 0.5, 6.5], [-3.5, 0.5, 3.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 6]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([0, 2, 6], # you can do this separately with seth(v)labels
               [-3, 2, 3])
axes.drawlabels()

def f(x):
    return -2*x + 0.16667*(x-3)**3 + 5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,6])
graph.draw()

point = Point([1, f(1)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

point = Point([3, f(3)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

point = Point([5, f(5)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

point = Point([6, f(6)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

label = Label("$(1, 5/3)$", [1, 1.667], alignment = "cb", offset = [0,2])
label.draw()

label = Label("$(3, -1)$", [3, -1], alignment = "rt", offset = [2,2])
label.draw()

label = Label("$t$", [6, 0.4], alignment = "cc", offset = [0,0])
label.draw()

label = Label("$s$", [2, 1], alignment = "lb", offset = [2,2])
label.draw()


restore()

endfigure()
