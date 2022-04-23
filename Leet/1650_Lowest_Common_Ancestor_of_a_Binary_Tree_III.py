'''
FB tag (Medium)
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def os():
            """
            Runtime: 68 ms, faster than 79.32% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.

            https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932499/Simple-Python-Solution-with-O(1)-space-complexity/871946
            XXX: common trick to find meeting point as in Floyd's Cycle Finding Algorithm
            T: O(H)
            M: O(1)
            """
            i, j = p, q
            while i != j:
                i = i.parent if i.parent else q
                j = j.parent if j.parent else p
            return i