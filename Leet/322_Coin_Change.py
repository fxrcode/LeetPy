"""
✅ GOOD DP
Tag: Medium, BFS, DP
Lookback:
- when INF, use float('inf'), rather 2e9, cuz INF+anything still INF, but 2e9 can be increased.
- reminds me 991, 1654
"""

from collections import deque
from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp_dbabichev():
            """
            Runtime: 2159 ms, faster than 37.65% of Python3 online submissions for Coin Change.

            classic DP problem
            T: O(amount*coins)
            """
            INF = float("inf")

            @cache
            def dp(i):
                if i == 0:
                    return 0
                if i < 0:
                    # BUG: return 2e9
                    # XXX: INF+anything => INF.
                    return INF
                return min(dp(i - c) + 1 for c in coins)

            return dp(amount) if dp(amount) != INF else -1

        def fxr_bfs():
            """
            Runtime: 489 ms, faster than 99.43% of Python3 online submissions for Coin Change.

            """
            q = deque([0])
            vis = set(q)
            coins.sort()
            step = 0
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u == amount:
                        return step
                    for c in coins:
                        v = u + c
                        if v in vis:
                            continue
                        if v > amount:
                            break
                        vis.add(v)
                        q.append(v)
                step += 1
            return -1

        # return fxr_bfs()
        return dp_dbabichev()


sl = Solution()
print(sl.coinChange(coins=[1, 2, 5], amount=11))
print(sl.coinChange(coins=[2], amount=3))
print(sl.coinChange(coins=[1], amount=0))
