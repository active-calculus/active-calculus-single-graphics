from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Ez1Soln", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -4, 2, 4])

grid = Grid([-2, 0.5, 2], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.sethlabels([1, 2, 2])
axes.drawhlabels()

label = Label("$x$", [1.8, -0.4])
label.draw()

def f(x):
    return 0.25*x**4 - 0.333*x**3 - 0.5*x**2 + x - 0.5 

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,2])
graph.draw()

p1 = Point([0,-0.5], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$f$", [1.6, 0.5])
label.draw()

label = Label(r"$(0,-0.25)$", [0, -0.5], alignment = "lt", offset = [4, -4])
label.draw()

restore()


############################################################################

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-2, -4, 2, 4])

grid = Grid([-2, 0.5, 2], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.setlabels([1, 2, 2], # you can do this separately with seth(v)labels
               [2, 2, 3])
axes.drawlabels()

label = Label("$x$", [1.8, 0.2])
label.draw()

def f(x):
    return (x-1)**2 * (x+1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,2])
graph.draw()

label = Label("$f'$", [1.6, 2])
label.draw()

restore()


############################################################################

save()
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-2, -4, 2, 4])

grid = Grid([-2, 0.5, 2], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 2, 2])
axes.drawticks()

axes.sethlabels([1, 2, 2])
axes.drawhlabels()

label = Label("$x$", [1.8, 0.2])
label.draw()

def f(x):
    return 3*x**2 - 2*x - 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,2])
graph.draw()

label = Label("$f''$", [1.6, 2])
label.draw()

restore()


endfigure()
