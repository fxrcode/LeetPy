"""
Tag: Medium
Lookback: daily challenge @ 03282024
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        def fxr():
            """
            solution: The decision to check frequency[nums[end]] > k in the while loop is grounded in
            the fact that frequency[nums[end]] has already been updated within the for loop. This means
            that only the frequency of the current element (nums[end]) could be greater than k and thus
            is being assessed for compliance with the goodness condition.
            """
            d = defaultdict(int)
            l, r = 0, 0
            res = 0
            while r < len(nums):
                e = nums[r]
                r += 1
                d[e] += 1
                # while l < r and max(d.values()) > k:  # when invalid, keep shrinking
                while l < r and d[e] > k:
                    b = nums[l]
                    l += 1
                    d[b] -= 1
                res = max(res, r - l)
            return res

        return fxr()


sl = Solution()
print(sl.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(sl.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(sl.maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
