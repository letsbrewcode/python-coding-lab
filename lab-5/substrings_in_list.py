# Given an array of string words. Return all strings in words which is substring of another word in any order. 
# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or
# right side of words[j].

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["universe","un","verse"]
# Output: ["un","verse"]
# Explanation: "un", "verse" are substring of "universe".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []

def substrings(words):
    return

def test(got, expected):
    if sorted(got) == sorted(expected):
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))

if __name__ == '__main__':
    test(substrings(["mass","as","hero","superhero"]), ["as","hero"])
    test(substrings(["universe","un","verse"]), ["un","verse"])
    test(substrings(["blue","green","bu"]), [])
    
