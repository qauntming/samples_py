import turtle
def draw(a,b,c,x1,x2):
    turtle.speed(10000000)
    turtle.pendown()
    turtle.forward(1000)
    turtle.backward(2000)
    turtle.forward(1000)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(1000)
    turtle.backward(2000)
    turtle.penup()
    turtle.forward(1000)
    x=(-100)
    fx=(a*x**2+b*x+c)
    turtle.penup()
    turtle.goto(x,fx)
    turtle.pendown()
    for x in range(300):
        x-=100
        fx=(a*x**2+b*x+c)
        turtle.goto(x,fx)
        if abs(x-x1)<2:
            turtle.goto(x,0)
            turtle.goto(x,fx)
        if abs(x-x2)<2:
            turtle.goto(x,0)
            turtle.goto(x,fx)
    turtle.done()

draw(-0.05,5,12,-50,100)