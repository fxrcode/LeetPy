"""
Daily Challenge (Dec 17)

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""

import pprint
from collections import defaultdict
from typing import List


class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        def daily():
            """
            Runtime: 337 ms, faster than 16.63% of Python3 online submissions for Maximal Square.
            XXX: life is short, use defaultdict to automatically handle OOR index, ie. (-1,0), (-1,-1), (0,-1)
            T: O(mn), M: O(mn)
            """
            m, n = len(M), len(M[0])
            F = defaultdict(int)
            mx = 0
            for i in range(m):
                for j in range(n):
                    if M[i][j] == "0":
                        continue
                    F[i, j] = min(F[i - 1, j - 1], F[i - 1, j], F[i, j - 1]) + 1
                    mx = max(F[i, j], mx)
            pprint.pprint(F)
            return mx**2

        def fxr():
            self.max_sqr = 0
            """
            Runtime: 204 ms, faster than 78.75% of Python3 online submissions for Maximal Square.

            AC in 2. Debug from WA

            XXX: OS: optimize: init with F = list[m+1][n+1], so generalize the traverse!
            """
            m, n = len(M), len(M[0])
            F = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i * j == 0:
                        if M[i][j] == "1":
                            F[i][j] = 1
                            self.max_sqr = max(self.max_sqr, 1)

                    elif M[i][j] == "1":
                        F[i][j] = min(F[i - 1][j - 1], F[i - 1][j], F[i][j - 1]) + 1
                        self.max_sqr = max(self.max_sqr, F[i][j])

            return self.max_sqr**2

        # return fxr()
        return daily()


sl = Solution()
# matrix = [["0"]]
matrix = [["0", "1"], ["1", "0"]]
# matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# matrix = [["1", "0", "1", "0"], ["1", "0", "1", "1"],
#           ["1", "0", "1", "1"], ["1", "1", "1", "1"]]
print(sl.maximalSquare(matrix))
