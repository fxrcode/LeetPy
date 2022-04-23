"""
tag: easy
Lookback:
"""
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        def fxr():
            cnt = 0
            for s, e in zip(startTime, endTime):
                # Runtime: 70 ms, faster than 21.05% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
                if s <= queryTime <= e:
                    cnt += 1
            return cnt
