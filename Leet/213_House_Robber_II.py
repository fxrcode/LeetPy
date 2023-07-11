"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Runtime: 28 ms, faster than 88.53% of Python3 online submissions for House Robber II.

        T: O(N), M: O(1)
        """

        def rob_range(start, end):
            dp_i_1, dp_i_2 = 0, 0
            # although for internal dp can be refered outside of for, but in case loop range is EMPTY!
            dp = 0
            for i in range(end, start - 1, -1):
                dp = max(dp_i_1, dp_i_2 + nums[i])
                dp_i_1, dp_i_2 = dp, dp_i_1
            return dp

        N = len(nums)
        if N == 1:
            return nums[0]
        return max(
            rob_range(0, N - 2),
            rob_range(1, N - 1),
        )

        '''
        def rob_from(i, vals):
            """
            Runtime: 60 ms, faster than 8.67% of Python3 online submissions for House Robber II.

            AC in 2, due to edge case: nums = [1]
            XXX: why so slow still? even with memo?
            """
            if i >= len(vals):
                return 0
            if i in F:
                return F[i]
            F[i] = max(vals[i] + rob_from(i+2, vals), rob_from(i+1, vals))
            return F[i]

        if len(nums) < 2:
            return max(nums)

        A, B = nums[1:], nums[:-1]
        max_A = rob_from(0, A)
        F.clear()
        max_B = rob_from(0, B)
        return max(max_A, max_B)
        '''


sl = Solution()
# print(sl.rob(nums=[2, 3, 2]))
# print(sl.rob(nums=[1, 2, 3, 1]))
# print(sl.rob(nums=[1, 2, 3]))
print(sl.rob([1]))
print(sl.rob([]))
