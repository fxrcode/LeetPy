'''
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming

'''


from typing import List
from functools import cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def os_tabular():
            """
            Runtime: 64 ms, faster than 51.72% of Python3 online submissions for Paint House.

            """
            N, C = len(costs), len(costs[0])
            F = [[0]*C for _ in range(2)]
            F[(N-1) % 2] = costs[-1][:]
            print(F)
            for n in range(N-2, -1, -1):
                F[n % 2][0] = min([F[(n+1) % 2][c] for c in [1, 2]]) \
                    + costs[n][0]
                F[n % 2][1] = min([F[(n+1) % 2][c] for c in [0, 2]]) \
                    + costs[n][1]
                F[n % 2][2] = min([F[(n+1) % 2][c] for c in [0, 1]]) \
                    + costs[n][2]
                print(F)
            if len(costs) == 0:
                return 0
            return min(F[0])

        def os_memo():
            """
            Runtime: 74 ms, faster than 29.62% of Python3 online submissions for Paint House.

            T: O(N), M: O(N)
            """
            @cache
            def paint(i, c):
                if i >= len(costs):
                    return 0
                not_c = list(range(3))
                not_c.remove(c)
                return costs[i][c] + min([paint(i+1, n) for n in not_c])

            if not costs:
                return 0

            return min([paint(0, c) for c in range(3)])

        # return os_memo()
        return os_tabular()


sl = Solution()
print(sl.minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
# print(sl.minCost(costs=[[7, 6, 2]]))
