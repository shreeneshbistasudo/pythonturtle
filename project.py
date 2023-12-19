import turtle

turtle.bgcolor("black")
t=turtle.Turtle()

t.pensize(1)

colours=["blue","green","red",'purple']



t.speed('fastest')

for number in range(5000):
    
    t.pencolor(colours[number%4])
    
    
    t.forward(number)
    
    t.right(89)    
    
    
turtle.done()