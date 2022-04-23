"""
tag: easy, skills
Lookback:
- Good problem to practice skills & logic
- groupby type str match

Similar:
- 914
- 809
"""

from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def pvlkmrv_ptrs():
            """
            Runtime: 28 ms, faster than 97.48% of Python3 online submissions for Long Pressed Name.

            https://leetcode.com/problems/long-pressed-name/discuss/698368/Easy-Python-Solution
            1-pass, M: O(1)
            """
            i, j, m, n = 0, 0, len(name), len(typed)
            while j < n:
                # case 1: matched, incr both i&j
                if i < m and name[i] == typed[j]:
                    i += 1
                # case 2: unmatch, must be streched (aka typed is [ee])
                elif j > 0 and typed[j - 1] == typed[j]:
                    pass
                # ow, Failed
                else:
                    return False
                j += 1
            return i == m

        return pvlkmrv_ptrs()

        def fxr():
            """
            Runtime: 54 ms, faster than 34.51% of Python3 online submissions for Long Pressed Name.

            groupby is quite handy
            """
            enc = lambda s: [(k, len(list(grp))) for k, grp in groupby(s)]
            enc_name, enc_typed = enc(name), enc(typed)
            if len(enc_name) != len(enc_typed):
                return False
            for n, t in zip(enc_name, enc_typed):
                if n[0] != t[0]:
                    return False
                if n[1] > t[1]:
                    return False
            return True

        return fxr()


sl = Solution()
print(sl.isLongPressedName(name="alex", typed="aaleex"))
print(sl.isLongPressedName(name="saeed", typed="ssaaedd"))
print(sl.isLongPressedName("vtkgn", "vttkgnn"))
