"""
    Problem: FizzBuzz

    Complete the function below. For a number N, print all the numbers starting
    from 1 to N, except
    1. For numbers divisible by 3, print "Fizz"
    2. For numbers divisible by 5, print "Buzz"
    3. For numbers divisible by both 3 and 5, print "FizzBuzz"

    Example: N = 16
    Output:
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
"""

def fizzbuzz(n):
    x = 1
    while x <= n:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

        x += 1

if __name__ == "__main__":
    fizzbuzz(100)
