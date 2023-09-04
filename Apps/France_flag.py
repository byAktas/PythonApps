import turtle

frs=turtle.Turtle()


for i in range (1):
    frs.pu()
    frs.right(180)
    frs.fd(400)
    frs.left(90)
    frs.fd(200)
    frs.right(90)
    frs.pd()
    frs.left(180)
    frs.begin_fill()
    frs.color("blue")
    for i in range (1):
        frs.pencolor("black")
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
        frs.left(90)
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
    frs.end_fill()
    frs.left(90)
    for i in range (1):
        frs.begin_fill()
        frs.color("white")
    for i in range (1):
        frs.fd(267)
        frs.pencolor("black")
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
        frs.left(90)
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
    frs.end_fill()
    frs.left(90)
    frs.pu()
    frs.fd(267)
    frs.pd()
    for i in range (1):
        frs.begin_fill()
        frs.color("red")
    for i in range (1):
        frs.pencolor("black")
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
        frs.left(90)
        frs.fd(267)
        frs.left(90)
        frs.fd(450)
    frs.end_fill()
    
