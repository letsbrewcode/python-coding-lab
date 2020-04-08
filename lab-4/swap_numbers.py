# Swap Numbers
# You are given an array containing some items and two indices. Complete the function
# below which swaps the items present on the two indices. If the indices are out
# of bound then return the unchanged array.

# Example 1
# Input, A = [1000, 2, 95, 109, 37, 46, 77], index1 = 2, index2 = 5
# Output => [1000, 2, 46, 109, 37, 95, 77]
#
# Example 2
# Input, A = ['Hi', 'Bye'], index1 = 0, index2 = 1
# Output => ['Bye', 'Hi']
#
# Example 3
# Input, A = ['Hi', 'Bye'], index1 = 0, index2 = 3
# Output => ['Hi', 'Bye']

def swap_nums(arr, index1, index2):
    return

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test(swap_nums([1000, 2, 95, 109, 37, 46, 77], 2, 5), [1000, 2, 46, 109, 37, 95, 77])
    test(swap_nums(['Hi', 'Bye'], 0, 1), ['Bye', 'Hi'])
    test(swap_nums(['Hi', 'Bye'], 0, 2), ['Hi', 'Bye'])
