"""
from #1359
tag: easy, math
Lookback
- not familiar with indexing, always fuzzy on base-0 vs base-1.
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        def jankit_O1():
            weeks, days = divmod(n, 7)
            if weeks == 0:
                return n * (n + 1) // 2
            weekly = sum(range(1, 8))  # base dollar/week
            tot = weekly * weeks  # total dollar/week without extra 1 per next Monday
            tot += weeks * (weeks - 1) * 7 // 2  # add the incr for extra money
            extra = weeks + 1  # start the next week money

            tot += days * (days - 1) // 2 + extra * days
            return tot

        def fxr():
            total = 0
            for d in range(1, n + 1):
                i, j = divmod(d - 1, 7)
                money = i + (j + 1)
                total += money
            return total

        # return fxr()
        return jankit_O1()


sl = Solution()
for n in [4, 10, 20]:
    print(sl.totalMoney(n))
