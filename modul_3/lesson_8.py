import turtle

window = turtle.Screen()
window.bgcolor("#B0F1FA")

t = turtle.Turtle()
t.speed(0)

# Yer qismi
t.up()
t.goto(-375, -230)
t.down()
t.fillcolor("#133A59")
t.begin_fill()
for i in range(2):
    t.forward(745)
    t.right(90)
    t.forward(85)
    t.right(90)
t.end_fill()

# Devor qismi
t.up()
t.goto(-280, -250)
t.down()
t.color("#86A5C2")
t.fillcolor("#86A5C2")
t.begin_fill()
for _ in range(2):
    t.forward(540)
    t.circle(15, 90)
    t.forward(310)
    t.circle(15, 90)
t.end_fill()

# Tom qismi
t.up()
t.goto(-290, 90)
t.down()
t.color("#471878")
t.fillcolor("#471878")
t.begin_fill()
t.left(35)
t.forward(340)
t.right(70)
t.forward(340)
t.right(145)
t.forward(560)
t.end_fill()


# Oyna qismi

def oyna(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.pencolor("#471878")
    t.fillcolor("#F0EDE7")
    t.pensize(3)
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.circle(10, 90)
    t.end_fill()
    t.forward(25)
    t.left(90)
    t.forward(70)
    t.right(90)
    t.forward(25)
    t.circle(-10, 90)
    t.forward(25)
    t.right(90)
    t.forward(70)
    t.hideturtle()


oyna(-200, 50)

oyna(300, 100)


window.mainloop()
