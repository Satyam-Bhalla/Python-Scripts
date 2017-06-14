from turtle import *

screen = Screen()
screen.setup(400,400)

colors = {
    'orange':'#FF9C33',
    'dark':'#37322D'
    }

screen.bgcolor(colors['orange'])
color(colors['dark'])
style = ('Arial',40,'bold')

write('HELLO',font=style,align='center')
#circle(100)
hideturtle()
