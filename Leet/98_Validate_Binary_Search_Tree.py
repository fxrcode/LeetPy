"""
✅ GOOD DFS (multiple args)
tag: dfs, BST
Lookback:
- common trick for BST: (min,max) range
Follow UP
* can you can break at most 1 edge to make it BST? (TuSimple)

https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2874/
Leetcode explore Recursion II: Divide and Conquer


Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key.
2) The right subtree of a node contains only nodes with keys greater than the node's key.
3) Both the left and right subtrees must also be binary search trees.


"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 32 ms, faster than 99.49% of Python3 online submissions for Validate Binary Search Tree.

        Neetcode: a classic Tree Recursion problem. https://www.youtube.com/watch?v=s6ATEkipzow
        Simple coding, and optimal time: O(N)
        XXX: Crux: explain nicely what value to set for floor/ceiling. As always, there's same solution in forum, but no thought flow explain, so hard to understand!
        XXX: Good example of DFS's Traversal. Different from my approach!
              5   -- can be any number
          /       \
         3         7   -- can be any number as long as it's greater than 5
                  /  \
                 4    8
        Since each node just checked once, so T: O(N)
        """

        def dfs(T: Optional[TreeNode], lo, hi) -> bool:
            if not T:
                return True
            if not (lo < T.val < hi):
                return False

            return dfs(T.left, lo, T.val) and dfs(T.right, T.val, hi)

        return dfs(root, float("-inf"), float("inf"))

    def isValidBST_fxr(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 56 ms, faster than 28.66% of Python3 online submissions for Validate Binary Search Tree.

        Time Submitted
        10/03/2021 20:30	Accepted	56 ms	17 MB	python3
        10/03/2021 20:29	Wrong Answer	N/A	N/A	python3
        10/03/2021 16:17	Wrong Answer	N/A	N/A	python3
        10/03/2021 16:00	Wrong Answer	N/A	N/A	python3
        10/03/2021 15:58	Wrong Answer	N/A	N/A	python3
        """

        def mn(nums):
            ret = float("inf")
            for n in nums:
                if not n:
                    continue
                ret = min(n, ret)
            return ret

        def mx(nums):
            ret = float("-inf")
            for n in nums:
                if not n:
                    continue
                ret = max(n, ret)
            return ret

        def dc(root: Optional[TreeNode]):
            # base
            if not root:
                return True, None, None
            if not root.left and not root.right:
                return True, root.val, root.val
            # divide
            # conquer
            check_l, mn_l, mx_l = dc(root.left)
            check_r, mn_r, mx_r = dc(root.right)

            # combine
            if not (check_l and check_r):
                return False, None, None
            if not ((not mx_l or root.val > mx_l) and (not mn_r or root.val < mn_r)):
                return False, None, None
            return True, mn([root.val, mn_l]), mx([mx_r, root.val])

        check, mn, mx = dc(root)
        print(check, mn, mx)
        return check


root = TreeNode(
    5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6))
)

root1 = TreeNode(5, left=TreeNode(14, left=TreeNode(1)))

root2 = TreeNode(
    5, left=TreeNode(3), right=TreeNode(7, left=TreeNode(4), right=TreeNode(8))
)
sl = Solution()
print(sl.isValidBST(root))
print(sl.isValidBST(root1))
print(sl.isValidBST(root2))
