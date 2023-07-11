"""
Weekly Contest 268 (Nov 20, 2021)

Metacognition: I only solved first 2 problems, directly skip 3rd without trying
    cuz I thought its Segment/Fenwick Tree. Should have try brute-force at least!
    Spent last 1hr on this 4th problem.

Top-1	uwi  	score:18	time: 0:12:21
"""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.idexs = defaultdict(list)
        for i, v in enumerate(arr):
            self.idexs[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        """
        Runtime: 1504 ms, faster than 100.00% of Python3 online submissions for Range Frequency Queries.

        XXX: better use bisect_left & bisect_right
        """
        indexs = self.idexs[value]
        left_idx = bisect_left(indexs, left)
        right_idx = bisect_right(indexs, right)
        return right_idx - left_idx

    def query_WA(self, left: int, right: int, value: int) -> int:
        full = self.idexs[value]
        if right < full[0] or left > full[-1]:
            return 0
        l = bisect_left(full, left)
        r = bisect_left(full, right)
        cnt = max(1, r - l)
        print(cnt, l, r)
        return cnt


"""
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
"""

"""
["RangeFreqQuery","query","query","query","query"]
[[[1,1,1,2,2]],[0,1,2],[0,2,1],[3,3,2],[2,2,1]]
"""
"""
sl = RangeFreqQuery(arr=[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
sl.query(1, 2, 4)
sl.query(0, 11, 33)
"""

A = [0, 5, 5, 9, 13]
print(bisect_left(A, 5))
print(bisect_left(A, 15))
print(bisect_right(A, 5))
print(bisect_right(A, 15))
