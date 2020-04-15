# Find end destination of travel route
# Imagine a 2D coordinate system centered at (0,0), You are given the
# route of a traveling point in the form of array. Each item of the array
# contains a direction and distace moved in that direction. Complete the
# function, destination to compute the route and return the final coordinate
# where the point finishes its travel. The answer should be returned in
# the form of a tuple, (x, y)

# Example
# Input = [['N', 1], ['E', 1]]
# Output = (1, 1)
# The point moves 1 unit north and then 1 unit east resulting in the final
# destination as x = 1 and y = 1. It is returned as tuple, (1, 1)

def destination(route):
    x, y = 0, 0
    for direction, distance in route:
        if direction == 'E':
            x += distance
            continue
        if direction == 'W':
            x -= distance
            continue
        if direction == 'N':
            y += distance
            continue
        if direction == 'S':
            y -= distance
            continue
    
    return x, y
        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    route1 = [['E', 2], ['N', 5], ['W', 1]]
    route2 = [['E', 4], ['N', 10], ['W', 7], ['S', 7], ['E', 10]]
    route3 = [['E', 10], ['N', 10], ['W', 10], ['S', 5], ['S', 5]]
    
    test(destination(route1), (1, 5))
    test(destination(route2), (7, 3))
    test(destination(route3), (0, 0))
