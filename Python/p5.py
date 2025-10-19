from turtle import *
from random import *

speed(50)
bgcolor("black")
for i in range(500):
    colormode(255)
    r=randrange(100,255)
    g=randrange(100,255)
    b=randrange(100,255)
    fd(90+i)
    rt(70)
    pencolor(r,g,b)
done()