"""
Basic Coding Skill
tag: easy
"""


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def fxr():
            """
            Runtime: 227 ms, faster than 85.81% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.

            since 2^N-1 <= 10^6 => N < 20
            """
            PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
            # return sum(1 for n in range(left, right + 1) if bin(n).count("1") in PRIMES)
            return sum(
                map(lambda x: bin(x).count("1") in PRIMES, range(left, right + 1))
            )
