import turtle as t
import queen_class
SIZE=30
t.speed(500)
queen8=queen_class.Queen(8)
res=queen8.getBoard()

def square(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()

    if z%2==1:
        t.color('black','white')
    else:
        t.color('black','yellow')

    t.begin_fill()

    for i in range(4):
        t.forward(SIZE)
        t.left(90)

    t.end_fill()
    
def set_color(f):
    if f%2==0:
        t.color('black','white')
    else:
        t.color('black','yellow')


def rectangle(x,y,w,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def polyline(p):
    t.penup()
    t.goto(p[0][0],p[0][1])
    t.pendown()
    t.begin_fill()
    for q in p:
        t.goto(q[0],q[1])
    t.end_fill()

def queen(x,y,z):  
    rectangle (x+SIZE*0.1,y+SIZE*0.1,SIZE*0.8,SIZE*0.1)
    rectangle (x+SIZE*0.15,y+SIZE*0.2,SIZE*0.7,SIZE*0.1)

    p=((x+0.15*SIZE,y+0.3*SIZE),
       (x+0.1*SIZE,y+0.4*SIZE),
       (x+0.9*SIZE,y+0.4*SIZE),
       (x+0.85*SIZE,y+0.3*SIZE))
    polyline(p)

    p=((x+0.1*SIZE,y+0.4*SIZE),(x+0.05*SIZE,y+0.95*SIZE),(x+0.4*SIZE,y+0.4*SIZE),
       (x+0.5*SIZE,y+0.95*SIZE),(x+0.6*SIZE,y+0.4*SIZE), (x+0.945*SIZE,y+0.95*SIZE),
      (x+0.9*SIZE,y+0.4*SIZE))
    polyline(p)
    


t.tracer(0)
t.hideturtle()
for j in range(8):
    for k in range(8):
        x=(j-4)*SIZE
        y=(k-4)*SIZE
        z=j*7+k
        square(x,y,z)
        if res[j][k]==1:
            queen(x,y,z)
t.update()











    
