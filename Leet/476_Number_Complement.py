"""
Daily Challenge (Dec 27)
"""
from math import floor, log2


class Solution:
    def findComplement(self, num: int) -> int:
        def os_log():
            """
            Runtime: 32 ms, faster than 56% of Python3 online submissions for Number Complement.

            """
            n = floor(log2(num)) + 1
            bitmask = (1 << n) - 1
            return bitmask ^ num

        def os_1(n):
            """
            Runtime: 32 ms, faster than 55.58% of Python3 online submissions for Number Complement.

            """
            todo, bit = n, 1
            while todo:
                n ^= bit
                bit <<= 1
                todo >>= 1
            return n
