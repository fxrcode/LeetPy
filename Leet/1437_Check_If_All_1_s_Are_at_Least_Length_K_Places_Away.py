"""
tag: easy, skills
Lookback:
- I stucked a bit on prev, cur 2ptr. Actually, we just need prev.
"""

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        def fxr():
            """
            Runtime: 624 ms, faster than 74.33% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
            T: O(N)
            """
            prev = -1
            for i, n in enumerate(nums):
                if n != 1:
                    continue
                if prev != -1:
                    if i - prev - 1 < k:
                        return False
                prev = i
            return True

        return fxr()


sl = Solution()
print(sl.kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(sl.kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
