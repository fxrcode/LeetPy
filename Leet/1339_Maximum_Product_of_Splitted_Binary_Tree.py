"""
Tag: Medium, DFS
Lookback:
- AC in 10min
- I found the re-state: split Tree into subtree and its complement part. 
    - I used sort subsum list by closest to total_sum//2. O(nlogn)
    - actually, we can do linear search O(N)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def fxr():
            """
            Runtime: 304 ms, faster than 96.69% of Python3 online submissions for Maximum Product of Splitted Binary Tree.

            """
            total = 0
            sms = []

            def dfs(T: TreeNode):
                if not T:
                    return 0
                l, r = dfs(T.left), dfs(T.right)
                smT = l + r + T.val
                sms.append(smT)
                return smT

            MOD = 10**9 + 7
            total = dfs(root)
            ans = 0
            for s in sms:
                ans = max(ans, s * (total - s))
            return ans % MOD

        return fxr()
