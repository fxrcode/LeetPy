"""
tag: easy
Lookback:
"""
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def fxr():
            """
            Runtime: 75 ms, faster than 48.86% of Python3 online submissions for 1-bit and 2-bit Characters.

            T: O(N)
            """
            i = 0
            last_is_two = False
            while i < len(bits):
                if bits[i] == 0:
                    i += 1
                    last_is_two = False
                else:
                    i += 2
                    last_is_two = True
            return last_is_two == False
