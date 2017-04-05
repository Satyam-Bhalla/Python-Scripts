import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("cyan")
    #create the 1st turtle named brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the 2nd turtle satyam
    #satyam = turtle.Turtle()
    #satyam.shape("turtle")
    #satyam.color("red")
    #satyam.circle(100)
    
    window.exitonclick()
draw_art()    
