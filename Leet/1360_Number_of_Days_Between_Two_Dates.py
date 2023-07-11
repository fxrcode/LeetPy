"""
tag: Easy,
"""

from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def leihao1313():
            """
            Runtime: 32 ms, faster than 74.67% of Python3 online submissions for Number of Days Between Two Dates.

            https://leetcode.com/problems/number-of-days-between-two-dates/discuss/517582/Python-Magical-Formula/810920
            """

            def isleap(year):
                if year % 4 != 0:
                    return False
                elif year % 100 != 0:
                    return True
                elif year % 400 != 0:
                    return False
                return True

            days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            def f(date):
                y, m, d = map(int, date.split("-"))
                x = 365 * (y - 1971) + sum(map(isleap, range(1971, y)))
                return x + d + sum(days[:m]) + (m > 2 and isleap(y))

            return abs(f(date1) - f(date2))

        return leihao1313()

        # M = datetime.strptime(date1, '%Y-%m-%d').date()
        # N = datetime.strptime(date2, '%Y-%m-%d').date()
        # return abs((N - M).days)


sl = Solution()
print(sl.daysBetweenDates(date1="2019-06-29", date2="2019-06-30"))
print(sl.daysBetweenDates(date1="2020-01-15", date2="2019-12-31"))
print(sl.daysBetweenDates("1971-06-29", "2010-09-23"))
