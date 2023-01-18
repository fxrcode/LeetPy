"""
Date: 01172023
Tag: Medium, DP, mono-queue, D&C
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

"""


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def hiepit_lee215():
            def maximumSubArray(nums):
                ans = nums[0]
                sumSoFar = 0
                for num in nums:
                    sumSoFar += num
                    ans = max(ans, sumSoFar)
                    if sumSoFar < 0:
                        sumSoFar = 0
                return ans

            def minimumSubArray(
                nums,
            ):  # the first element and the last element are exclusive!
                if len(nums) <= 2:
                    return 0
                ans = nums[1]
                sumSoFar = 0
                for i in range(1, len(nums) - 1):
                    sumSoFar += nums[i]
                    ans = min(ans, sumSoFar)
                    if sumSoFar > 0:
                        sumSoFar = 0
                return ans

            return max(maximumSubArray(nums), sum(nums) - minimumSubArray(nums))

        return hiepit_lee215()

        def lee215():
            """
            Runtime: 552 ms, faster than 60.31% of Python3 online submissions for Maximum Sum Circular Subarray.

            XXX: all followups are related to classic problem's solution!
                So is ALL leetcode, you just need to reduce them to classics (prerequisit: you're familiar with classics + top 500 Q's)

            REF: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
            """
            A = nums
            total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
            for a in A:
                curMax = max(curMax + a, a)
                maxSum = max(maxSum, curMax)
                curMin = min(curMin + a, a)
                minSum = min(minSum, curMin)
                total += a
            return max(maxSum, total - minSum) if maxSum > 0 else maxSum


sl = Solution()
# print(sl.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
# print(sl.maxSubarraySumCircular(nums=[3, -1, 2, -1]))
# print(sl.maxSubarraySumCircular(nums=[5, -3, 5]))
print(sl.maxSubarraySumCircular([-2, -3, -1]))
