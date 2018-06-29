import turtle
t = turtle.Turtle()
w = turtle.Screen()
t.speed(10)

f = open('mystery.txt', 'r')
for l in f:
    i = l.split()
    if i[0] == 'UP':
        t.up()
    elif i[0] == 'DOWN':
        t.down()
    else:
        t.goto(int(i[0]), int(i[1]))

w.exitonclick()
