import turtle

itl=turtle.Turtle()


for i in range (1):
    itl.pu()
    itl.right(180)
    itl.fd(400)
    itl.left(90)
    itl.fd(200)
    itl.right(90)
    itl.pd()
    itl.left(180)
    itl.begin_fill()
    itl.color("green")
    for i in range (1):
        itl.pencolor("black")
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
        itl.left(90)
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
    itl.end_fill()
    itl.left(90)
    for i in range (1):
        itl.begin_fill()
        itl.color("white")
    for i in range (1):
        itl.fd(267)
        itl.pencolor("black")
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
        itl.left(90)
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
    itl.end_fill()
    itl.left(90)
    itl.pu()
    itl.fd(267)
    itl.pd()
    for i in range (1):
        itl.begin_fill()
        itl.color("red")
    for i in range (1):
        itl.pencolor("black")
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
        itl.left(90)
        itl.fd(267)
        itl.left(90)
        itl.fd(450)
    itl.end_fill()
    
