import random
import turtle

t = turtle.Turtle()
t.speed(0)
t.width(20)
screen = turtle.Screen()
screen.setup(width=600, height=400)

t.penup()
t.goto(-300,200)
t.pendown()

a = 0
b = 200

while a == 0:

    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    distance = random.randint(0, 5)

    for i in range(1):
        b -= 20
        if t.pos()[0] < 300:
            t.color(red/255, green/255, blue/255)
            t.forward(distance)
        if t.pos()[0] >= 300:
            t.penup()
            t.goto(-300,t.pos()[-1]-20)
            t.pendown()

turtle.exitonclick()