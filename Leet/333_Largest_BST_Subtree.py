"""
tag: medium, BST, dfs
Lookback:
* Common BST trick: return subtree (min,max)
    1. None node is valid, return (+inf, -inf), so its parent's validation pass.
    2. invalid BST, return (-inf, +inf), so its parent fail validation
    3. +/- inf works with normal range update: min(l_mn, T.val), max(r_mx, T.val)
* nice OS analysis: pre-order O(N^3) vs post-order O(N)

Similar:
98. Validate Binary Search Tree
1373. Maximum Sum BST in Binary Tree
can you can break at most 1 edge to make it BST? (TuSimple)

Weekly Special (Nov W5)

✅ GOOD DFS (multiple return)
❌ SUCKS (bad in Tree DFS)
[ ] REDO
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def os3():
            def dfs(T: TreeNode):
                """
                Runtime: 65 ms, faster than 63.79% of Python3 online submissions for Largest BST Subtree.

                get max BST in subtree T, and return its range

                'T' as treenode, learned from CP4: https://github.com/stevenhalim/cpbook-code/blob/master/ch2/nonlineards/AVL.cpp
                """
                if not T:
                    return 0, float("inf"), float("-inf")  # BST trick

                l_n, l_min, l_max = dfs(T.left)
                r_n, r_min, r_max = dfs(T.right)

                if l_max < T.val < r_min:
                    return (
                        l_n + r_n + 1,
                        min(l_min, T.val),
                        max(r_max, T.val),
                    )  # BST trick
                else:
                    # BUG: return 0, -inf, +inf
                    return max(l_n, r_n), float("-inf"), float("inf")  # BST trick

            return dfs(root)[0]
