"""
Kevin Facebook Tag

tag: Medium, Stack
Lookback
- parenthesis => Stack (Greedy)
- s[i] = '' # simple python to remove char at i-th pos

Similar:
- 301
- 678
- 921
- 2116
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def asivura(s):
            """
            Runtime: 122 ms, faster than 76.12% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.

            https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
            """
            ss = list(s)
            stk = []
            for i, c in enumerate(s):
                if c == "(":
                    stk.append(i)
                elif c == ")":
                    if stk:
                        stk.pop()
                    else:
                        ss[i] = ""
            while stk:
                ss[stk.pop()] = ""
            return "".join(ss)

        return asivura(s)


sl = Solution()
print(sl.minRemoveToMakeValid(s="lee(t(c)o)de)"))
