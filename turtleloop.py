import turtle
from random import randint
unum = int(input('What is your favorite number? '))

turtle.bgcolor('black')
turtle.pensize(10)
turtle.colormode(255)
turtle.speed(0)
x = 1

while True:
    while x < unum:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        turtle.pencolor('r,g,b')
        turtle.fd(x+5)
        turtle.rt(90.911)
        x += 1

    while x > 1:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        turtle.pencolor('r,g,b')
        turtle.fd(x+5)
        turtle.rt(90.911)
        x -= 1
