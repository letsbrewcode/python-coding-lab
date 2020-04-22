# Odd Replace
# Complete the function below. Given a strings, replace 
# all the odd characters in string with character '-'. 
# If the string is Empty or None then return an empty 
# string.

def odd_replace(s):
    ans = ''
    for i in range(len(s)):
        if i % 2 == 0:
            ans += '-'
        else:
            ans += s[i]
    return ans

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test_cases = [('Saturn', '-a-u-n'),
                  ('a', '-'), 
		  ('123456789', '-2-4-6-8-')
		 ]
    for t in test_cases:    
        test(odd_replace(t[0]), t[1])
