"""
✅ GOOD DP (re-state, discretize)
Daily challenge (Mar 5, 2022)
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

tag: medium, DP
Lookback:
- reduce problem by re-state, then it becomes disguise 198. House Robber (knapsack state vs choice)!
- how to find this reduction? The problem is relate to nums[i] +/- 1, rather given nums' order!
- similar reduction found in medium/hard problem
    - 1035. Uncrossed line (disguise LCS)
    - 296. Best meeting point (from 1D median [2033])
    - 1901. Find a peak Element II (from 1D peak [162])
- 1st time Discretize
"""


from collections import Counter
from functools import cache
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def os_discretize():
            """
            Runtime: 99 ms, faster than 35.95% of Python3 online submissions for Delete and Earn.

            discretize is to optimize space, rather time!
            """
            points = Counter(nums)
            mx = max(nums)
            # print(points, mx)

            @cache
            def rob(v) -> int:
                if v > mx:
                    return 0
                return max(points[v] * v + rob(v + 2), rob(v + 1))

            return rob(min(nums))

        def huahua_rob():
            """
            Runtime: 60 ms, faster than 74.13% of Python3 online submissions for Delete and Earn.

            REF: huahua https://www.youtube.com/watch?v=YzZd-bsMthk&list=PLLuMmzMTgVK7vEbeHBDD42pqqG36jhuOr
            ! disguise 198. Hourse Robber.
            The key is Understanding the problem, so as to reduce to 198.
            """

            # def rob(vals):
            #     n = len(vals)
            #     F = [0] * n
            #     for i in range(n):
            #         F[i] = max((F[i - 2] if i - 2 >= 0 else 0) + vals[i], (F[i - 1] if i - 1 >= 0 else 0))
            #     return F[-1]

            @cache
            def rob(i) -> int:
                """
                MIT: rob returns max profit by robbing suffix houses[i:]
                Set aspect to understand DP (yxc): at pos i, you have 2 choices: rob vs skip.
                """
                if i >= len(A):
                    return 0
                return max(A[i] + rob(i + 2), rob(i + 1))

            A = [0] * (max(nums) + 1)
            for v in nums:
                A[v] += v

            return rob(0)

        # return huahua_rob()
        return os_discretize()


sl = Solution()
print(sl.deleteAndEarn(nums=[3, 4, 2]))
print(sl.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
