#! /usr/bin/env python

import turtle
from random import randrange


def tree(branchLen, t, pensize):
    count = 1
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
        else:
            t.color("SaddleBrown")
        t.pensize(pensize)
        t.forward(branchLen)
        right = randrange(20, 90)
        # print 'right: ' + str(right) + str(count)
        t.right(right)
        tree(randrange(branchLen-20, branchLen), t, pensize // 2)
        left = randrange(20, 90)
        # print 'left: ' + str(left) + str(count)
        t.left(left + right)
        tree(randrange(branchLen-20, branchLen), t, pensize // 2)
        t.right(left)
        count += 1
        if branchLen < 20:
            t.color("green")
        else:
            t.color("SaddleBrown")
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("wheat4")
    tree(75, t, 20)
    myWin.exitonclick()

if __name__ == '__main__':
    main()
