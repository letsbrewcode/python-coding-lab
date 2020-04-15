# Complete the function below. Given an input string, replace the
# second character with '*' and return the new modified string if
# the string length is odd. Otherwise return the original string.
# If the string length is less than 2 then do not modify string.

# Example 1
# Input: 'Hello'
# Output: 'H*llo'

# Example 2
# Input: 'Cake'
# Output: 'Cake'

def second_modify(s):
    if len(s) >= 2 and len(s) % 2 == 1:
        return s[0] + '*' + s[2:]
    else:
        return s
        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test(second_modify('Hello'), 'H*llo')
    test(second_modify('Cake'), 'Cake')
    test(second_modify('@'), '@')
    test(second_modify('He'), 'He')
