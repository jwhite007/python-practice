#! /usr/bin/env python

import turtle

# def drawTriangle(points,color,myTurtle):
#     myTurtle.fillcolor(color)
#     myTurtle.up()
#     myTurtle.goto(points[0][0],points[0][1])
#     myTurtle.down()
#     myTurtle.begin_fill()
#     myTurtle.goto(points[1][0],points[1][1])
#     myTurtle.goto(points[2][0],points[2][1])
#     myTurtle.goto(points[0][0],points[0][1])
#     myTurtle.end_fill()

# def getMid(p1,p2):
#     return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# def sierpinski(points,degree,myTurtle):
#     colormap = ['blue','red','green','white','yellow',
#                 'violet','orange']
#     drawTriangle(points,colormap[degree],myTurtle)
#     if degree > 0:
#         sierpinski([points[0],
#                         getMid(points[0], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[1],
#                         getMid(points[0], points[1]),
#                         getMid(points[1], points[2])],
#                    degree-1, myTurtle)
#         sierpinski([points[2],
#                         getMid(points[2], points[1]),
#                         getMid(points[0], points[2])],
#                    degree-1, myTurtle)

# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-200,-50],[-100,100],[250,-50]]
#    sierpinski(myPoints,3,myTurtle)
#    myWin.exitonclick()

# main()

def draw_poly(num_sides, turn, length, turtle):
    t = turtle
    total_of_angles = 180
    angle_multiplier = num_sides - 3
    total_of_angles = 180 + 180 * angle_multiplier
    angle = total_of_angles / num_sides
    if turn > 0:
        t.forward(length)
        t.left(180 - angle)
        turn -= 1
        draw_poly(num_sides, turn, length, t)


# def sierpinski(deg, length, turtle):
#     t = turtle
#     length /= 2
#     # t.penup()
#     if deg > 0:
#         t.penup()
#         t.forward(length)
#         t.left(60)
#         t.pendown()
#         draw_poly(3, 3, length, t)
#         deg -= 1
#         t.right(60)
#         sierpinski(deg, length, t)
#         t.backward(3 * length / 8)

# def sierpinski(deg, length, turtle):
#     t = turtle
#     t.pendown()
#     if deg > 0:
#         draw_poly(3, 3, length, t)
#         draw_poly(3, 3, length / 2, t)
#         t.forward(length)
#         t.left(120)
#         draw_poly(3, 3, length / 2, t)
#         t.forward(length)
#         t.left(120)
#         draw_poly(3, 3, length / 2, t)
        # deg -= 1
        # sierpinski(deg, length / 2, t)
        # t.forward(length / 3)
        # draw_poly(3, 3, length / 3, t)
        # sierpinski(deg, length / 2, t)


# t = turtle.Turtle()
# win = turtle.Screen()
# t.penup()
# t.setpos(-200, -150)
# sierpinski(2, 400, t)
# win.exitonclick()


def draw_triangle(points, color, turtle):
    t = turtle
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def get_mid(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)


def sierpinski(deg, points, turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                        'violet', 'orange']

    draw_triangle(points, colormap[deg], turtle)

    if deg > 0:
        sierpinski(deg - 1, [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], turtle)
        sierpinski(deg - 1, [points[1], get_mid(points[1], points[2]), get_mid(points[0], points[1])], turtle)
        sierpinski(deg - 1, [points[2], get_mid(points[0], points[2]), get_mid(points[1], points[2])], turtle)


t = turtle.Turtle()
win = turtle.Screen()
# points = [[-100, -100], [100, -100], [0, 200]]
# sierpinski(3, points, t)
t.fillcolor("blue")
t.up()
t.goto(-100, -100)
t.down()
t.begin_fill()
draw_poly(5, 5, 200, t)
t.end_fill()

win.exitonclick()
