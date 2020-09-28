# Given two strings, return a string made of common chars between both
# the strings. If the character is already found common between the two
# strings then do not add it again in the resulting string.
# Example
# s1 = 'abcd' and s2 = 'azxc'  ==> result = 'ac'
# s1 = 'aaab' and s2 = 'aac'   ==> result = 'a'


def common_chars(s1, s2):
    # Your code
    return

if __name__ == '__main__':
    test_case = [('abcd', 'azxc'), ('aaab', 'aac'), ('abcd', 'wxyz')]
    
    for t in test_case:
        s1, s2 = t[0], t[1]
        print('For {} and {}, common chars are -> {}'.format(s1, s2, common_chars(s1, s2)))
