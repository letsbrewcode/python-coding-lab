"""
    Problem: Social Network
    Description: Complete the definition of class below, SocialNetwork. You
    will be provided with a relationship matrix in the form of lists of lists,
    [[a, b], [p, q]... ]

    Each pair in a list represents a friendship => a and b are friends so are p
    and q.

    Example
    Input:
    relation = [[9, 5], [5, 2], [2, 1], [5, 1], [3, 1], [3, 9], [2, 6]]
    
    If represented in graph, the above
    relations will look something like this:

    9----------5
    |          |\
    |          | \
    |          |  \
    |          |   2--------6
    |          |  /
    |          | /
    |          |/
    3----------1

    Complete the definition of
    - __init__()
    - friends()
        - returns a list of friends in any order
    - friends_of_friends()
        - returns a list of friends of friends in any
      order.

    Its up to you to decide the data structure that you would like to use. In
    the above example, the output of following functions will be - 
    
    friends(9) = 5, 3
    friends_of_friends(9) = [2, 1]

    friends(6) = 2
    friends_of_friends(6) = [1, 5]


"""

class SocialNetwork:

    def __init__(self, relations):
        # +++ Your code here +++
        return

    def friends(self, userid):
        # +++ Your code here +++
        return

    def friends_of_friends(self, userid):
        # +++ Your code here +++
        return
