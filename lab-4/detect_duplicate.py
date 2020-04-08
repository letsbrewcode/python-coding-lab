# Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: True

# Example 2:
# Input: [1,2,3,4]
# Output: False

def contains_duplicate(arr):
    return

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test(contains_duplicate([1,2,3,1]), True)
    test(contains_duplicate([1,2,3,4]), False)
    test(contains_duplicate([1,1,1,3,3,4,3,2,4,2]), True)
