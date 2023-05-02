"""
date: 04262023
tag: easy, math
Lookback:
- learn how to do analysis to find pattern!
"""


class Solution:
    def addDigits(self, num: int) -> int:
        def os_math(x):
            """
            REF: https://leetcode.com/problems/add-digits/discuss/68572/3-methods-for-python-with-explains

            Runtime: 40 ms, faster than 51.49% of Python3 online submissions for Add Digits.
            T: O(1)
            """
            if x == 0:
                return x
            return 9 if x % 9 == 0 else x % 9

        return os_math(num)

        def fxr(x):
            while x >= 10:
                x = sum(map(int, str(x)))
            return x


sl = Solution()
print(sl.addDigits(num=123))
