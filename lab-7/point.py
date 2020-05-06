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

class Point:

    def __init__():
        # +++ your code here +++
        pass

    def move_x():
        # +++ your code here +++
        pass

    def move_y():
        # +++ your code here +++
        pass

    def distance():
        # +++ your code here +++
        pass

    def __str__():
        # +++ your code here
        pass

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
