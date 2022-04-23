'''
tag: Probability, Medium

[ ] REDO
'''
from math import ceil
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        def lee215(n):
            """
            Runtime: 55 ms, faster than 28.57% of Python3 online submissions for Soup Servings.

            XXX: convert 1 serving = 25ml.  check lee215's detail analysis

            f(a,b) means the result probability for a ml of soup A and b ml of soup B.
              f(a-4,b) means that we take the first operation: Serve 100 ml of soup A and 0 ml of soup B.
              f(a-3,b-1), f(a-2,b-2), f(a-1,b-3) are other 3 operations.
            """
            @cache
            def dp(a, b):
                if a <= 0 and b > 0: return 1
                elif a <= 0 and b <= 0: return 0.5
                elif a > 0 and b <= 0: return 0
                return 0.25*(dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) \
                    + dp(a-1,b-3))

            if n > 5000: return 1
            n = ceil(n / 25)
            return dp(n, n)

        return lee215(n)


sl = Solution()
print(sl.soupServings(50))
print(sl.soupServings(100))