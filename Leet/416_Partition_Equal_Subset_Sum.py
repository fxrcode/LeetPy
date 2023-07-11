"""

Daily Challenge (Dec 12)

✅ GOOD DP (knapsack partition)
✅ GOOD DFS (backtrack)

Meta-cognition
* proficiently draw recursion tree to fully understand!!!
* don't be stuck in dfs template! Get deeper understand of DFS!
* when it says subset, you don't need to use subset backtrack template! Be robust! Why? Because we only needs T/F, rather ALL subsets!
* order matters in DP optimization, so you'd better write out DP table for case analyze to understand dependencies.

similar:
- 1774
"""

from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def os_memo():
            """
            with @cache: Runtime: 1344 ms, faster than 50.61% of Python3 online submissions for Partition Equal Subset Sum.
            without memo: TLE: 36 / 117 test cases passed.

            """

            @cache
            def rec(i, subset_sum):
                print(i, subset_sum)
                # base
                if subset_sum == 0:
                    return True
                if i == len(nums) or subset_sum < 0:
                    return False
                # BUG: check recursion tree, it might hit i = len, and also he = 0, should return True!
                # if he == 0:
                #     return True

                # recur
                return rec(i + 1, subset_sum - nums[i]) or rec(i + 1, subset_sum)

            sm = sum(nums)
            if sm % 2 == 1:
                return False
            return rec(0, sm // 2)

        # return os_brute()
        def os_dp():
            n, sm = len(nums), sum(nums)
            if sm % 2 == 1:
                return False
            hm = sm // 2

            T = [[False] * (hm + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                T[i][0] = True
            for i in range(n - 1, -1, -1):
                cur = nums[i]
                for j in range(hm + 1):
                    if j < cur:
                        T[i][j] = T[i + 1][j]
                    else:
                        T[i][j] = T[i + 1][j] or T[i + 1][j - cur]
            return T[0][hm]

        def os_optimized_dp():
            """
            Runtime: 2708 ms, faster than 27.22% of Python3 online submissions for Partition Equal Subset Sum.

            IN OS, by drawing out the DP table process, we analyze the order of update DP.
            So we can optimize space from m*n -> 2*n => 1*n!
            Here I just write the 2xN version
            """
            n, sm = len(nums), sum(nums)
            if sm % 2 == 1:
                return False
            hm = sm // 2

            T = [[False] * (hm + 1) for _ in range(2)]
            for i in range(2):
                T[i][0] = True
            for i in range(n - 1, -1, -1):
                cur = nums[i]
                for j in range(hm + 1):
                    if j < cur:
                        T[i % 2][j] = T[(i + 1) % 2][j]
                    else:
                        T[i % 2][j] = T[(i + 1) % 2][j] or T[(i + 1) % 2][j - cur]
            return T[0 % 2][hm]

        # return os_dp()
        return os_optimized_dp()


sl = Solution()
# print(sl.canPartition(nums=[1, 2, 3, 4]))
print(sl.canPartition(nums=[1, 2, 5]))
