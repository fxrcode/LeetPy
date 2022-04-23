'''
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
Leetcode explore - Array 101
Given an array nums of integers, return how many of them contain an even number of digits.
1<=nums[i] <=10^5
'''


from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for n in nums:
            # 10,1000
            if 10 <= n <= 99 or 1000 <= n <= 9999 or n == 100000:
                evens += 1
        return evens
