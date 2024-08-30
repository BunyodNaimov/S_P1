import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.speed(0)
t.up()
t.setposition(-170, -250)
t.down()
for i in range(4):
    t.forward(300)
    t.left(90)
t.left(90)
t.forward(300)
t.right(45)
t.forward(210)
t.right(90)
t.forward(210)


t.up()
t.goto(-150, -80)
t.down()
t.left(135)
for i in range(4):
    t.forward(80)
    t.right(90)
t.up()
t.goto(20, -80)
t.down()
for i in range(4):
    t.forward(80)
    t.right(90)

t.up()
t.goto(-80, -120)
t.down()
t.right(90)
t.forward(100)
t.right(90)
t.forward(120)
t.right(90)
t.forward(100)
t.right(90)
t.forward(120)

window.mainloop()
