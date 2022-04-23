"""
tag: easy
Lookback:
- practice more for clean code
"""


class Solution:
    def reformat(self, s: str) -> str:
        def JummyEgg():
            """
            Runtime: 77 ms, faster than 32.94% of Python3 online submissions for Reformat The String.

            """
            a = [c for c in s if c.isalpha()]
            b = [c for c in s if c.isdigit()]
            if len(a) < len(b):
                a, b = b, a
            if len(a) - len(b) > 1:
                return ""

            rv = []
            while a:
                rv.append(a.pop())
                if b:
                    rv.append(b.pop())
            return "".join(rv)

        return JummyEgg()


sl = Solution()
for s in ["a0b1c2", "leetcode", "a0b1c23", "a0b1c234"]:
    print(sl.reformat(s))
