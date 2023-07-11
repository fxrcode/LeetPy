"""
https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/1028/
Leetcode Explore: Binary Search - Template Analysis

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
"""

# Definition for a binary tree node.


from bisect import bisect_left
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = float("inf")

        def shaneTsui_bin_search(cur: TreeNode):
            """
            https://leetcode.com/problems/closest-binary-search-tree-value/discuss/183172/Elegant-Recursive-Python-solution
            Your runtime beats 76.64 % of python3 submissions.
            XXX: BST: search property + Tree recursion!
            """
            if not cur:
                return
            if abs(cur.val - target) < abs(self.closest - target):
                self.closest = cur.val

            if target < cur.val:
                shaneTsui_bin_search(cur.left)
            else:
                shaneTsui_bin_search(cur.right)

        shaneTsui_bin_search(root)
        return self.closest

        def inord_bisect():
            """
            Runtime: 62 ms, faster than 20.82% of Python3 online submissions for Closest Binary Search Tree Value.

            T: O(N+logN). M: O(N)
            """

            def inord(cur: TreeNode):
                if not cur:
                    return []
                return inord(cur.left) + [cur.val] + inord(cur.right)

            ino = inord(root)
            # min_dif, x = 1e6, -1
            # for n in ino:
            #     if abs(target-n) < min_dif:
            #         min_dif = abs(target-n)
            #         x = n

            # XXX: Common snippet: find closest value to target in sorted array
            # https://codereview.stackexchange.com/a/47344
            i = bisect_left(ino, target)
            if i == 0:  # smaller than any:
                return ino[0]
            elif i == len(ino):  # larger than any:
                return ino[-1]
            else:
                if ino[i] - target > target - ino[i - 1]:
                    return ino[i - 1]
                else:
                    return ino[i]

        return inord_bisect()
