"""
Tag: Easy, Skill, math
Lookback:
- Two's Complement: num &= 0xFFFF_FFFF
"""


class Solution:
    def toHex(self, num: int) -> str:
        def bw1226():
            """
            Runtime: 28 ms, faster than 94.02% of Python3 online submissions for Convert a Number to Hexadecimal.

            https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/719521/Easiest-Python-Solution
            """
            nonlocal num
            if num == 0:
                return "0"
            mp = "0123456789abcdef"
            res = []
            # if neg (2's complement)
            num &= (1 << 32) - 1
            while num:
                num, d = divmod(num, 16)
                res.append(mp[d])
            return "".join(res[::-1])

        return bw1226()


sl = Solution()
print(sl.toHex(26))
print(sl.toHex(-1))
