'''
FB tag (Medium)
'''

from typing import List, Optional
from collections import defaultdict


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def post_height():
            """
            Runtime: 61 ms, faster than 5.07% of Python3 online submissions for Find Leaves of Binary Tree.

            T:O(N), M:O(N)
            """

            def height(node: TreeNode, heights):
                if not node:
                    return -1
                l = height(node.left, heights)
                r = height(node.right, heights)
                hgt = max(l, r) + 1
                heights[hgt].append(node.val)
                return hgt

            dic = defaultdict(list)
            height(root, dic)

            res = []
            for h in range(len(dic)):
                res.append(dic[h])
            return res
