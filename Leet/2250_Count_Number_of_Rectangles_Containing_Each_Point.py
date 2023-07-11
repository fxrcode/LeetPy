"""
✅ GOOD (1st time input data scale as condition)
Tag: Medium, Hash, Bisect
Lookback:
- Worst students start solving w/o fully understand the problem (include conditions, questions)
- I implemented use sort + bisect, but TLE on 41 / 47 test cases passed.
"""
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def countRectangles(
        self, rectangles: List[List[int]], points: List[List[int]]
    ) -> List[int]:
        def a13r1():
            """
            Runtime: 3690 ms, faster than 40.00% of Python3 online submissions for Count Number of Rectangles Containing Each Point.
            T: O(RlogR + PlogR)
            """
            rectangles.sort()
            h2l = defaultdict(list)
            for l, h in rectangles:
                h2l[h].append(l)
            cnt = [0] * len(points)
            for i, xy in enumerate(points):
                x, y = xy
                for h in range(y, 101):
                    cnt[i] += len(h2l[h]) - bisect_left(h2l[h], x)
            return cnt

        return a13r1()


sl = Solution()
print(sl.countRectangles(rectangles=[[1, 2], [2, 3], [2, 5]], points=[[2, 1], [1, 4]]))
print(sl.countRectangles(rectangles=[[1, 1], [2, 2], [3, 3]], points=[[1, 3], [1, 1]]))
print(
    sl.countRectangles(
        [[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [5, 9]],
        [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]],
    )
)
