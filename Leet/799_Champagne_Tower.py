"""
Daily Challenge (Mar 4, 2022)
tag: medium, google
Lookback:
- Galton Board simulation is the better suit, rather Pascal Trangle. (But why latter got WA but quite close?)
"""


from functools import cache


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def hiepit_topdown():
            """
            https://leetcode.com/problems/champagne-tower/discuss/911964/JavaPython-Top-Down-DP-Clean-and-Concise-O(R-*-C)

            T: O(n^2)
            """

            @cache
            def dp(r, c):
                if c < 0 or c > r:
                    return 0
                if r == c == 0:
                    return poured
                return max(dp(r - 1, c - 1) - 1, 0) / 2 + max(dp(r - 1, c) - 1, 0) / 2

            return min(1, dp(query_row, query_glass))

        return hiepit_topdown()

        def os_dp():
            A = [[0] * k for k in range(1, 102)]
            A[0][0] = poured
            for r in range(query_row + 1):
                for c in range(r + 1):
                    q = (A[r][c] - 1.0) / 2.0
                    if q > 0:
                        A[r + 1][c] += q
                        A[r + 1][c + 1] += q
            return min(1, A[query_row][query_glass])

        return os_dp()

        '''
        def fxr_WA():
            """
            WA: 132 / 312 test cases passed.
            poured=25, query_row=6, query_glass=1. Ans=0.1875, My output=0.375
            """
            ratio = [1] * (query_row + 1)
            left = poured
            for r in range(query_row + 1):
                for c in range(r - 1, 0, -1):
                    ratio[c] += ratio[c - 1]
                print(ratio[: r + 1])
                left -= r
                if left == 0:
                    return 0
                print(left)
                if r == query_row:
                    return min(1, ratio[query_glass] / sum(ratio[: r + 1]) * left)
        '''

        # return fxr_WA()


sl = Solution()
# print(sl.champagneTower(poured=1, query_row=1, query_glass=1))
# print(sl.champagneTower(poured=2, query_row=1, query_glass=1))
# print(sl.champagneTower(poured=6, query_row=2, query_glass=1))
print(sl.champagneTower(poured=25, query_row=6, query_glass=1))

# print(sl.champagneTower(poured=100000009, query_row=33, query_glass=17))
