"""
Weekly contest 290: Apr 23, 2022
2/4
Q3 conditions are HINT! But I missed it, so TLE
"""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        ls = [(i, rectangles[i][0]) for i in range(len(rectangles))]
        hs = [(i, rectangles[i][1]) for i in range(len(rectangles))]
        ls.sort(key=lambda x: x[1])
        hs.sort(key=lambda x: x[1])
        # points.sort()
        pi = [(i, points[i]) for i in range(len(points))]
        pi.sort(key=lambda x: x[1])
        cnt = [0] * len(points)
        li, hi = 0, 0
        for i, xy in pi:
            x, y = xy
            li = bisect_left(ls, x, key=lambda l: l[1])
            hi = bisect_left(hs, y, key=lambda h: h[1])
            setl = set([t[0] for t in ls[li:]])
            seth = set([t[0] for t in hs[hi:]])
            c = len(setl.intersection(seth))
            cnt[i] = c
        return cnt

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def dis(x, y, r, i, j):
            return sqrt((x - i) ** 2 + (y - j) ** 2) <= r

        ans = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if dis(x, y, r, i, j):
                        ans.add((i, j))
        return len(ans)

    def intersection(self, nums: List[List[int]]) -> List[int]:
        ss = [set(li) for li in nums]
        res = ss[0]
        for i in range(1, len(ss)):
            res.intersection_update(ss[i])
        return sorted(list(res))


sl = Solution()
print(sl.countRectangles(rectangles=[[1, 2], [2, 3], [2, 5]], points=[[2, 1], [1, 4]]))
print(sl.countRectangles(rectangles=[[1, 1], [2, 2], [3, 3]], points=[[1, 3], [1, 1]]))
print(
    sl.countRectangles(
        [[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [5, 9]],
        [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]],
    )
)
