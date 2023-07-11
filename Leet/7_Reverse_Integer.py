"""
FB tag (medium)

Similar: 9. Palindrome Number

"""


class Solution:
    def reverse(self, x: int) -> int:
        def eastonlee():
            """
            https://leetcode.com/problems/reverse-integer/discuss/132861/3-lines-Python-Solution
            XXX: pythonic

            Runtime: 28 ms, faster than 91.94% of Python3 online submissions for Reverse Integer.

            """
            sign = [1, -1][x < 0]
            rst = sign * int(str(abs(x))[::-1])
            return rst if -(2**31) - 1 < rst < 2**31 else 0

        def fxr():
            """
            Your runtime beats 31.23 % of python3 submissions.

            """
            sig = 1 if x >= 0 else -1
            n = abs(x)
            rev = 0
            while n:
                n, m = divmod(n, 10)
                rev = rev * 10 + m

                if sig < 0:
                    if rev * sig < -(2**31):
                        return 0
                else:
                    if rev > 2**31 - 1:
                        return 0
            return rev * sig

        return eastonlee()


sl = Solution()
print(sl.reverse(x=123))
print(sl.reverse(x=-123))
print(sl.reverse(x=120))
print(sl.reverse(1534236469))
