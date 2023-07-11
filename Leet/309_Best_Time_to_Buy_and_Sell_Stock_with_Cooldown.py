"""
✅ GOOD DP (FSM)

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def labuladong():
            """
            Runtime: 36 ms, faster than 93.14% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

            XXX: Labuladong 团灭 LEETCODE 股票买卖问题
                You'd better do in DP table way, which reflects the insights of FSM DP, rather concise but miserable 2 vars DP.
            """
            N = len(prices)
            T = [[0] * 2 for _ in range(N)]
            for i in range(N):
                # how to define what is base case? Simple: when T[i][0] is out-of-index
                # base I: i=0 is can be directly think out
                if i == 0:
                    T[i][0] = 0
                    T[i][1] = -prices[i]
                    continue
                # base II: i=1, need to consider i=0 for yesterday, so I simply calculate using the recurrence relation beflow
                #   since i-1 = 0, I can simply the recurrence with base I
                if i == 1:
                    T[i][0] = max(0, -prices[i - 1] + prices[i])
                    T[i][1] = max(-prices[i - 1], -prices[i])
                    continue

                T[i][0] = max(T[i - 1][0], T[i - 1][1] + prices[i])
                T[i][1] = max(T[i - 1][1], T[i - 2][0] - prices[i])
            return T[N - 1][0]

        def os():
            """
            Runtime: 28 ms, faster than 99.59% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

            XXX: FSM DP
            REF: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/
            REF: https://www.acwing.com/blog/content/4340/
            """
            INF = 1e6
            sold, held, reset = -INF, -INF, 0
            for p in prices:
                """
                sold[i] = held[i-1] + price[i]
                held[i] = max(held[i-1], reset[i-1] - price[i])
                reset[i] = max(reset[i-1], sold[i-1])
                """
                pre_sold = sold
                sold = held + p
                held = max(held, reset - p)
                reset = max(reset, pre_sold)
            return max(sold, reset)

        return labuladong()


sl = Solution()
print(sl.maxProfit(prices=[1, 2, 3, 0, 2]))
print(sl.maxProfit(prices=[1]))
