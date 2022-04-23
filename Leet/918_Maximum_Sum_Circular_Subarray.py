'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

'''


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maxSubarraySum(A: List[int]) -> int:
            """
            Runtime: 552 ms, faster than 60.31% of Python3 online submissions for Maximum Sum Circular Subarray.

            XXX: all followups are related to classic problem's solution!
                So is ALL leetcode, you just need to reduce them to classics (prerequisit: you're familiar with classics + top 500 Q's)

            REF: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
            """
            n = len(A)
            F = [0] * n
            F[0] = A[0]
            ans = F[0]
            for i in range(1, n):
                F[i] = (F[i-1] if F[i-1] > 0 else 0) + A[i]
                ans = max(ans, F[i])
            return ans

        maxSum = maxSubarraySum(nums)

        negNums = [-1*v for v in nums]
        maxNegSum = maxSubarraySum(negNums)
        minSum = -maxNegSum

        circMax = sum(nums) - minSum
        print(maxSum, circMax)

        if circMax == 0 and all([v <= 0 for v in nums]):
            return maxSum
        return max(maxSum, circMax)


sl = Solution()
# print(sl.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
# print(sl.maxSubarraySumCircular(nums=[3, -1, 2, -1]))
# print(sl.maxSubarraySumCircular(nums=[5, -3, 5]))
print(sl.maxSubarraySumCircular([-2, -3, -1]))
