from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_Ez1Soln", 2*width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -12, 5.5, 12])

grid = Grid([-0.5, 0.5, 5.5], [-12, 2, 12])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,5]) # you can do this in one line with setticks([], [])
axes.setvticks([-10,4,10])
axes.drawticks()

axes.setlabels([0,1,5], # you can do this separately with seth(v)labels
               [-10,4,10])
axes.drawlabels()

label = Label("mph", [0.1,11], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [5.0,0.25], alignment = "lb", offset = [2, 2] )
label.draw()


def f(x):
    return (11/0.05)*x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,0.05])
graph.draw()


def f(x):
    return 11

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.01,0.95])
graph.draw()

def f(x):
    return 11 - (21/0.1)*(x-0.95)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.95,1.05])
graph.draw()

def f(x):
    return -10

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.025,2.95])
graph.draw()

def f(x):
    return -10 + (19/0.1)*(x-2.95)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2.95,3.05])
graph.draw()

def f(x):
    return 9

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([3.025,3.95])
graph.draw()

def f(x):
    return 9 - (9/0.05)*(x-3.95)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([3.95,4])
graph.draw()

label = Label(r"$y = v(t)$", [4, 9], alignment = "lb", offset = [2,2])
label.draw()

restore()

###################################

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.5, -12, 5.5, 12])

grid = Grid([-0.5, 0.5, 5.5], [-12, 2, 12])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,5]) # you can do this in one line with setticks([], [])
axes.setvticks([-10,4,10])
axes.drawticks()

axes.setlabels([0,1,5], # you can do this separately with seth(v)labels
               [-10,4,10])
axes.drawlabels()

label = Label("miles", [0.1,11], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [5.0,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

def f(x):
    return 11*(x-0)+1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1])
graph.draw()

def f(x):
    return -10*(x-1)+12

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3])
graph.draw()

def f(x):
    return 9*(x-3)-8

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([3,4])
graph.draw()

label = Label(r"$y = s(t)$", [2, 4], alignment = "lb", offset = [2,2])
label.draw()

point = Point([0, 1], 2)
point.setfillcolor(red)
point.fill()
point.draw()

label = Label(r"$(0,s(0))$", [0,1], alignment = "lc", offset = [4, 2] )
label.draw()

point = Point([1, 12], 2)
point.setfillcolor(red)
point.fill()
point.draw()

label = Label(r"$(1,s(1))$", [1,12], alignment = "lt", offset = [6, -1] )
label.draw()

point = Point([3, -8], 2)
point.setfillcolor(red)
point.fill()
point.draw()

label = Label(r"$(3,s(3))$", [3,-8], alignment = "lb", offset = [6, 2] )
label.draw()

point = Point([4, 1], 2)
point.setfillcolor(red)
point.fill()
point.draw()

label = Label(r"$(4,s(4))$", [4,1], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
