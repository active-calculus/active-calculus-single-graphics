from figures import *

r = -0.83
def f(n):
    sign = 1
    sum = 0
    for i in range(1,n+1):
        sum += sign
        sign *= r 
    return sum

width = 200
height = 60
beginfigure("8_4_Alternating_Series_Test", 200, 60)

x1 = 1.2
setupcoordinates([5, 5, width-5, height-5],
                 [0, -0.5, x1, 0.3])

x0 = 20
x1 = 9
newpath()
moveto(f(x0), 0)
lineto(f(x1), 0)
stroke()

axes = Axes()
axes.sethticks([f(x0), f(x1)-f(x0), f(x1)])
axes.drawhticks()

Label(r"$a_n$", [(f(x0)+f(x1))/2.0, 0], alignment="cb", offset=[2, 6]).draw()

translate(0, -0.15)
newpath()
moveto(0,0)
lineto(x1,0)
stroke()

def p(n, l):
    sum = f(n)
    gsave()
    p = Point([sum, 0], 2.5, fillcolor=blue)
    p.fill()
    p.draw()

    if l == None:
        l = r"$S_" + str(n) + r"$"
    Label(l, [sum, 0], offset=[0, -5], alignment="ct").draw()
    grestore()

for i in range(1,7):
    p(i, None)

Label(r"$\ldots$", [f(6), 0], offset=[5, -12], alignment="lt").draw()

p(x0, r"$S_{n-1}$")
p(x1, r"$S_{n}$")

endfigure()
