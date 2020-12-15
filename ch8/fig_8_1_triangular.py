from figures import *
from math import *
margin = 5
width = 140 + 2*margin
height = (int) (140*sqrt(3)/2) + 2*margin

beginfigure("8_1_Triangular_Numbers.eps", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0, 0, 4, 4*sin(pi/3)])

def dot(p):
    p = Point(p, 2.5)
    p.fill()

def row(N):
    gsave()
    newpath()
    moveto(0,0)
    lineto(N,0)
    stroke()
    for i in range(N+1):
        dot([0,0])
        translate(1,0)
    grestore()

newpath()
moveto(0,0)
lineto(4, 0)
lineto(4*cos(pi/3), 4*sin(pi/3))
closepath()
stroke()

gsave()
for j in range(5):
    N = 4-j
    row(N)
    translate(cos(pi/3), sin(pi/3))
grestore()


            



endfigure()
