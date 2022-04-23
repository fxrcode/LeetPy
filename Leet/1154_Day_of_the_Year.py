'''
Teaching Kids & Wife Programming (Day 367)
'''


class Solution:
    def dayOfYear(self, date: str) -> int:
        def fxr():
            """
            Runtime: 80 ms, faster than 48.24% of Python3 online submissions for Day of the Year.

            XXX: careful on leap definition
            """
            yy, mm, dd = map(int, date.split('-'))
            leap = False
            if yy % 4 == 0 and yy % 100:
                leap = True
            elif yy % 400 == 0:
                leap = True
            days = [
                31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
            ]
            pre = [0] * 13
            for i in range(1, 13):
                pre[i] = pre[i - 1] + days[i - 1]
            ans = pre[mm - 1] + dd
            return ans

        return fxr()


sl = Solution()
print(sl.dayOfYear(date="2019-01-09"))
print(sl.dayOfYear(date="2019-02-10"))
print(sl.dayOfYear("1900-05-02"))
print(sl.dayOfYear("1901-05-02"))
print(sl.dayOfYear("2003-03-01"))