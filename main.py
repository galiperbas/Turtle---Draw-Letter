import turtle

wn = turtle.Screen()
wn.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed("slow")
pen.pensize(6)
pen.color("blue")

# initial location:
inital_x = -200
inital_y = 100


def pen_go_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def blank():
    pen.penup()
    pen.forward(10)
    pen.pendown()


pen_go_to(inital_x, inital_y)


def draw_a():
    pen.setheading(0)
    pen_go_to(inital_x, inital_y)

    for i in range(4):
        pen.forward(100)
        blank()
        pen.right(90)
        blank()

    pen_go_to(inital_x - 10, inital_y - 130)
    pen.right(90)
    pen.forward(100)

    pen_go_to(inital_x + 110, inital_y - 130)
    pen.forward(100)


def draw_b():
    pen.setheading(0)  # initial angle

    pen_go_to(inital_x + 140, inital_y)

    for i in range(4):
        pen.forward(100)
        blank()
        pen.right(90)
        blank()

    pen_go_to(inital_x + 130, inital_y - 130)
    pen.right(90)
    for i in range(3):
        pen.forward(100)
        blank()
        pen.left(90)
        blank()


# press-key

wn.onkey(draw_a, "a")
wn.onkey(draw_b, "b")
wn.listen()

wn.exitonclick()
