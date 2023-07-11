"""
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve():
            """
            Runtime: 8248 ms, faster than 6.62% of Python3 online submissions for Count Primes.

            REF: OS has excellenct explain on the outer/inner boundary
            """
            nonlocal n
            if n <= 2:
                return 0

            numbers = {}
            for p in range(2, int(n**0.5) + 1):
                if p not in numbers:
                    # why start from p*p rather 2*p, because all lower has been filter out in lower p!
                    for multiple in range(p * p, n, p):
                        numbers[multiple] = 1

            # exclude "1" and the number "n" itself
            return n - len(numbers) - 2
