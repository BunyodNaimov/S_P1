import turtle

window = turtle.Screen()
window.setup(900, 600)

t = turtle.Turtle()
t.speed(1)
t.pensize(10)
t.write("PDP Junior", font=("Arial", 48, "bold"), move=True)

window.mainloop()
