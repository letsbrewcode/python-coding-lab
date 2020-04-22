# First Unique
# Given a string containing all lowercase characters, find
# the first non-repeating character in the string

# Example 1
# Input : "trignometry"
# Output: "i" 

# Example 2
# Input : "abccba"
# Output: ""

def first_unique(s):
    counts = {}
    for x in s:
        counts[x] = counts.get(x, 0) + 1

    for x in s:
        if counts[x] == 1:
            return x

    return ''

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test_cases = [('himanshu sharma', 'i'),
                  ('abccba', ''),
                  ('successful', 'e')
		 ]
    for t in test_cases:
        test(first_unique(t[0]), t[1])
