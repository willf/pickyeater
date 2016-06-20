import random

from graphics import *


def edible_1d(y, n):
    return n / 4 <= y <= 3 * n / 4


def edible(x, y, n):
    return edible_1d(x, n) and edible_1d(y, n)


def main():
    n = 100
    runs = 5000
    win = GraphWin()
    win.setCoords(0, 0, n, n)
    win.setBackground("black")
    edibles = 0
    for run in range(runs):
        x = random.randint(0, n)
        y = random.randint(0, n)
        if edible(x, y, n):
            edibles += 1
            win.plot(x, y, "white")
        else:
            win.plot(x, y, "red")

    print(edibles / runs)
    win.getMouse()
    win.close()


main()
