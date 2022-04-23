'''
Explore Array & String
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Your runtime beats 77.78 % of python3 submissions.
        XXX: didn't bug free in 1st, careful in coding basics, loop-invariant.
        """
        leftSum = 0
        S = sum(nums)
        for i in range(len(nums)):
            # print(leftSum, S)
            if leftSum * 2 == S-nums[i]:
                return i
            leftSum += nums[i]
        return -1


class PlayPrefixSum:
    @staticmethod
    def n_plus_1(nums):
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        print(presum)

    def exact_n(nums):
        # n = len(nums)
        # presum = [0] * n
        # for i in range()
        pass


numss = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [2, 1, -1]]
# for nums in numss:
#     PlayPrefixSum.n_plus_1(nums)

sl = Solution()
for nums in numss:
    print(sl.pivotIndex(nums))
