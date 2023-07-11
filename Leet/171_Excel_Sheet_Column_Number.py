"""
Completion Streak: 100 Days

Top Interview Questions

tag: easy
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def fxr():
            """
            Runtime: 50 ms, faster than 35.78% of Python3 online submissions for Excel Sheet Column Number.

            """
            res = 0
            for c in columnTitle:
                res = res * 26 + (ord(c) - ord("A") + 1)
            return res

        return fxr()


sl = Solution()
for ct in ["A", "AB", "ZY"]:
    print(sl.titleToNumber(ct))
