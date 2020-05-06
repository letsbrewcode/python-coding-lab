# Point
# Complete the Point class below. Points may be created by either passing x,y
# coordinates. If not coordinates are passed then initialize the point as (0,0).
# Functions move_x and move_y add the x and y distance by argument value.
# Function, distance calculates the distance of the point from origin, (0,0).
# 
# Provided below is a barebone skeleton of class. Based on the calls mentioned,
# complete the init and functions below. You will also need to add arguments.

# NOTE - You will get errors when you try to execute the code below. This is 
# because code is syntactically not complete. You need to fix all the errors.

import math

class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move_x(self, dist):
        self.x += dist

    def move_y(self, dist):
        self.y += dist

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        # (x, y)
        return "({},{})".format(self.x, self.y)

if __name__ == '__main__':
    p1 = Point(1,2)
    p2 = Point()
    p1.move_x(3)
    p2.move_x(5)
    p2.move_y(10)
    print(p1)
    print(p2)
    print(p1.distance())
    print(p2.distance())
