import turtle

blg=turtle.Turtle()


for i in range (1):
    blg.pu()
    blg.right(180)
    blg.fd(400)
    blg.left(90)
    blg.fd(200)
    blg.right(90)
    blg.pd()
    blg.left(180)
    blg.begin_fill()
    blg.color("red")
    for i in range (1):
        blg.pencolor("black")
        blg.fd(801)
        blg.left(90)
        blg.fd(150)
        blg.left(90)
        blg.fd(801)
        blg.left(90)
        blg.fd(150)
    blg.end_fill()
    
    blg.begin_fill()
    blg.color("green")
for i in range (1):
    blg.pencolor("black")
    blg.right(180)
    blg.fd(300)
    blg.right(90)
    blg.fd(801)
    blg.right(90)
    blg.fd(150)
    blg.right(90)
    blg.fd(801)
    
    blg.end_fill()
    
    blg.begin_fill()
    blg.color("white")
for i in range (1):
    blg.pencolor("black")
    blg.right(90)
    blg.fd(300)
    blg.right(90)
    blg.fd(801)
    blg.right(90)
    blg.fd(150)
    blg.right(90)
    blg.fd(801)

    blg.end_fill()
        
    
    
