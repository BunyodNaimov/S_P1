import turtle

window = turtle.Screen()

# orqa fon
window.bgcolor("#0049FF")
t = turtle.Turtle()
t.speed(0)

# Sohil qismi
t.up()
t.goto(-383, -50)
t.down()
t.color("#DDD69B")
t.begin_fill()
for i in range(2):
    t.forward(758)
    t.right(90)
    t.forward(265)
    t.right(90)
t.end_fill()

# Osmon qismi

t.up()
t.goto(-385, 160)
t.down()
t.color("#A7CBFF")
t.begin_fill()
for i in range(2):
    t.forward(760)
    t.left(90)
    t.forward(265)
    t.left(90)
t.end_fill()

# Quyosh
t.up()
t.goto(300, 250)
t.down()
t.color("yellow")

t.pensize(10)
t.dot(80, "yellow")
for i in range(8):
    t.left(45)
    t.forward(80)
    t.backward(80)
t.left(40)

# Bulut
t.up()
t.goto(0, 250)
t.down()
t.color("white")
for i in range(3):
    t.begin_fill()
    t.circle(35)
    t.right(50)
    t.end_fill()
t.left(200)


# Qushlar shakli
def qush(x, y):
    t.color("black")
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(2):
        t.setheading(0)
        t.left(145)
        t.circle(35, 90)


qush(-210, 250)
qush(-270, 210)
qush(-230, 180)
t.left(170)

# Akula shakli
def shark(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.left(30)
    t.fillcolor("#B0ACAB")
    t.begin_fill()
    t.circle(50, 60)
    t.left(50)
    t.circle(50, -98)
    t.right(40)
    t.end_fill()


shark(-100, 100)
shark(-110, 30)
shark(-20, 50)

window.mainloop()
