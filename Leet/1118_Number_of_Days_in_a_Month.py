"""
Tag: Easy, Math
Lookback:
- prerequisite of leap year/calendar
"""


class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        def ye15():
            """
            Runtime: 19 ms, faster than 97.26% of Python3 online submissions for Number of Days in a Month.

            https://leetcode.com/problems/number-of-days-in-a-month/discuss/416459/Python-3-self-explained-solution
            """
            leap = lambda Y: Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0
            if M in {1, 3, 5, 7, 8, 10, 12}:
                return 31
            elif M != 2:
                return 30
            else:
                return 28 + leap(Y)

        return ye15()


sl = Solution()
print(sl.numberOfDays(1992, 7))
print(sl.numberOfDays(2000, 2))
print(sl.numberOfDays(1900, 2))
