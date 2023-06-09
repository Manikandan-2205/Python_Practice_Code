from turtle import *
import colorsys as cs
bgcolor('black')
tracer(10)
pensize(3)
h = 0.3

for i in range(300):
    c = cs.hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    up()
    goto(-8, 25)
    fd(i)
    down()
    rt(859)
    fillcolor(c)
    begin_fill()
    circle(15, 320)
    end_fill()
    bk(i/2)
    rt(4)
done()
