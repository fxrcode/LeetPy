"""
✅ GOOD DP
Tag: Medium, DP, BFS
Lookback:
- similar to 474, classic knapsack
- Lagrange's four-square theorem
Similar
- 322
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/
Queue & Stack - Queue and BFS

"""
import math
import timeit
from collections import deque
from functools import cache


class Solution:
    def numSquares(self, n: int) -> int:
        def wantqiuc_bfs():
            """
            Runtime: 1580 ms, faster than 65.31% of Python3 online submissions for Perfect Squares.
            T: O(n√n)
            """
            evens = [i**2 for i in range(1, int(n**0.5) + 1)]

            d, q = 1, deque([n])
            while q:
                for _ in range(len(q)):
                    x = q.popleft()
                    for e in evens:
                        if x == e:
                            return d
                        if x < e:
                            break
                        q.append(x - e)
                d += 1
            return d

        def fxr_knapsack():
            """
            Runtime: 3713 ms, faster than 53.62% of Python3 online submissions for Perfect Squares.
            T: O(n√n)
            """
            evens = [i**2 for i in range(1, math.isqrt(n) + 1)]

            @cache
            def dp(i):
                if i == 0:
                    return 0
                if i < 0:
                    return float("inf")
                return min([dp(i - e) + 1 for e in evens if i >= e])

            return dp(n)

        # return fxr_knapsack()
        return wantqiuc_bfs()


sl = Solution()
for i in [12, 13, 3, 11, 7927]:  # [12]:  #
    print(sl.numSquares(i))

# XXX: how to use timeit: https://stackoverflow.com/questions/8727108/python-timeit-and-global-name-is-not-defined
# print(
#     timeit.timeit(
#         stmt="sl.numSquares(7927)",
#         setup="from __main__ import Solution; sl = Solution()",
#         number=3,
#     )
# )
