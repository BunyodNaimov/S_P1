import turtle
import random

window = turtle.getscreen()
window.setup(width=500, height=450)
turtle.title("PDP Junior")
t = turtle.Turtle()
t.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
forword_ = 100
window.bgcolor('black')
while True:
    for i in range(4):
        t.forward(forword_)
        t.left(98)
        forword_ += 1
    t.color(random.choice(colors))

turtle.mainloop()
