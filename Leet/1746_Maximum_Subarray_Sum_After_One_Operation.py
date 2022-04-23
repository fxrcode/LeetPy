'''
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
'''


from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        def fxr_dp():
            """
            Runtime: 1560 ms, faster than 18.81% of Python3 online submissions for Maximum Subarray Sum After One Operation.

            AC in 1! (inspired from 376. Wiggle Subsequence & 309. Best Time to Buy and Sell Stock with Cooldown)
            Metacognition: T[n][0 or 1]
                0: till now, max subarray sum including nums[i]
                1: till now one item is squared in max subarray

            T: O(N), M: O(N)
            """
            n = len(nums)
            T = [[0]*2 for _ in range(n+1)]
            mx = nums[0]**2
            for i in range(1, n+1):
                T[i][0] = nums[i-1] + max(T[i-1][0], 0)
                T[i][1] = max(
                    nums[i-1]**2 + max(T[i-1][0], 0),
                    nums[i-1] + max(T[i-1][1], 0)
                )
                mx = max(mx, *T[i])
            return mx

        def fxr_kadane():
            """
            TLE: 24 / 57 test cases passed.

            T: O(N^2)
            """
            def kadane(A: list[int], i):
                cur = mx = A[0] if i != 0 else A[0]**2
                for j in range(1, len(A)):
                    n = A[j]
                    if j == i:
                        n = n**2
                    cur = max(n, n+cur)
                    mx = max(mx, cur)
                return mx
            ans = -1e6
            for i in range(len(nums)):
                ans = max(ans, kadane(nums, i))
            return ans

        # return fxr_kadane()
        return fxr_dp()


sl = Solution()
print(sl.maxSumAfterOperation(nums=[2, -1, -4, -3]))
print(sl.maxSumAfterOperation(nums=[1, -1, 1, 1, -1, -1, 1]))
