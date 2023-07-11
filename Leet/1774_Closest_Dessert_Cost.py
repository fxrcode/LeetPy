"""
✅ GOOD Backtrack/DP

tiktok tag
tag: medium, DP, backtrack, bisect

Lookback
- Core: subsets sum
- min(iter, key=lambda x: (abs(x-goal), x)) to find closest
- my 1st 二进制枚举迭代实现 (base-3, very slowwww)
"""

from functools import cache
from typing import List


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        def lenchen1112():
            """
            https://leetcode.com/problems/closest-dessert-cost/discuss/1085820/Python3-top-down-dp
            Runtime: 59 ms, faster than 92.92% of Python3 online submissions for Closest Dessert Cost.

            Return sum of subsequence closest to target.
            T: O(MNV)

            """

            @cache
            def dfs(i, cost):
                if cost >= target or i == len(tC):
                    return cost
                return min(
                    [dfs(i + 1, cost + tC[i] * j) for j in range(3)], key=closest
                )

            tC = toppingCosts
            closest = lambda x: (abs(x - target), x)
            return min([dfs(0, b) for b in baseCosts], key=closest)

        return lenchen1112()

        def base3():
            """
            Runtime: 1510 ms, faster than 32.92% of Python3 online submissions for Closest Dessert Cost.

            https://leetcode-cn.com/problems/closest-dessert-cost/solution/san-jin-zhi-mei-ju-bao-li-by-xin-lee-irq5/
            base-3 (二进制枚举)迭代实现.
            T: O(T*3^T) # T = len(toppings)
            """
            opt = 1e6
            for i in range(pow(3, len(toppingCosts))):
                topps, idx, cur = 0, i, 0
                while idx != 0:
                    idx, q = divmod(idx, 3)
                    topps += toppingCosts[cur] * (q)
                    cur += 1
                for b in baseCosts:
                    cost = topps + b
                    if cost == target:
                        return cost
                    if abs(cost - target) < abs(opt - target):
                        opt = cost
                    elif abs(cost - target) == abs(opt - target):
                        opt = min(cost, opt)
            return opt

        def ye15_a():
            """
            https://leetcode.com/problems/closest-dessert-cost/discuss/1085820/Python3-top-down-dp

            top-down dp
            T: O(2^N)
            """
            # tC = toppingCosts * 2
            tC = toppingCosts

            @cache
            def dp(i, x):
                """Return sum of subsequence of toppingCosts[i:] closest to x.
                #!Once x is negative, we can cut this branch.
                """
                if x < 0 or i == len(tC):
                    return 0
                ops = [
                    tC[i] * pick + dp(i + 1, x - tC[i] * pick) for pick in range(2 + 1)
                ]
                print(i, x, ops)
                return min(ops, key=lambda y: (abs(y - x), y))

            ans = 1e6
            for bc in baseCosts:
                ans = min(
                    ans, bc + dp(0, target - bc), key=lambda x: (abs(x - target), x)
                )
            return ans

        def fxr():
            """
            Runtime: 431 ms, faster than 65.17% of Python3 online submissions for Closest Dessert Cost.

            REF: https://leetcode.com/problems/closest-dessert-cost/discuss/1275679/Python%3A-Explained-Easy-Backtracking-with-Time-and-Space-complexity
            """

            def dfs(ti, p, cost):
                print("ti:", ti, "pick:", p, "cost:", cost)
                nonlocal ans, diff
                if abs(cost - target) < diff:
                    ans = cost
                    diff = abs(cost - target)
                elif abs(cost - target) == diff:
                    ans = min(ans, cost)
                # add all combi to res
                res.append(cost)
                if ti == len(toppingCosts):
                    return
                if cost > target:
                    return
                for pick in range(3):
                    dfs(ti + 1, pick, cost + toppingCosts[ti] * pick)

            res = []
            ans = diff = 1e6
            for b in baseCosts:
                dfs(0, 0, b)
            # res.sort()
            # print(res)
            return ans

        # return base3()
        # return ye15_a()
        # return fxr()


sl = Solution()

# print(sl.closestCost(baseCosts=[10], toppingCosts=[8, 3], target=17))
# sl.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10)
# print(sl.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10))
# print(sl.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18))
# print(sl.closestCost(baseCosts=[3, 10], toppingCosts=[2, 5], target=9))
print(sl.closestCost([5, 77, 38, 61, 97], [62, 7, 100, 30, 16, 84], 73))
