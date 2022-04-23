'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
Explore Array & String: 2 pointer technique

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Your runtime beats 99.25 % of python3 submissions.
        AC in 1.
        """
        l, r = 0, len(nums)-1
        while l < r:
            he = nums[l] + nums[r]
            if he < target:
                l += 1
            elif he > target:
                r -= 1
            else:
                break
        return [l+1, r+1]


sl = Solution()
print(sl.twoSum([2, 7, 11, 15], 9))
