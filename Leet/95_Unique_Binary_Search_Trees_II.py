"""
Leetcode Explore Recursion I - Conclusion
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""
# Definition for a binary tree node.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """[summary]
        Runtime: 83 ms, faster than 32.91% of Python3 online submissions for Unique Binary Search Trees II.
        """

        def recur(start, end) -> List[Optional[TreeNode]]:
            if start > end:
                # BUG: return []
                # I return empty list which seems meaningful, but the result is wrong, say, n = 3, the final result is [[2,1,3]
                #   The reason is: if return [], then back to upper recursion tree, the callee will get res_l = [], so the inner loop will be skipped
                #   therefore the tree is not built and saved in res!
                #   See detail explain in post: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/929000/Recursive-solution-long-explanation
                # None in python is a singleton object itself!
                return [None]
            # XXX: UCB: half-armed recursion!
            # if start == end:
            #     return [TreeNode(start)]
            res = []
            for v in range(start, end + 1):
                # BUG: root = TreeNode(v)
                res_l = recur(start, v - 1)
                res_r = recur(v + 1, end)
                for rl in res_l:  # inner loop
                    for rr in res_r:
                        root = TreeNode(v)
                        root.left, root.right = rl, rr
                        res.append(root)

            return res

        return recur(1, n)
