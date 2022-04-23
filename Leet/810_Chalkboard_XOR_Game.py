'''
tag: Brainteaser, Hard
Similar: 1908. Game of Nim: Sprague-Grundy theorem
'''

from typing import List
from operator import xor
from functools import reduce


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        def os():
            """
            Runtime: 76 ms, faster than 80.00% of Python3 online submissions for Chalkboard XOR Game.

            XXX: 1st time use functools.reduce()
            https://realpython.com/python-reduce-function/#getting-started-with-pythons-reduce

            """
            XOR = reduce(xor, nums)
            even = len(nums) % 2 == 0
            if XOR == 0 or even:
                return True
            return False

        return os()


sl = Solution()
print(sl.xorGame(nums=[1, 1, 2]))
