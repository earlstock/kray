import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("lightblue1")

t = turtle.Turtle()
t.speed(0)


#sand
t.penup()
t.goto(-5000,-100)
t.pendown()
t.fillcolor("navajowhite2")
t.pencolor("navajowhite2")
t.begin_fill()
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100)
t.end_fill()

t.penup()
t.goto(50,0)
t.pendown()
t.pencolor("navajowhite3")
t.fillcolor("navajowhite3")
t.begin_fill()
t.goto(150,0)
t.goto(100,100)
t.goto(150,0)
t.end_fill()













turtle.done()