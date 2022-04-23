"""
FB tag (easy)
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def os():
            """
            Runtime: 1769 ms, faster than 14.95% of Python3 online submissions for Maximum Average Subarray I.

            T:O(N)
            """
            best = now = sum(nums[:k])
            for i in range(k, len(nums)):
                now += nums[i] - nums[i - k]
                best = max(best, now)
            return best / k

