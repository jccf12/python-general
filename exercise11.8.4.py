import turtle
t = turtle.Turtle()
f = open('labdata.txt', 'r')
w = turtle.Screen()


def plotRegression(txtfile):
    coords = [[int(x.split()[0]), int(x.split()[1])] for x in txtfile]
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    n = len(coords)
    blx = min(xs)
    bly = min(ys)
    rtx = max(xs)
    rty = max(ys)
    meanx = sum(xs)/n
    meany = sum(ys)/n

    w.setworldcoordinates(blx-5, bly-5, rtx+5, rty+5)
    t.shape('circle')
    t.speed(10)
    t.up()
    t.turtlesize(0.25)
    for pair in coords:
        t.goto(pair[0], pair[1])
        t.stamp()

    a = sum([xs[i]*ys[i]-meanx*meany for i in range(n)])
    b = sum([xs[i]-meanx**2 for i in range(n)])
    m = a/b

    t.goto(blx-3, meany+m*(blx-3-meanx))
    t.color('red')
    t.down()
    t.goto(rtx+3, meany+m*(rtx+3-meanx))


plotRegression(f)
w.exitonclick()
