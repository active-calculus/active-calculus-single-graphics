from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_6_Ez4Soln", width, height)

margin = 20
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 1, 4], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$y = f(x)$", [1,-2])
label.draw()

label = Label(r"$y = f^{-1}(x)$", [-4,1])
label.draw()

def f(x):
    return x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(gray)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,4])
graph.draw()

def f(x):
    return 2*math.atan(x-1) - 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,4])
graph.draw()

a = 1
dx = 1
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

def f(x):
    return math.tan((x+1)/2) + 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-3.75,2])
graph.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-1, f(-1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([-3, f(-3)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([f(1),1], 2)
point.setfillcolor(darkred)
point.fill()
point.draw()

point = Point([f(-1),-1], 2)
point.setfillcolor(darkred)
point.fill()
point.draw()

point = Point([f(-3),-3], 2)
point.setfillcolor(darkred)
point.fill()
point.draw()

restore()

endfigure()
