"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- Proof: #digits of number n = floor(log(n))+1
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def fxr():
            """
            https://math.stackexchange.com/questions/231742/proof-how-many-digits-does-a-number-have-lfloor-log-10-n-rfloor-1

            XXX: number n's # digits = floor(log(n))+1
            T: O(logN)
            """
            x = n
            add = 0
            prod = 1
            while x:
                x, r = divmod(x, 10)
                prod *= r
                add += r
            return prod - add
