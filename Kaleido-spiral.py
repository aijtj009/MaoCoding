import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange','yellow','green','blue','purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)
    
t.bgcolor('black')   
t.speed(999)
t.pensize(10)
draw_circle(30, 0, 1)


