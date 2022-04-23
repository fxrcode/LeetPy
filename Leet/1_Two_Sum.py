'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
Leetcode Explore: Hash Table. Practical Application - HashMap
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Notes: https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
* In general, sum problems can be categorized into two categories:
1) there is any array and you add some numbers to get to (or close to) a target,
2) you need to return indices of numbers that sum up to a (or close to) a target value. Note that when the problem is looking for a indices, sorting the array is probably NOT a good idea.
'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Your runtime beats 49.30 % of python3 submissions.
        AC in 1, with coding basics
        """
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target-n], i]
            if n not in d:
                d[n] = i
        return [-1, -1]


sl = Solution()
print(sl.twoSum([3, 3], 6))
print(sl.twoSum([11, 2, 7, 5], 9))
