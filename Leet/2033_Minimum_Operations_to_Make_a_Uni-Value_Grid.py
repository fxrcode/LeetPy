"""
✅ GOOD Median index (Quick select O(N))


Similar: 
296. Best Meeting Point
1478. Allocate Mailboxes.

tag: medium, Math

Lookback:
- Jingying's mock (Dec 7, 2021) when you try to find pattern of problem, try position 0, last, avg/median position
    or the positions given! Don't stuck at one guess
"""


from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def bixing():
            """
            Runtime: 2553 ms, faster than 21.55% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.

            https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid/solution/zhong-wei-shu-by-endlesscheng-p0vj/
            https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/discuss/1513490/Intuition-on-why-we-need-the-median
            * Why target is one of the element? Why the median-index element?
            proof: why median? https://asvrada.github.io/blog/median-shortest-distance-sum/
            """

            def min_ops(grid: list[list[int]], target, x):
                ops = 0
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        dist = abs(grid[i][j] - target)
                        if dist % x != 0:
                            return -1
                        else:
                            ops += dist // x
                return ops

            m, n = len(grid), len(grid[0])
            if m == 1 and n == 1:
                return 0

            arr = []
            for row in grid:
                arr.extend(row)
            arr.sort()

            cand1 = arr[len(arr) // 2]
            cand2 = arr[len(arr) // 2 - 1]

            return min(min_ops(grid, can, x) for can in [cand1, cand2])

        def median_cn():
            """
            https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid/solution/2033huo-qu-dan-zhi-wang-ge-de-zui-xiao-c-42fw/
            """
            line, col, ret, li = len(grid), len(grid[0]), 0, []
            for row in grid:
                li.extend(row)
            li.sort()
            mid = li[len(li) // 2]
            for v in li:
                if abs(mid - v) % x:
                    return -1
                ret += abs(mid - v) // x
            return ret
