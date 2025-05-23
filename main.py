import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("lightblue1")

t = turtle.Turtle()
t.speed(0)


#sand
t.penup()
t.goto(-5000,200)
t.pendown()
t.fillcolor("green")
t.pencolor("green")
t.begin_fill()
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100)
t.end_fill()
#danny brown
t.penup()
t.goto(150,0)
t.pendown()
t.pencolor("navajowhite3")
t.fillcolor("navajowhite3")
t.begin_fill()
t.goto(-200,0)
t.goto(2,100)
t.goto(150,0)
t.end_fill()


#sun
t.penup()
t.goto(-300,300)
t.pendown()
t.circle(70)
t.fillcolor("yellow")
t.pencolor("yellow")
t.begin_fill()
t.end_fill()




#flower
t.penup()
t.goto(190,0)
t.pendown()
t.pencolor("green")
t.fillcolor("green")

t.goto(200,30)
t.goto(200,40)



turtle.done()