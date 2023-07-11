"""
[ ] REDO

GOOD: char, indexing!
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Runtime: 20 ms, faster than 99.20% of Python3 online submissions for Excel Sheet Column Title.

        youtube: Michelle小梦想家
        XXX: whenever we do char <-> number, we use chr() <-> ord()
        XXX: char system is 0-index, so we need to n-1 to divmod in each loop:
            https://leetcode.com/problems/excel-sheet-column-title/discuss/441430/Detailed-Explanation-Here's-why-we-need-n-at-first-of-every-loop-(JavaPythonC%2B%2B)

        for String ABZ and its corresponding number n:
        n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0
        Equation:
        (n-1)%26 =  Z                                                  (1)
        (n-1)/26 = (A+1) * 26^1 + (B+1) * 26^0                         (2)
        """
        cn = columnNumber
        ans = ""
        # my init impl is ugly, and the indexing is confusing!!!
        # for i, c in enumerate(ascii_uppercase):
        #     i2c[i+1] = c
        while cn:
            ans += chr((cn - 1) % 26 + ord("A"))
            cn = (cn - 1) // 26
        return ans[::-1]


sl = Solution()
print(sl.convertToTitle(28))
