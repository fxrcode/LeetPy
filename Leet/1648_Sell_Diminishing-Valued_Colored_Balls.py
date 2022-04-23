"""
✅ GOOD Bisect (Indirect)
Amazon Top50
tag: Medium, Greedy, Bisect, Skills
Lookback:
- I did it in simulation, idea is same as bisect-balls, but impl logic is nasty compare to ye15.
Similar:
- 2141. Maximum Running Time of N Computers
"""

from bisect import bisect_left
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def ye15():
            """
            Runtime: 3411 ms, faster than 5.05% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.

            https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927560/c-binary-answer-or-sortgreedy
            """
            fn = lambda x: sum(max(0, xx - x) for xx in inventory)  # balls sold

            # bisect_left (first True)
            lo, hi = 0, max(inventory)
            while lo < hi:
                mid = (lo + hi) // 2
                if fn(mid) < orders:  # FFFFTTT
                    hi = mid
                else:
                    lo = mid + 1

            ans = sum((x + lo + 1) * (x - lo) // 2 for x in inventory if x > lo)

            left = orders - fn(lo)
            ans += left * lo
            return ans % 1_000_000_007

        return ye15()

        def fxr(orders):
            """
            Runtime: 3865 ms, faster than 5.05% of Python3 online submissions for Sell Diminishing-Valued Colored Balls.

            """
            MOD = 10**9 + 7
            A = inventory
            A.sort()
            A = [0] + A
            r = len(A) - 1
            gain = 0

            def sm(v, num):
                last, fir = v, v - num + 1
                return (fir + last) * num // 2

            while orders:
                less_idx = bisect_left(A, A[r]) - 1
                less = A[less_idx]
                batch = r - less_idx
                diff = A[r] - less
                bought = min(orders, diff * batch)
                num_batch, last_batch = divmod(bought, batch)
                if num_batch:
                    for i in range(less_idx + 1, r + 1):
                        gain += sm(A[i], num_batch)
                        A[i] -= num_batch
                for i in range(less_idx + 1, less_idx + 1 + last_batch):
                    gain += A[i]
                    A[i] -= 1
                orders -= bought
                # for i in range(less_idx + 1, r + 1):
                #     if orders != 0 and A[i] > less:
                #         gain += A[i]
                #         A[i] -= 1
                #         orders -= 1
            return gain % MOD

        return fxr(orders)


sl = Solution()
print(sl.maxProfit(inventory=[1, 2, 2, 3, 5], orders=7))
print(sl.maxProfit(inventory=[2, 5], orders=4))
print(sl.maxProfit(inventory=[3, 5], orders=6))
print(sl.maxProfit([3, 5, 8, 10], 10))
print(sl.maxProfit([1000000000], 1000000000))
