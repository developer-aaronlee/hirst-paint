# import colorgram
#
# colors = colorgram.extract('haist.jpg', 30)
#
# my_color = []
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     one_color = (r, g, b)
#     my_color.append(one_color)
#
# print(my_color)

import turtle
import random
turtle.colormode(255)

color_list = [(243, 225, 235), (185, 157, 167), (247, 236, 227), (231, 231, 244), (28, 17, 24), (215, 176, 191),
              (112, 83, 101), (207, 160, 117), (22, 20, 37), (152, 163, 195), (140, 77, 65), (89, 85, 123),
              (225, 205, 125), (18, 9, 8), (205, 88, 73), (173, 104, 123), (185, 183, 217), (58, 50, 95),
              (89, 48, 71), (153, 174, 164), (218, 178, 174), (123, 113, 175), (7, 13, 10), (83, 122, 112),
              (152, 142, 85), (160, 202, 208), (98, 50, 48), (96, 147, 132), (171, 204, 187)]

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed(10)
timmy.hideturtle()


def drawing():
    for x in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


def turning(a, b):
    timmy.penup()
    timmy.setposition(a, b)


a = -225
b = -225
timmy.penup()
timmy.setposition(a, b)


for x in range(10):
    drawing()
    b += 50
    turning(a, b)


screen = turtle.Screen()
screen.exitonclick()