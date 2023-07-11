"""
FB tag 
tag: easy, bisect
lookback:
- young tableau => bisect, or staircase (symmetric logic!)
++++++--
++++----
++++----
+++-----
+-------
+-------

Similar:
240. Search a 2D Matrix II 
1428. Leftmost Column with at Least a One
"""

from bisect import bisect_left
from typing import List


class Solution:
    def countNegatives(self, G: List[List[int]]) -> int:
        def rock_top_right():
            """
            Runtime: 172 ms, faster than 53.36% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

            https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510249/JavaPython-3-2-similar-O(m-%2B-n)-codes-w-brief-explanation-and-analysis.

            XXX: count '-' in current COLUMN, if start from top-right
            """
            m, n = len(G), len(G[0])
            r, c, cnt = 0, n - 1, 0
            while r < m and c >= 0:
                if G[r][c] < 0:
                    cnt += m - r
                    c -= 1
                else:
                    r += 1
            return cnt

        def fxr_bottom_left():
            """
            Runtime: 116 ms, faster than 77.06% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
            XXX: count '-' in this row, if start from bottom-left
            T: O(m+n)
            """
            m, n = len(G), len(G[0])
            i, j = m - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if G[i][j] < 0:
                    cnt += n - j
                    i -= 1
                else:
                    j += 1
            return cnt

        def fxr_bisect():
            def bi(row: list[int]):
                """
                Runtime: 116 ms, faster than 77.06% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

                T: O(nlogm)
                """
                # BUG: l,r = 0, len(row)-1. search space is [0...len(row)] since len(row) means all >= 0!
                l, r = 0, len(row)
                while l < r:
                    mid = (l + r) // 2
                    if row[mid] < 0:
                        r = mid
                    else:
                        l = mid + 1
                return len(row) - l

            cnt = 0
            for row in G:
                cnt += bi(row)
            return cnt

        return fxr_bisect()


sl = Solution()
print(
    sl.countNegatives(
        G=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    )
)
print(sl.countNegatives([[3, 2], [1, 0]]))
