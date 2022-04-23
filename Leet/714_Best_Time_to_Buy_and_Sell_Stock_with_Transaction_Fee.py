'''
✅ GOOD DP (FSM)

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
💡insight
'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def fxr2():
            """
            Runtime: 996 ms, faster than 27.46% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

            XXX: Labuladong 团灭 LEETCODE 股票买卖问题
                You'd better do in DP table way, which reflects the insights of FSM DP, rather concise but miserable 2 vars DP.

            T: O(N), M: O(N)
            """
            # T[i][k][0/1]: ith day, maximum allowed tx allowed, 0:no stock, 1:has stock. T stands for Table (DP)
            N = len(prices)
            T = [[0]*2 for _ in range(N)]  # N-by-2
            for i in range(N):
                if i-1 == -1:
                    T[i][0] = 0
                    T[i][1] = -prices[i] - fee
                    continue
                T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i])
                T[i][1] = max(T[i-1][1], T[i-1][0] - prices[i]-fee)
            return T[N-1][0]

        def fxr():
            '''
            AC in 1!
            XXX: Thanks 309. Best Time to Buy and Sell Stock with Cooldown, I learned FSM DP!

            sold[i] = max(sold[i-1], hold[i-1]+price[i])  # BUG: no need to deduct since I've deduct when buy! -fee)
            held[i] = max(held[i-1], sold[i-1]-price[i]-fee)

            OS: At the end of the i-th day, we maintain `cash` (here fxr used sold), the maximum profit we could have if we did not have a share of stock
                and `hold`, the maximum profit we could have if we owned a share of stock.
            '''
            INF = 1e6
            sold, held = 0, -INF
            for p in prices:
                pre_sold = sold
                sold = max(sold, held+p)
                held = max(held, pre_sold-p-fee)
                print(p, sold, held)
            return max(sold, held)
        return fxr2()


sl = Solution()
print(sl.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(sl.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
