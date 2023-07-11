"""
Labuladong: 一行代码就能解决的算法题

Easy
tag: Math
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
