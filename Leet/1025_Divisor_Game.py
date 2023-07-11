"""
Tag: Math, Easy
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        # Runtime: 32 ms, faster than 70.85% of Python3 online submissions for Divisor Game.
        return n & 1 == 0
