"""
tag: Easy
Lookback:
- how to neat code? (handle edge case?)
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def rock():
            """
            https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/451290/JavaPython-3-O(n)-and-O(logn)-codes-w-brief-explanation-and-analysis.
            """

            def freq(v):
                return bisect_right(arr, v) - bisect_left(arr, v)

            n = len(arr)
            k = max(1, n // 4)
            for i in range(0, n, k):
                if freq(arr[i]) > n // 4:
                    return arr[i]

        return rock()


sl = Solution()
print(sl.findSpecialInteger([1, 1]))
