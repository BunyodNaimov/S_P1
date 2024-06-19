import turtle

window = turtle.getscreen()
window.setup(width=600, height=550)

t = turtle.Turtle()
t.shape("triangle")
t.speed(1)
t.forward(200)
window.mainloop()
