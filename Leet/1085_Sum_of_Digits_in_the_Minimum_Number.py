'''
tag: easy

similar: 258.Add Digits
'''

from typing import List


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        def fxr():
            """
            Runtime: 52 ms, faster than 38.21% of Python3 online submissions for Sum of Digits in the Minimum Number.

            T: O(N)
            """
            if sum(map(int, str(min(nums)))) % 2 == 1:
                return 0
            else:
                return 1
