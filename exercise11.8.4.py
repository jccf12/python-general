import turtle
t = turtle.Turtle()
f = open('labdata.txt', 'r')
w = turtle.Screen()


def plotRegression(txtfile):
    coords = [[int(x.split()[0]), int(x.split()[1])] for x in txtfile]
    blx = min([c[0] for c in coords])
    bly = min([c[1] for c in coords])
    rtx = max([c[0] for c in coords])
    rty = max([c[1] for c in coords])
    w.setworldcoordinates(blx, bly, rtx, rty)
    for pair in coords:
        t.goto(pair[0], pair[1])
        t.stamp()


plotRegression(f)
