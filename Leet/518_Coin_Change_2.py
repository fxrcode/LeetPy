"""
TuSimple: Lintcode 1834: Grouping Options (can be modeled as complete knapsack DP)
https://www.lintcode.com/problem/1834/solution/23055

"""


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def fxr_labuladong():
            """
            Runtime: 410 ms, faster than 36.51% of Python3 online submissions for Coin Change 2.

            """
            n = len(coins)
            # T[i][n] First i coin-types to make up n amount, T[...][0] = 1, T[0][...] = 0
            T = [0] * (amount + 1)
            for i in range(n + 1):
                T[0] = 1
            for i in range(1, n + 1):
                for j in range(1, amount + 1):
                    # use i-th coin
                    if j - coins[i - 1] >= 0:
                        T[j] = T[j] + T[j - coins[i - 1]]
                    # else:
                    #     T[i][j] = T[i-1][j]
            return T[amount]

        def fxr_labuladong_1():
            """
            Runtime: 729 ms, faster than 17.59% of Python3 online submissions for Coin Change 2.

            """
            n = len(coins)
            # T[i][n] First i coin-types to make up n amount, T[...][0] = 1, T[0][...] = 0
            T = [[0] * (amount + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                T[i][0] = 1
            for i in range(1, n + 1):
                for j in range(1, amount + 1):
                    # use i-th coin
                    if j - coins[i - 1] >= 0:
                        T[i][j] = T[i - 1][j] + T[i][j - coins[i - 1]]
                    else:
                        T[i][j] = T[i - 1][j]
            return T[n][amount]

        return fxr_labuladong()


sl = Solution()
print(sl.change(amount=5, coins=[1, 2, 5]))
