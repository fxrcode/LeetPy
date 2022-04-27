"""
Tag: Easy, Math, Enumeration
Lookback:
- int(c) == c (c is float). eg. c = 5.0, then 5.0==5 => True
- Don't confuse a**a vs a**2
"""


from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        def fxr():
            # Runtime: 428 ms, faster than 61.22% of Python3 online submissions for Count Square Sum Triples.
            ans = 0
            for a in range(3, n + 1):
                for b in range(a + 1, n + 1):
                    c2 = a * a + b * b
                    c = sqrt(c2)
                    if int(c) == c and c2 <= n * n:
                        ans += 2
            return ans

        return fxr()


sl = Solution()
print(sl.countTriples(n=5))
print(sl.countTriples(n=10))
