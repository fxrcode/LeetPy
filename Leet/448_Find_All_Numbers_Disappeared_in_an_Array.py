'''
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
leetcode explore: Array 101. Conclusion
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Note: template: include 1st encounter reason (from book? explore? huahua list?)
As well as question, my notes, reference
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            # BUG: if nums[n-1] > 0: after 1 week, I made the same mistake again!
            k = abs(n)-1
            if nums[k] > 0:
                nums[k] *= -1
        print(nums)
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res


sl = Solution()
nns = [[1, 1], [4, 3, 2, 7, 8, 2, 3, 1]]
for n in nns:
    print(sl.findDisappearedNumbers(n))
