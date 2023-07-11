"""

"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        def fxr():
            """
            Runtime: 20 ms, faster than 99.49% of Python3 online submissions for Base 7.

            """
            x, ans, time = abs(num), 0, 1
            while x:
                x, m = divmod(x, 7)
                ans += time * m
                time *= 10
            ret = str(ans)
            return "-" * (num < 0) + ret

        return fxr()


sl = Solution()
print(sl.convertToBase7(num=100))
print(sl.convertToBase7(num=-7))
print(sl.convertToBase7(num=349))
print(sl.convertToBase7(num=0))
