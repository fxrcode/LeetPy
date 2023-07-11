"""
✅ GOOD DP (knapsack w/ many variables)
tag: Medium, DP, DFS
Lookback:
- apparently, this is DP problem, w/o greedy property, so you have to recursively try

[ ] REDO
"""

from functools import cache
from typing import List


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def sl3635():
            """
            Runtime: 60 ms, faster than 96.93% of Python3 online submissions for Shopping Offers.

            #  https://leetcode.com/problems/shopping-offers/discuss/145989/Clean-Python-solution%3A-Top-Down-%2B-Memorization-beats-100
            """

            @cache
            def dp(needs):
                # not take offer
                cost = sum(n * price[i] for i, n in enumerate(needs))
                # take one offer
                for offer in special:
                    for i, n in enumerate(needs):
                        if n < offer[i]:
                            break
                    else:
                        new_needs = tuple([n - offer[i] for i, n in enumerate(needs)])
                        # update cost
                        cost = min(cost, offer[-1] + dp(new_needs))
                return cost

            return dp(tuple(needs))

        return sl3635()

        """
        def fxr_WA():
            # This is Greedy, but WA here
            opt = sum(p * n for p, n in zip(price, needs))
            for offer in special:
                # cost = offer[-1]
                take = [1] * len(needs)
                for i in range(len(offer) - 1):
                    o, n = offer[i], needs[i]
                    if o > n:
                        break
                    else:
                        # cost += price[i] * (n - o)
                        take[i] = n // o if o else 2e9
                else:
                    take_offers = min(take)
                    cost = take_offers * offer[-1]
                    for i, o in enumerate(offer[:-1]):
                        cost += (needs[i] - take_offers * o) * price[i]
                    opt = min(opt, cost)
            return opt
        """


sl = Solution()
print(sl.shoppingOffers(price=[2, 5], special=[[3, 0, 5], [1, 2, 10]], needs=[3, 2]))
assert (
    sl.shoppingOffers(
        price=[2, 3, 4], special=[[1, 1, 0, 4], [2, 2, 1, 9]], needs=[1, 2, 1]
    )
    == 11
)
assert sl.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [0, 0, 0]) == 0
print(sl.shoppingOffers([0, 0, 0], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 1, 1]))
assert (sl.shoppingOffers([9, 9], [[1, 1, 1]], [2, 2])) == 2
assert (
    sl.shoppingOffers([2, 3], [[1, 0, 1], [0, 1, 2]], [1, 1]) == 3
)  # 56 / 64 test cases passed.
