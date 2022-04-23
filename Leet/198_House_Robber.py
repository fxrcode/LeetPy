'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
✅ GOOD DP (1D)
'''


from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def os_memoization():
            """
            Runtime: 47 ms, faster than 16.37% of Python3 online submissions for House Robber.

            T: O(N), M: O(N)
            """
            @cache
            def rob_from(i):
                if i >= len(nums):
                    return 0
                return max(nums[i] + rob_from(i+2), rob_from(i+1))
            return rob_from(0)

        def os_tabular():
            """
            Runtime: 51 ms, faster than 12.34% of Python3 online submissions for House Robber.

            T: O(N), M: O(N)
            """
            if not nums:
                return 0
            n = len(nums)
            dp = [0]*(n+1)
            dp[n-1] = nums[n-1]
            for i in range(n-2, -1, -1):
                dp[i] = max(dp[i+1], dp[i+2]+nums[i])
            return dp[0]

        def os_tabular_optimized():
            """
            Runtime: 51 ms, faster than 12.34% of Python3 online submissions for House Robber.

            T: O(N), M: O(N)
            """
            if not nums:
                return 0
            n = len(nums)
            dp_i_1, dp_i_2 = 0, 0
            for i in range(n-1, -1, -1):
                dp = max(dp_i_1, dp_i_2+nums[i])
                dp_i_1, dp_i_2 = dp, dp_i_1
            return dp

        # return os_memoization()
        return os_tabular_optimized()

        def huahua():
            """
            Runtime: 32 ms, faster than 75.96% of Python3 online submissions for House Robber.

            REF: huahua's DP playlist (105/134)
            """
            if not nums or len(nums) < 1:
                return 0

            F = [0 for _ in range(len(nums))]
            for i in range(len(nums)):
                F[i] = max(
                    (F[i-2] if i >= 2 else 0) + nums[i],
                    (F[i-1] if i >= 1 else 0)
                )
            return F[-1]
        '''
        F = {}

        def rob_from(i):
            """
            Runtime: 66 ms, faster than 5.43% of Python3 online submissions for House Robber.

            XXX: OS: no need greedy, simply try all combination then max.
            backword thinking, rob_from is max profit of suffix houses.
            So it's clean and easy.
            """
            if i >= len(nums):
                return 0
            if i in F:
                return F[i]
            rob_cur = nums[i] + rob_from(i+2)
            not_rob_cur = rob_from(i+1)
            ans = max(rob_cur, not_rob_cur)
            F[i] = ans
            return ans

        return rob_from(0)
        '''

        '''
        def rec(i):
            """
            Runtime: 45 ms, faster than 29.84% of Python3 online submissions for House Robber.

            AC in 2, due to base case.
            XXX: rec(i): means the max profit that we rob till i, and i must be robbed.
                This is forward thinking.
            """
            if i in F:
                return F[i]
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            one_pre = rec(i-1)
            two_pre = rec(i-2) + nums[i]
            ans = max(one_pre, two_pre)
            F[i] = ans
            return ans

        return rec(len(nums)-1)
        '''


sl = Solution()
print(sl.rob(nums=[2, 7, 9, 3, 1]))
# print(sl.rob(nums=[2, 1]))
print(sl.rob(nums=[12, 7, 100, 1000, 100]))
