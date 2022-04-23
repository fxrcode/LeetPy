"""
✅ GOOD DFS Tree (Path)
tag: Easy, dfs
Lookback:
- classic post-order dfs

Similar:
- 687. Longest Univalue Path

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        def diameter(cur: TreeNode) -> int:
            """
            Runtime: 48 ms, faster than 63.43% of Python3 online submissions for Diameter of Binary Tree.

            """
            if not cur:
                return 0

            long_l, long_r = diameter(cur.left), diameter(cur.right)
            self.diam = max(self.diam, long_l + long_r)
            return max(long_l, long_r) + 1

        '''
        def neet(cur: TreeNode) -> int:
            """
            Neetcode & Huahua uses Tree height
            REF: https://www.youtube.com/watch?v=bkxqA8Rfv04

            leaf node height = 0
            Null node height = -1
            """
            if not cur:
                return -1

            hl, hr = neet(cur.left), neet(cur.right)
            self.diam = max(self.diam, hl+hr+1+1)
            return max(hl, hr)+1
        '''

        diameter(root)
        return self.diam
