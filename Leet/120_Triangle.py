'''
✅ GOOD DP (2D): Reverse thinking! Flip triangle!

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
'''
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def os_reverse_triangle():
            """
            Runtime: 60 ms, faster than 94.60% of Python3 online submissions for Triangle.

            XXX: OS: Interview Tip: Practice Overriding Your Brains "Assume" Mode!
            """
            n = len(triangle)
            below_row = triangle[-1]
            for r in reversed(range(n-1)):
                cur_row = []
                for c in range(r+1):
                    cur_row.append(triangle[r][c] +
                                   min(below_row[c], below_row[c+1]))
                below_row = cur_row
            return below_row[0]

        def fxr():
            """
            Runtime: 80 ms, faster than 36.28% of Python3 online submissions for Triangle.

            XXX: how to be creative as OS? Polya: learn every trick/thoughtflow from them, and use it!
            """
            n = len(triangle)
            for i in range(1, n):
                for j in range(len(triangle[i])):

                    # learned pythonic list generator from 931. Minimum Falling Path Sum
                    triangle[i][j] += min(triangle[i-1][k]
                                          for k in [j-1, j] if 0 <= k < len(triangle[i-1]))
            return min(triangle[-1])

        # return fxr()
        return os_reverse_triangle()


sl = Solution()
print(sl.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
