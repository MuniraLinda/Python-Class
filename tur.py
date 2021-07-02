from turtle import t
t.color('red')
t.speed(11)
t.pensize(2)
t.hideturtle()
for i in range(60):
    t.left(6)
    for j in range(4):
        t.forward(200)
        t.left(90)