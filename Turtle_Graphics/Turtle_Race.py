from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)

for step in range(1,11):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(30)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.right(360)
ada.pendown()

bob = Turtle()
bob.color('yellow')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.left(360)
bob.pendown()

von = Turtle()
von.color('green')
von.shape('turtle')
von.penup()
von.goto(-160,40)
von.right(360)
von.pendown()

rob = Turtle()
rob.color('blue')
rob.shape('turtle')
rob.penup()
rob.goto(-160,10)
rob.left(360)
rob.pendown()



for turn in range(95):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    von.forward(randint(1,5))
    rob.forward(randint(1,5))

