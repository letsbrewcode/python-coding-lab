# Complete the funtion below
# Given a string, print a pyramid by printing each character of a 
# string on a new line. If its the nth character then it should be
# repeated n times.
# If input string is None or empty then print an '*'
# Example, for s = 'Saturn'
# Output:
# S
# aa
# ttt
# uuuu
# rrrrr
# nnnnnn

# Solution 1
def print_pyramid(s):
    for x in range(len(s)):
        print(s[x] * (x + 1))
    return

# solution 2
def print_pyramid_2(s):
    for i, x in enumerate(s):
        print(x * (i + 1))
    return

if __name__ == '__main__':
    test_case = ['Saturn', '123456789', '']
    for t in test_case:
        print(t)
        print_pyramid_2(t)
        print_pyramid(t)
