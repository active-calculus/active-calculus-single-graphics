from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_8_Ez1Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [1.5, -2.5, 4.5, 0.5])

grid = Grid([1.5, 0.5, 4.5], [-2.5, 0.5, 0.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([2, 1, 4]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 1, 0])
axes.drawticks()

axes.setlabels([2, 1, 4], # you can do this separately with seth(v)labels
               [-2, 1, 0])
axes.drawlabels()

def f(x):
    return 2*(x - 3)*((x - 3)**2 - 1) - 1

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,4.5])
graph.draw()


def f(x):
    return -2*x + 5

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,4.5])
graph.draw()

point = Point([3, -1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

label = Label(r"$y = p(x)$", [2,-1], alignment = "rb", offset = [-2, 2]  )
label.draw()

label = Label(r"$y = L(x)$", [3.25,-2], alignment = "rb", offset = [2, 2]  )
label.draw()

label = Label(r"$(3,-1)$", [3,-1], alignment = "rb", offset = [-4, 4]  )
label.draw()


restore()

endfigure()
