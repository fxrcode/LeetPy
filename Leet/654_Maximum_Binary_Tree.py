"""
✅ GOOD Mono-stack
Tag: Medium, DFS, Stack
Lookback:
- from #427. Quad-Tree discuss 
- This is also called a Cartesian Tree. One interesting property is that if we do an in-order traversal, we get the array back which we used to create it.

"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def tom0727():
            """
            Runtime: 176 ms, faster than 99.66% of Python3 online submissions for Maximum Binary Tree.

            https://leetcode.com/problems/maximum-binary-tree/discuss/316286/Python-O(n)-Solution-with-explanation
            XXX: nice thought process
            """
            stack = []

            for i in nums:
                n = TreeNode(i)
                lastpop = None
                while stack and i > stack[-1].val:
                    lastpop = stack.pop()
                n.left = lastpop

                if stack:
                    stack[-1].right = n
                stack.append(n)

            return stack[0]

        def fxr():
            """
            Runtime: 209 ms, faster than 89.86% of Python3 online submissions for Maximum Binary Tree.
            T: O(N^2)
            """

            def dfs(l, r):
                if l == r:
                    return TreeNode(nums[l])
                if l > r:
                    return None
                mx = -1
                mxi = -1
                for i in range(l, r + 1):
                    if nums[i] > mx:
                        mx = nums[i]
                        mxi = i
                subl, subr = dfs(l, mxi - 1), dfs(mxi + 1, r)
                return TreeNode(mx, subl, subr)

            return dfs(0, len(nums) - 1)
