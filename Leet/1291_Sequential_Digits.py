"""
💡insight
Daily Challenge (Jan 22)
tag: sliding window

[ ] REDO
"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def os_window():
            """
            Runtime: 32 ms, faster than 62.30% of Python3 online submissions for Sequential Digits.

            """
            sample = "123456789"
            n = 10
            nums = []
            for le in range(len(str(low)), len(str(high)) + 1):
                for start in range(n - le):
                    v = int(sample[start : start + le])
                    if low <= v <= high:
                        nums.append(v)
            return nums

        return os_window()


sl = Solution()
print(sl.sequentialDigits(low=100, high=300))
print(sl.sequentialDigits(low=1000, high=13000))
