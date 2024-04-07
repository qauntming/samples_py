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
    for x in range(200):
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

print("查找定积分")
print("f(x)=ax^2+bx+c")
a=float (input('a='))
b=float (input('b='))
c=float (input('c='))
x1=float(input('x1='))
x2=float(input("x2="))
A1=(a*(x1**3/3)+b*(x1**2/2)+c*x1)
A2=(a*(x2**3/3)+b*(x2**2/2)+c*x2)
A=A2-A1
print("定积分为，",A)

draw(a,b,c,x1,x2)