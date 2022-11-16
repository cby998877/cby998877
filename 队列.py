import time
from turtle import *
g = 0
t = 0
d = ((20,10),
     (-20,10),
     (-20,-10),
     (20,-10))
o = ((10,83-40),(10,-83+40),(-10,-83+40),(-10,83-40))
register_shape('chang2',o)
register_shape('chang',d)
a1 = Turtle()
a2 = Turtle()
a3 = Turtle()
a1.shape('chang')
a2.shape('chang')
a3.shape('chang')
a1.up()
a2.up()
a3.up()
a1.color('red')
a2.color('red')
a3.color('red')
a1.ht()
a2.ht()
a3.ht()
z = [(33,0),(0,0),(-33,0)]
a1.goto(-120,0)
a2.goto(-120,0) 
a3.goto(-120,0)
a1.speed(10)
a1.speed(10)
a1.speed(10)
a = []
n = [a1,a2,a3]
a4 = Turtle()
a5 = Turtle()
a5.up()
a4.up()
a4.shape('chang2')
a5.shape('chang2')
a4.goto(0,40)
a5.goto(0,-40)
def b():
    global g,t
    if g < len(n):
        nowpen = n[g]
        nowpen.showturtle()
        nowpen.goto(z[t%3])
        g = g+1
        t += 1
        a.insert(g,n[g-1])
def f():
    global g,t
    if len(a) != 0:
        nowpen = a[0]
        nowpen.goto(120,0)
        nowpen.ht()
        nowpen.goto(-120,0)
        n.append(nowpen)
        del a[0]
        t -= 1
        if len(a)>=1:
            x1 = a[0].pos()
            x1 = x1[0]
            a[0].goto(x1+33,0)
            if len(a) >= 2:
                x2 = a[1].pos()
                x2=x2[0]
                a[1].goto(x2+33,0)
onkey(b,'Up')
onkey(f,'Down')
listen()
mainloop()
