"""
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
Leetcode explore - Array 101
Explore Array & String: 2 pointer technique

Given a binary array nums, return the maximum number of consecutive 1's in the array.


"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        AC in 1st try. T:O(N)
        """
        count, result = 0, 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                result = max(result, count)

        return result
