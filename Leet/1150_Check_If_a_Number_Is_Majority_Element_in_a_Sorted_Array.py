'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
from bisect import bisect_left


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def top_vote():
            """
            Runtime: 28 ms, faster than 97.60% of Python3 online submissions

            XXX: using single binary search!
            """
            k = len(nums)//2
            if nums[k] != target:
                return False
            lo = bisect_left(nums, target)
            hi = lo + k
            return hi < len(nums) and nums[hi] == target

        def fxr_binary():
            """
            Runtime: 36 ms, faster than 77.26% of Python3 online submissions
            T:O(logN) with 2 binary search
            """
            l, r = bisect_left(nums, target), bisect_left(nums, target+1)
            print(l, r)
            return len(nums)//2 < r-l

        def fxr_WA():
            '''
            nums=[1,2,3,4,5], target=3
            '''
            n = len(nums)
            mid = n//2
            if n % 2 == 0:
                mid -= 1
            return target == nums[mid]
