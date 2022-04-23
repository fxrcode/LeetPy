"""
Tag: Easy, Math
Lookback:
- gcd(a,b) must in 30sec
Similar 
- 952. Largest Component Size by Common Factor
UF + prime factors

"""


from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def fxr_gcd():
            """
            Runtime: 40 ms, faster than 99.93% of Python3 online submissions for Find Greatest Common Divisor of Array.

            AC in 1min :)
            """

            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a

            mn, mx = min(nums), max(nums)
            return gcd(mx, mn)
