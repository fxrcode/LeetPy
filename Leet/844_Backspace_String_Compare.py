"""
Tag: Easy, FB, 2ptr, skills
Lookback:
- 2ptr, str are good tag to practice basic coding skills

[] REDO
"""
from itertools import zip_longest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def yongzx_backward():
            """
            Runtime: 65 ms, faster than 6.96% of Python3 online submissions for Backspace String Compare.

            https://leetcode.com/problems/backspace-string-compare/discuss/161771/Python-O(1)-Space
            """
            i, j = len(s) - 1, len(t) - 1
            backs = backt = 0
            while i >= 0 or j >= 0:
                # i stops at non-deleted character in S or -1
                while i >= 0:
                    if s[i] == "#":
                        backs += 1
                        i -= 1
                    elif s[i] != "#" and backs > 0:
                        backs -= 1
                        i -= 1
                    else:
                        break
                # hi stops at non-deleted character in T or -1
                while j >= 0:
                    if t[j] == "#":
                        backt += 1
                        j -= 1
                    elif t[j] != "#" and backt > 0:
                        backt -= 1
                        j -= 1
                    else:
                        break
                # XXX
                if (i < 0 and j >= 0) or (j < 0 and i >= 0):
                    # eg. S = 'a#', T = 'a'
                    return False
                if (i >= 0 and j >= 0) and s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            return True

        return yongzx_backward()

        def fxr():
            """
            Runtime: 53 ms, faster than 8.06% of Python3 online submissions for Backspace String Compare.

            T: O(N)
            M: O(N)
            """

            def helper(s):
                stk = []
                for c in s:
                    if c != "#":
                        stk.append(c)
                    else:
                        if stk:
                            stk.pop()
                print("".join(stk))
                return stk

            return helper(s) == helper(t)

        def os():
            """
            Runtime: 32 ms, faster than 65.78% of Python3 online submissions for Backspace String Compare.

            clean logic
            """

            def F(s):
                skip = 0
                for x in reversed(s):
                    if x == "#":
                        skip += 1
                    elif skip:
                        skip -= 1
                    else:
                        yield x

            # print(list(F(s)))
            # print(list(F(t)))

            return all(x == y for x, y in zip_longest(F(s), F(t)))


sl = Solution()
print(sl.backspaceCompare(s="ab#c", t="ad#c"))
print(sl.backspaceCompare(s="ab##", t="c#d#"))
print(sl.backspaceCompare(s="a#c", t="b"))

print(sl.backspaceCompare("bxj##tw", "bxj###tw"))
