"""
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/915/
N-ary Tree: Traversal
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3897/
Leetcode Explore Graph: BFS

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""

# Definition for a Node.


import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        """
        Your runtime beats 66.06 % of python3 submissions.
        AC in 1.
        """
        res = []
        if not root:
            return res
        q = collections.deque([root])
        while q:
            qlen = len(q)
            cur_level = []
            for _ in range(qlen):
                cur = q.popleft()
                cur_level.append(cur.val)
                if cur.children:
                    q.extend(cur.children)
            res.append(cur_level)

        return res
