"""
✅ GOOD Logic + Skills
tag: medium, logic
Lookback:
- lee215 so smart. If half split, no need to count all, simply A,B take turn to receive `(` and `)`!
"""

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        def lee215():
            """
            Runtime: 61 ms, faster than 57.51% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

            1-pass clear logic
            """
            A = B = 0
            res = [0] * len(seq)
            for i, c in enumerate(seq):
                if c == "(":
                    if A < B:
                        A += 1
                    else:
                        B += 1
                        res[i] = 1
                else:
                    if A > B:  # XXX: careful: mirror of '('
                        A -= 1
                    else:
                        B -= 1
                        res[i] = 1
            return res

        return lee215()

        def fxr():
            """
            Runtime: 83 ms, faster than 24.28% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

            """
            mxop = 0
            bal = 0
            for c in seq:
                if c == "(":
                    bal += 1
                    mxop = max(mxop, bal)
                else:
                    bal -= 1
            thrd = (mxop + 1) // 2
            print(thrd)
            res = [0] * len(seq)
            for i, c in enumerate(seq):
                if c == "(":
                    bal += 1
                    if bal > thrd:
                        res[i] = 1
                else:
                    if bal > thrd:
                        res[i] = 1
                    bal -= 1
            return res

        return fxr()


sl = Solution()
print(sl.maxDepthAfterSplit(seq="(()())"))
print(sl.maxDepthAfterSplit(seq="()(())()"))
print(sl.maxDepthAfterSplit(seq="()((())())"))
