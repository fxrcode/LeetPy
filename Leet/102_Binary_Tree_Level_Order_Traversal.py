"""
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
Leetcode Explore: Binary Tree - Traverse a Tree
https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2784/
Leetcode explore Recursion II: Recursion to Iteration

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

eg.
* 01-Matrix (init queue with all 0's, to get all 0's shortest distance to 1)
* Target Sum (lee215 solution using rolling 2 queue for level order)
"""

# Definition for a binary tree node.


from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Classic impl with 1 queue and loop qlen
        T: O(V+E), because Tree's E = V-1, so O(V)
        M: O(2^h) because last level has 2^h nodes, given h the height of tree
        """

        def level_qlen():
            res = []
            if not root:
                return res
            q = deque([root])
            # visited = set([root])
            while q:
                cur_level, qlen = [], len(q)
                for _ in range(qlen):
                    cur = q.popleft()
                    cur_level.append(cur.val)
                    # visit neighbor
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                res.append(cur_level)
            return res

        def doubleQ():
            """
            BFS level order use 2 queues
            https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
            Same technique in 494. Target Sum by lee215. Since we need # ways to get sum, we use map rather queue
            """
            res = []
            level = [root]  # level is the generic pointer
            if not root:
                return res
            while level:
                cur_level = []
                next_level = []
                for node in level:
                    cur_level.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                res.append(cur_level)
                level = next_level  # update pointer to next level
            return res
