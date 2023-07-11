"""
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/926/
N-ary Tree: Traversal
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""

# Definition for a Node.
from typing import List

import Util


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        """[summary]
        Your runtime beats 38.35 % of python3 submissions.

        XXX: similar to 94. Binary Tree Inorder Traversal
        https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31228/Simple-Python-iterative-solution-by-using-a-visited-flag-O(n)-56ms
        Universal stack iterative using visited flag, can be easily modified for pre/in/post order.
        Because normal pre/in order iterative stack is easy, but post order hard.
        This method is easy to understand and memoize.
        """
        res = []
        stk = [(root, False)]

        while stk:
            cur, visited = stk.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    # post: LRV -> VRL
                    stk.append((cur, True))
                    if cur.children:
                        for kid in reversed(cur.children):
                            stk.append((kid, False))

        return res


sl = Solution()
yi, er, san, si, wu, liu = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
yi.children = [er, san]
er.children = [liu]
san.children = [si, wu]

print(sl.postorder(yi))
