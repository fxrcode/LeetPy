"""
✅ GOOD DFS (w/ return)
tag: easy, dfs
Lookback:
- GOOD os in analysis top-down vs bottom-up DFS time complexity!
- 小组讨论题目
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1027/
Leetcode Explore Binary Search Tree: Conclusion

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Similar: 124, 543, 563
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bottom_up(cur: TreeNode) -> (bool, int):
            """
            Runtime: 41 ms, faster than 94.86% of Python3 online submissions for Balanced Binary Tree.

            """
            # return bool, int
            if not cur:
                return True, -1
            # check subtrees to see if they're balanced
            bal_l, hgt_l = bottom_up(cur.left)
            if not bal_l:
                return False, 0
            bal_r, hgt_r = bottom_up(cur.right)
            if not bal_r:
                return False, 0

            # if both subtrees balanced, check if current tree is balanced using subtree height
            bal_cur, hgt_cur = abs(hgt_l - hgt_r) < 2, 1 + max(hgt_l, hgt_r)
            return bal_cur, hgt_cur

        return bottom_up(root)[0]


'''
        def height(cur: TreeNode) -> int:
            # XXX: common snippet
            if not root:
                return -1
            return 1 + max(height(cur.left), height(cur.right))

        def top_down(cur: TreeNode) -> bool:
            """
            Runtime: 60 ms, faster than 46.70% of Python3 online submissions for Balanced Binary Tree.

            Q: Why/when do I need 2-layer DFS?
            A: (OS) The balanced subtree definition hints at the fact that we should treat each subtree as a subproblem.
            """
            if not root:
                return True
            return top_down(cur.left) and top_down(cur.right) and abs(height(cur.left) - height(cur.right)) <= 1

    def isBalanced_fxr_WA(self, root: Optional[TreeNode]) -> bool:
        """
        BUG: 88 / 228 test cases passed.
        eg. [1,null,2,null,3]
        """
        self.minmax = [1e6, 0]

        def dfs(cur, height):
            if not cur:
                return True
            if not cur.left and not cur.right:
                self.minmax[0] = min(self.minmax[0], height)
                self.minmax[1] = max(self.minmax[1], height)
                if self.minmax[1] - self.minmax[0] > 1:
                    return False
            return dfs(cur.left, height + 1) and dfs(cur.right, height + 1)

        if not root:
            return True
        return dfs(root, 1)
'''


root = TreeNode(
    3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
)

sl = Solution()
print(sl.isBalanced(root))
