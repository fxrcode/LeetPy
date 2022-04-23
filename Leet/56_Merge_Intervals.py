"""
tag: sort, interval
Lookback:
- Daily Challenge (Dec 24)
- intervals 3 types: 1288, 56, 986
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def os():
            """
            https://leetcode.com/problems/merge-intervals/solution/
            """
            intervals.sort(key=lambda x: (x[0], -x[1]))
            merged = []
            for iv in intervals:
                if not merged or merged[-1][1] < iv[0]:
                    merged.append(iv)
                else:
                    merged[-1][1] = max(merged[-1][1], iv[1])
            return merged

        return os()


sl = Solution()
print(sl.merge([[1, 4], [1, 5]]))
assert sl.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
