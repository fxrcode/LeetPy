"""
tag: easy
Lookback:
- TODO: find pattern
"""


class Solution:
    def countEven(self, num: int) -> int:
        def fxr():
            # Runtime: 48 ms, faster than 81.09% of Python3 online submissions for Count Integers With Even Digit Sum.
            return sum(1 for n in range(2, num + 1) if sum(map(int, str(n))) % 2 == 0)

        return fxr()


sl = Solution()
print(sl.countEven(4))
print(sl.countEven(30))
